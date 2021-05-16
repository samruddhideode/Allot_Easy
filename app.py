'''
Main function which provides the interface for the firs and the last page of the application.
'''

import time
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from menu import Menu

mymenu = Menu()  # obj of class Menu

def run_app():
    #opening page interface
    img1 = open('E:\SAMRUDDHI\SY\Buffer_2.0-FINAL\images\welcome.png', 'rb').read()
    style(put_image(img1, width='100%'),'display: block; margin-left: auto; margin-right: auto;')
    put_processbar('bar')
    for i in range(1, 11):
        set_processbar('bar', i / 10)
        time.sleep(0.8)
    time.sleep(2)
    clear()
    
    #Displays Main Menu, program works till choice is not 4(log out)
    while(mymenu.user != 4):
        img2 = open('E:\SAMRUDDHI\SY\Buffer_2.0-FINAL\images\college.png', 'rb').read()
        style(put_image(img2, width='100%'), 'display: block; margin-left: auto; margin-right: auto;')
        mymenu.login()
        if mymenu.user == 2:
            clear()
            mymenu.menu_for_student()
        elif mymenu.user == 3:
            clear()
            mymenu.menu_for_admin()
        clear()
        
    #closing page interface
    img = open('E:\SAMRUDDHI\SY\Buffer_2.0-FINAL\images\goodbye.png', 'rb').read()
    style(put_image(img, width='80%'),'display: block; margin-left: auto; margin-right: auto;')
    time.sleep(10)
    clear()

if __name__=='__main__':
    pasrser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080)
    args = parser.parse_args()
    start_server(run_app , port=args.port)
