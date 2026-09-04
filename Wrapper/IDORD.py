import os
import sys
import time

BASE_DIR = os.getcwd()


class Colors:
    """Terminal color codes.

    Remember to append ``Colors.ENDC`` after each colored segment, e.g.::

        print(Colors.WARNING + "Warning" + Colors.ENDC)
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def configure_django():
    """Reset the local SQLite datastore and apply a fresh schema."""
    print("Step 2/4")
    os.system("rm -f db.sqlite3")
    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")
    os.system("python3 manage.py flush --no-input")


def crawl():
    """Run the Scrapy spiders that gather links from the target."""
    try:
        os.system("clear")
        os.system("cd idord_infograther && scrapy crawl railsgoatNotLogin")
        os.system("cd idord_infograther && scrapy crawl railsgoatLogin")
    except OSError:
        pass


def attack():
    """Run the attack/detection stage against the crawled links."""
    print("Step 4/4")
    os.system("python3 Attack.py")


def take_input():
    """Prompt for the target link and hand it to the crawler."""
    os.system("clear")
    print("Please Enter the web link: ")
    text = input()
    os.chdir("idord_infograther")
    with open("link_to_crawl.txt", "w") as handle:
        handle.write(text.strip())
    os.chdir(BASE_DIR)


def sec_to_min(seconds):
    """Format a duration in seconds as ``M mins S seconds``."""
    minutes = str((seconds % 3600) // 60)
    remaining = str(round((seconds % 3600) % 60))
    return f"{minutes} mins {remaining} seconds"


def main():
    print("Step 1/4")
    try:
        url = sys.argv[1]
        print(f"<================> {url} <================>")
    except IndexError:
        print("<_____Using default_____>")

    configure_django()
    take_input()

    start = time.time()
    crawl()
    attack()
    end = time.time()

    print(f"Total time took: {sec_to_min(end - start)}")


if __name__ == "__main__":
    main()
