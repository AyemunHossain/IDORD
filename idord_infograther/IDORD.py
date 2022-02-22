import os
import subprocess

cmd = 'scrapy crawl prothomalo'
# os.system(cmd)

x = subprocess.check_output(['scrapy', 'crawl', 'prothomalo'])

print(f">>>>>>>>>>>>>>>>>{x}>>>>>>>>>>>>>>")




#Below this for Production 
# from subprocess import Popen, PIPE


# print("Step 1/X")
# p = Popen(['scrapy', 'crawl', 'prothomalo'], stdout=PIPE, stderr = PIPE)
# output = p.communicate()[0]
# if p.returncode != 0: 
#     print("> Setp Failed")
# else:
#     print("> Setp 1 Completed Successfully")