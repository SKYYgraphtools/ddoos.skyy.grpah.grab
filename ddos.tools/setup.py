from http.client import OK
from operator import truediv
from pdb import Restart
from statistics import variance
from tracemalloc import stop
import time
from requests import delete

ref = True

def startv2():
    input("bienvenue")
def disclameur():
    print("""bonjour est bienvenue dans mon tools \n
    je decline tout action mauvaise que vous pourriez faire avec se tools""")




def helpddos():
    if helpddos== "help":
        print("""bienvenue dans le menue help
                -layer4
                    -udp
                    -tcp""")





def logs():
    if logs == "login":
        user = input("entre ton user name: ")
        mdp = input("entre ton mdp: ")
        print("user save")

def start():
    tddos = input("""
    qu'elle type de ddos veux tu utliser ?\n    layer 4  [1] \n    layer 7  [2]\n reponse : """)
    if tddos == "1":
        print("bienvenue dans le layer 4")
        layer4()
    if tddos == "2":
        layer7()
    reboot()    
    

def layer4():

    layer4_choix = input("""udp [1] \ntcp [2] \n reponse :  """)
    if layer4_choix == "1":
        ip =input("•IP      :")
        #if ip 
        input("•PORT    :")
        input("•THREAD  :") 
        print("attack run ") 
        stop = input("pour stopper l'attack fait stop\n utlsie ping pour voir l'etat de la co ")  
        if  stop == "stop":
            ("end attack")

    if layer4_choix == "2":
        input("•IP      :")
        input("•PORT    :")
        input("•THREAD  :")
        stop = input("pour stopper l'attack fait stop\n utlsie ping pour voir l'etat de la co ")  
        if  stop == "stop":
            ("end attack")



def layer7():
    tl4 =input("bienvenue dans le layer 7 \n http crash [1]:")
    if tl4 =="1":
        input("•link     :")
        stop = input("pour stopper l'attack fait stop utlises le module ping pour voir l'etat du site")  
    if  stop == "stop":
            ("end attack")

def countdown(num_of_sec):
    num_of_sec   = input ("TIME(s) :")
    while num_of_sec:
        m, s = str(divmod)(num_of_sec, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_sec -= 1
        
    print('Countdown finished.')
    

def reboot():
    global ref
    while ref :
        choix = input("veux tu reboot le tools \n oui[1]\n non [2] \n :")
        if choix != "1" : ref = False
        else : start()

    
