'''
menu.py has interfaces functions for the Main Menu,
Menu for Student Login and for Admin login.
'''
from pywebio.input import *
from pywebio.output import *
from os import system, name
from database import *
from pywebio import STATIC_PATH
import time

mydata= Data() #object of class Data

#validation functions
def check_login(p):
    if (p<1 or p>4):
        return ('invalid input!')
def check_student_login(p):
    if (p<1 or p>7):
        return('invalid input!')
    
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')


class Menu:
  def __init__(self):
    
    self.user= None

  def login(self):
    clear()
    #list of Main Menu options
    listMainMenu = [
        'Sign Up', 
        'Login as Student', 
        'Login as Admin', 
        'Exit'
        ]
    
    ch = radio(label='MENU', options=listMainMenu, inline=False,
                   validate=None, name=None, value=None, required=True)
    
    #maps a choice from the Main Menu to an integer
    dictMainMenu = {
        'Sign Up':1, 
        'Login as Student':2,
        'Login as Admin':3,
        'Exit':4
        }
    
    user_inp = dictMainMenu[ch]
    self.user = user_inp
    
    if user_inp==1: #Signup for students is selected
        clear()
        mydata.student_sign_up()
    
    if user_inp==2 : #Login as student is selected
        data = input_group("Enter details",[
            input('Enter name' , name = 'name', required =True),
            input('Enter surname', name ='surname', required = True)
            ])
        
        name = data['name']
        surname = data['surname']
        
        mydata.set_userinfo(2,name,surname) #send user info to database file
        
        is_correct_pswd = mydata.check_pswd(name, surname)
        if(is_correct_pswd==1):  #Name and password match
            put_success(f"\n Welcome, {name.capitalize()}!")
            time.sleep(2)
            return
        else: #Username or password or both do not match
            put_error("Sorry! Incorrect credentials. ") 
            time.sleep(1)
            clear()
            self.login()
        
    if user_inp ==3: #Login as admin is selected
        #(pwd for admin is 12345)
        pwd= input("Enter password:", type=PASSWORD)
        if (pwd =="12345"):
            put_success("Welcome, Admin!")
            mydata.set_userinfo(3,"admin","") # send user info to database file
            time.sleep(2)
        else:
            put_error("Sorry wrong password! ")
            self.login()

  def menu_for_student(self):
    clear() 
    choice= None
    #breaks out of loop when 6 i.e. logout is selected
    while(choice!=7): 
        img2 = open('welcome2.png', 'rb').read()
        put_image(img2, width='50%')   
        if mydata.flag==0: #flag=0 indicates user has not withdrawn his application.
            #List of Student Menu Options
            listStudentMenu = [
                'View Seat Matrix',
                'Check application status',
                'Complete your application', 
                'Withdraw Application',
                'View Cutoff Marks',
                'Change password',
                'Logout'
                ]
            ch = radio(label='STUDENT MENU', options=listStudentMenu, inline=False, validate=None, name=None, value=None, required=True, help_text=None)
            #Maps a choice from the Student Menu to an integer
            dictStudentMenu = {
                'View Seat Matrix':1,
                'Check application status':2,
                'Complete your application':3,
                'Withdraw Application':4,
                'View Cutoff Marks':5,
                'Change password':6,
                'Logout':7
                }
            choice= dictStudentMenu[ch]
            
        else: 
            '''flag=1 is the case where user has withdrawn the application. 
            So we do not show him any other option and force him to logout.'''
            choice=7
            
        if choice!=7:
            '''When any choice other than logout is selected, 
            call the corresponding function from the functions list in database.py'''
            mydata.student_options[choice-1](mydata)
    return


  def menu_for_admin(self):
    clear() 
    choice= None 
    #breaks out of loop when 8 i.e. logout is selected
    while(choice!=7):  
        #List of Admin Menu Options
        img3 = open('welcome1.png', 'rb').read()
        put_image(img3, width='30%')
        listAdminMenu = [
            'Run Seat Allotment Process',
            'View full allotment result',
            'View branchwise allotment list',
            'Search a student',
            'View list of students left without allotment',
            'Get data of vacancies left',
            'Log out'
            ]        
        ch = radio(label='ADMIN MENU', options=listAdminMenu, inline=False, validate=None, name=None, value=None, required=True, help_text=None)
        #Maps a choice from Admin Menu to an integer
        dictAdminMenu = {
            'Run Seat Allotment Process':1,
            'View full allotment result':2,
            'View branchwise allotment list':3,
            'Search a student':4,
            'View list of students left without allotment':5,
            'Get data of vacancies left':6,
            'Log out':7
            }
        choice=dictAdminMenu[ch]
        
        if choice!=7: 
            '''when any choice other than logout is selected,
            call the corresponding function from the functions list in database.py'''
            
            if choice!=1: 
                '''all functions other than 'run allotment' are present in class Data.
                They require an object of this class to be passed as parameter.'''
                mydata.admin_options[choice-1](mydata)   
            else:
                '''if choice 1 is selected, this run allotment function is
                present in a diff class than other functions and hence does
                not require the object of class Data to be passed as paramenter.'''
                mydata.admin_options[0]() 
    return
    
