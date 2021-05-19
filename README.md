# Allot Easy
This is a group project as a part of the Buffer 2.0 project series organised by Team Loop of Cummins College of Engineering, Pune.
Students can apply for a degree program at an engineering college. Students are admitted taking in consideration their marks and course preferences. 
This project aims to simulate the admission process for Engineering Colleges every year in Maharashtra.

The code is divided mainly into 2 parts:
Admin and Student.
There are different functionalities available to the user depending upon whether he/she is an Admin or a Student.

Some important functionalities available to Student Users:
  1. Sign Up: A new Student has to register and set his username and password before he can log into the application and access further functionalities.
  2. Login for Students: Student has to log into the application with his username and password.
  3. Students can update their record with their course prefernces, marks and other details. (This functionality is available only till the Admin hasn't run the allotment process)
  4. Students can withdraw their application.(This functionality is available only till the Admin hasn't run the allotment process)
  5. Students can view the cut off marks of various Engineering Courses that the college offers. (This functionality is available only after the Admin has run the allotment process)

Some important functionalities available to the Admin:
  1. Admin can *run the allotment* process after which the Students are admitted to a course of their choice depending upon their marks and preferences.
  2. Admin can view the details of any Student who has applied to the college.
  3. Admin can view the vacant seats of a course and also the details of the students who haven't been admitted in the college. (This functionality is available only after the Admin has run the allotment process)
  4. Admin can also view the details of all the students who have been admitted to a particular course.
  
Language: Python
Libraries used: Pandas, csv and pywebio (for GUI)  
