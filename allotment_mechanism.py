from pywebio.input import *
from pywebio.output import *
import time
import pandas as pd
from csv import *
 
comp_allotment=[]
IT_allotment=[]
mech_allotment=[]
elec_allotment=[]
all_allotments=[comp_allotment, IT_allotment, mech_allotment, elec_allotment]
no_allotment = []
    
class Allotment_mechanism:
    
    
    def __init__(self):
        self.allotment_done= False
        self.vacancies={0: 15, 1: 15, 2: 15, 3: 15}
                
    def run_allotment(self):
        
        global comp_allotment, IT_allotment, mech_allotment, elec_allotment, all_allotments, no_allotment
        
        if self.allotment_done== True:
            confirm = actions('Do you want to reset the Allotment Process?', ['Reset', 'Back'],)
            if confirm=='Reset':
                self.allotment_done= False;
                self.vacancies={0: 15, 1: 15, 2: 15, 3: 15}
                global comp
                comp_allotment=[]
                IT_allotment=[]
                mech_allotment=[]
                elec_allotment=[]
                all_allotments=[comp_allotment, IT_allotment, mech_allotment, elec_allotment]
                no_allotment = []
            else:
                return
        else:
            #UI
            put_text("Running allotment process.. please wait") 
            put_processbar('bar');
            for i in range(1, 11):
                set_processbar('bar', i / 10)
                time.sleep(0.2)
                
            df = pd.read_csv("datasheet.csv")
            allotment_pre = df[(df['PREF1']>=0) & (df['PREF2']>=0) & (df['PREF3']>=0)]
            allotment = allotment_pre.sort_values('MARKS', ascending = False)
            dict1 = {}
            for i in range(len(allotment)):
                (surname, marks,pref1,pref2,pref3) = (allotment.iloc[i][1],allotment.iloc[i][3],allotment.iloc[i][4],allotment.iloc[i][5],allotment.iloc[i][6])
                dict1[allotment.iloc[i][0]]= (surname,marks,pref1,pref2,pref3)

            for regis in dict1:
                pref1 = dict1[regis][2]
                pref2 = dict1[regis][3]
                pref3 = dict1[regis][4]
                
                if(self.vacancies[pref1]>0):
                    self.vacancies[pref1]-=1
                    all_allotments[pref1].append((regis,dict1[regis][0]))
                elif(self.vacancies[pref2]>0):
                    self.vacancies[pref2]-=1
                    all_allotments[pref2].append((regis,dict1[regis][0]))
                elif(self.vacancies[pref3]>0):
                    self.vacancies[pref3]-=1
                    all_allotments[pref3].append((regis,dict1[regis][0]))
                else:
                    no_allotment.append((regis,dict1[regis][0]))
            
            
            #****************Allotment done***********************************
            self.update_allotments()
            self.allotment_done= True
            #after 2 secs wait, print the allotment process completed.
            put_success("Allotment process completed.") 
            
    def get_no_allotment_data(self):
        return no_allotment

    def get_row(self, person):
        with open("datasheet.csv",'r') as f: 
            reader_object= reader(f)
            for row in reader_object:
                if(row[0]==person[0]) and row[1]==person[1]:
                    # return the row no. where record is found
                    return reader_object.line_num
        clear()
    def update_allotments(self):
        global comp_allotment, IT_allotment, mech_allotment, elec_allotment
        row_to_edit =-1
        lines=[]
        with open("datasheet.csv",'r') as f:
            lines= f.read().splitlines()
    
            for person in comp_allotment:
                row_to_edit= self.get_row(person)
                all_fields= lines[row_to_edit-1].split(",")
                lines[row_to_edit-1]=f"{all_fields[0]},{all_fields[1]},{all_fields[2]},{all_fields[3]},{all_fields[4]},{all_fields[5]},{all_fields[6]},Computer,{all_fields[8]}"
            
            for person in IT_allotment:
                row_to_edit= self.get_row(person)
                all_fields= lines[row_to_edit-1].split(",")
                lines[row_to_edit-1]=f"{all_fields[0]},{all_fields[1]},{all_fields[2]},{all_fields[3]},{all_fields[4]},{all_fields[5]},{all_fields[6]},IT,{all_fields[8]}"

            for person in mech_allotment:
                row_to_edit= self.get_row(person)
                all_fields= lines[row_to_edit-1].split(",")
                lines[row_to_edit-1]=f"{all_fields[0]},{all_fields[1]},{all_fields[2]},{all_fields[3]},{all_fields[4]},{all_fields[5]},{all_fields[6]},Mechanical,{all_fields[8]}"


            for person in elec_allotment:
                row_to_edit= self.get_row(person)
                all_fields= lines[row_to_edit-1].split(",")
                lines[row_to_edit-1]=f"{all_fields[0]},{all_fields[1]},{all_fields[2]},{all_fields[3]},{all_fields[4]},{all_fields[5]},{all_fields[6]},Electronics,{all_fields[8]}"
        
        with open("datasheet.csv",'w') as f:
            # overwrite
            for line in lines:
                f.write(line+"\n")    
        clear()
    def get_cutoffs(self, branch):
        with open("datasheet.csv",'r') as f:
            reader_object= reader(f)
            if branch=="comp":
                last_person = comp_allotment[-1]
            elif branch =="it":
                last_person = IT_allotment[-1] 
            elif branch =="mech":
                last_person = mech_allotment[-1]  
            elif branch =="entc":
                last_person = elec_allotment[-1]   

            for row in reader_object:
                if row[0]==last_person[0] and row[1]== last_person[1]:
                        # return the row no. where record is found
                        return row[3]
        clear()
