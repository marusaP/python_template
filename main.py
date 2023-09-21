#! /usr/bin/python2

# za izvajanje pozeni  chmod +x main.py 
#./main.py
import time         #dodan modul za nadzor casa v programu
"""#######################################################
Primer dodajanja modulov 
##########################################################"""
#from time import sleep
#from time import *              #importaj vse
#import time as t    # preimenujemo modul

def main():     # dodamo funkcijo main za omejiev scope
    
    print("moje besedilo")      #primer print stavka
    print("moje stevilo: %d" % 5)  #primer formatranja stevil v stringu (print formats)
    time.sleep(1.54)        # primer cakanja 1.54 sekunde

if __name__ == "__main__":          # preverimo ce je bil program zagnan kot modul ali kot program 
    main ()                     # klicemo funkcijo main 