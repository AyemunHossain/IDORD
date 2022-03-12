import os
import subprocess


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

print("Step 1/X")
# p = Popen(['scrapy', 'crawl','railsgoatNotLogin'],cwd='idord_infograther/', stdout=PIPE, stderr = PIPE)

url = sys.argv[1]
print(f"================={url}================")

# os.system(f"cd idord_infograther && scrapy crawl railsgoatNotLogin")
# os.system(f"cd idord_infograther && scrapy crawl signupRailsgoat -a start_url={url}")
os.system(f"cd idord_infograther && scrapy crawl railsgoatLogin")



# p = Popen(['scrapy', 'crawl','signupRailsgoat','-a',f'start_url={url}',],cwd='idord_infograther/', stdout=PIPE, stderr = PIPE)

# output = p.communicate()[0]

# if p.returncode != 0: 
#     print(f'------------{p.communicate()}-------------')
#     print("> Setp Failed")
# else:
#     print("> Setp 1 Completed Successfully")