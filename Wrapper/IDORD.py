import os
import subprocess
import sys


BASE_DIR = os.getcwd()

class colors:
    """Note you need to add  colors.ENDC every time you changed the color 
       like this : 
       print(colors.WARNING + "Warning" + colors.ENDC)
    """
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# x = subprocess.check_output(['scrapy', 'crawl', 'prothomalo'], cwd='idord_infograther/')

# print(f">>>>>>>>>>>>>>>>>{x}>>>>>>>>>>>>>>")



#Below this for Production 
from subprocess import Popen, PIPE
import sys
import os

print("Step 1/4")
# p = Popen(['scrapy', 'crawl','railsgoatNotLogin'],cwd='idord_infograther/', stdout=PIPE, stderr = PIPE)

try:
    url = sys.argv[1]
    print(f"<================> {url} <================>")
except:
    print("<_____Using default_____>")

# os.system(f"cd idord_infograther && scrapy crawl railsgoatNotLogin")
# os.system(f"cd idord_infograther && scrapy crawl signupRailsgoat -a start_url={url}")

# os.system(f"python3 Attack.py") call a file to store base information here
def configure_django():
    print("Step 2/4")
    os.system(f"python3 manage.py makemigrations")
    os.system(f"python3 manage.py migrate")
    os.system(f"python3 manage.py flush --yes")


def crawl():
    os.system(f"clear")
    print("Please Enter the web link: ")
    
    try:
        pass
        # text = input()

        # os.chdir('idord_infograther')
        # file= open("link_to_crawl.txt","w")
        # file.write(text)
        # file.close()
        # os.chdir(BASE_DIR)
        
        # os.system(f"clear")
        # os.system(f"cd idord_infograther && scrapy crawl railsgoatNotLogin")
        # os.system(f"cd idord_infograther && scrapy crawl railsgoatLogin")
        # print("Step 3/4")

    except:
        pass

def attack():
    print("Step 4/4")
    os.system(f"python3 Attack.py")


configure_django()
crawl()
attack()


# p = Popen(['scrapy', 'crawl','signupRailsgoat','-a',f'start_url={url}',],cwd='idord_infograther/', stdout=PIPE, stderr = PIPE)

# output = p.communicate()[0]

# if p.returncode != 0: 
#     print(f'------------{p.communicate()}-------------')
#     print("> Setp Failed")
# else:
#     print("> Setp 1 Completed Successfully")