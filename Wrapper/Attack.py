# from curses.ascii import isdigit
# import os, django, re, sys
# from platform import mac_ver
# BASE_DIR = os.path.dirname(os.path.abspath('./Wrapper'))
# sys.path.append(BASE_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'Wrapper.settings'
# django.setup()
# from core.models import *


# BASE_LINK = "http://localhost:3000"

# def has_numbers(inputString):
#     return any(char.isdigit() for char in inputString)

# def generateAttack():
#     for link in LinkItem.objects.all():
#         if(has_numbers(link.link)):
            
#             # full_link = BASE_LINK+str(link.link)
#             matching = re.split("\W+",str(link.link))
#             # print(','.join(out))
#             for i in range(len(matching)):
                
#                 original= matching[i]
#                 try:
#                     if isdigit(original):
#                         for j in range(25):
#                             matching[i]=str(j)
#                             obj = LinkActionItem.objects.create(link=BASE_LINK+'/'.join(matching),orginal_param=original,manupulated_param=matching[i])
#                             obj.save()

#                 except Exception as e:        
#                     pass
#                     # print(e)

# generateAttack()

import requests
def get_attack(headers):
    session = requests.Session()
    session.headers.update(headers)
    print(session.headers)
    


    



def attack():
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'email':'a@a.com','password':'ashikashik'}

    session = requests.Session()
    r = session.post('http://0.0.0.0:3000/sessions/',headers=headers,data=payload)
    header = dict(r.headers)
    d = session.get("http://0.0.0.0:3000/dashboard/home",headers={'Set-Cookie':header['Set-Cookie'],'X-Request-Id':header['X-Request-Id']})


attack()




def post_attack():
    pass

def put_attack():
    pass
def patch_attack():
    pass
def delete_attack():
    pass




















