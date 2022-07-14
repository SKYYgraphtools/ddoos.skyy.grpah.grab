from statistics import variance
from tracemalloc import stop
import time
from requests import delete
def startv2():
    input("bienvenue")

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
        print("bienvenue dans le layer7")
        
    

def layer4():

    layer4_choix = input("""udp [1] \ntcp [2] \n reponse :  """)
    if layer4_choix == "1":
        input("•IP      :")
        input("•PORT    :")
        input("•THREAD  :") 
        print("attack run ") 
        stop = input("pour stopper l'attack fait stop")  
        if  stop == "stop":
            ("end attack")

    if layer4_choix == "2":
        input("•IP      :")
        input("•PORT    :")
        input("•THREAD  :")
        stop = input("pour stopper l'attack fait stop")  
        if  stop == "stop":
            ("end attack")



def layer7():
        
        
        input("•IP      :")
        input("•PORT    :")
        input("•THREAD  :")
        input("•TIME(s) :")
       


def countdown(num_of_sec):
    num_of_sec   = input ("TIME(s) :")
    while num_of_sec:
        m, s = str(divmod)(num_of_sec, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_sec -= 1
        
    print('Countdown finished.')
    


