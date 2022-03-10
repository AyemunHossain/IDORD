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


print("Step 1/X")
p = Popen(['scrapy', 'crawl', 'prothomalo'],cwd='idord_infograther/', stdout=PIPE, stderr = PIPE)
output = p.communicate()[0]
if p.returncode != 0: 
    print("> Setp Failed")
else:
    print("> Setp 1 Completed Successfully")