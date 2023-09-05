# Hospital Management System
Hospital Management System using MySQL,Django and Bootstrap

## Prerequisites
1. Install Django
2. Install mathfilters (pip3 install django-mathfilters)
3. Install flags (pip install django-flags)
4. install mysql-client (pip install mysqlclient)

## Languages and Technologies used
1. HTML5/ CSS3
2. JavaScript (to create dynamically updating content)
3. Bootstrap 5.0.1 (An HTML, CSS, and JS library)
5.Django for the backend
6. MySQL (An RDBMS tpip install mysqlclient.
hat uses SQL)
7. System File storage to store all the files

## Steps to run the project in your machine
1. Download and install Django in your machine
2. Install all the prerequisites
3. Clone the project into your local storage
4. Change the mysql password and username to yours in DATABASES of settings.py file in HMS folder inside the Code directory
5. Add a database named HospitalManagementSystem by running ( CREATE DATABASE HospitalManagementSystem ) in your mysql workbench
6. To create the tables for the database, run models of all apps periodically in order doctor,patient,receptionist,administration,wardclerk,medical_assistant,diagnostician,billing_desk,pharmacy_technician using power shell
7. As follows- 
8. open power shell and cd to the Code folder of the project
9. python manage.py makemigrations <app_name>
10. python manage.py migrate
11. for all apps in above order
12. Open mysql and add an administrator to the database at administration_administrator
13. Now you are ready to run the server.
14. Run it using command - python manage.py runserver 
    
### SOFTWARES USED
  - Django was installed on the Windows 11 machine and MySQL were initialized. And, files were built inside C Drive
  - VS Code Text was used as a text editor.
  - Google Chrome Browser was used to run the project (localhost/myhmsp was used as the url).
  
## GETTING INTO THE PROJECT:
Hospital Management System is a website to digitalize the hospital management using python django. This system has a ‘Home’ page from where the patient can login using patient login and staff using staff login buttons available on the home page. Given below image 1.1 is the image of the home page of the website

![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/glimpse%20of%20home%20page.png)

Given below are the patient and staff login pages respectively
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/patientlogin.png)
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/stafflogin.png)
# Patient 
Patient after logging in can navigate to patient info page available in the nav bar ,
there he can view all the appointments bills and reports of him.
given below is the image of patient info page
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/patientinfopage.png)
# Doctor
Doctor after logging in can navigate to Appointment info page available in the nav bar ,
there he can view all the appointments and the medical and diagnosis reports assigned to him.
given below is the image of Appointment info page
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/appointmentinfopage.png)
there by clicking on view details following page will show up
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/viewdetaispage.png)
# Medical Assistant
Each medical assistant is assigned to a doctor. He can also view all the appointments of the doctor. Different from the doctor he will be the one who adds the medical report of that visit or assigns patient to ward or diagnosis. And also changes the status of the appointment using the additional edit button available to him
Edit page will be as follows
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/editpage.png)
# Receptionist
Receptionist can Register a new patient
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/registration.png)
Can Appoint Doctor to a patient
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/patientappointment.png)
Or can see all the Ward and Doctor details
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/wardanddoctor.png)
Can also see all the patients registered in the hospital
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/seepatients.png)
# Diagnostician
Diagnostician can see all the appointments waiting for the diagnosis or already diagnosed. He/She can also add the diagnosis report and Diagnosis bill pdf aswell as the amount of bill for each Appointment who needs diagnosis as shown belo
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/diagnosisinfopage.png)
# Pharmacy Technician
Pharmacy Technician can add a bill for the pharmacy a patient has bought for a particular appointment, along with the total bill in numbers as shown below
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/pharmacypage.png)
# Ward Assistant
Ward Assistant can see the details of all patients in his ward. Along with removing the patient after his stay along with adding a Ward bill and the amount in ruppes as shown below
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/warddetailspage.png)
# Biller
Biller can view all the bills and update the final bill as follows
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/editbills.png)
# Administrator
Administrator can view all the employess of the hospital and can all kinds of new staff using the dropdown provided
![image](https://github.com/Sreekara-Madyastha/Hospital-Management-system/blob/master/photos/admininfopage.png)
by selecting one a new registration page is provided from there a new staff will be created.

# Logout
Any Staff or Patient can be logged out using the log out button in the home page
