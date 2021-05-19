# Attendance-Management-System
A face-recognition based student attendance management system using OpenCV

This **“Attendance Management System”** (Prototype) is a stand-alone Python back-end application developed using Python and TensorFlow as backend and uses the Machine Learning algorithms of OpenCV2 to detect faces. The programming language used is Python. The GUI for the front-end of this prototype is the Python Tkinter Application. Along with TensorFlow, Keras and SQLlite3 is used for the database. The prerequisite for running this app is Python, Tensorflow and SQLlite3 installed on your computer. 

**Features available:**  
1.	Register a new student or teacher with their required details.    
2.	Take multiple images of the newly registered student/teacher as training images. 
3.	Train the machine on the new set of images. 
4.	Attendance is marked in the sheet once the machine recognizes the users face. 
5.	The attendance record can be viewed which contains the name of student/teacher with date and time of attendance. 
 
_Register New Student/Teacher_    
The system uses the SQLlite3 database and Python to take a new entry of a student. The students Name, Roll No, Registration Id and Branch is stored in the database and a folder of their name is created. The laptop camera is activated and multiple pictures of the user is taken and stored in the training folder with their name. 
 
_Train Machine using Images _ 
The system has a button to train images. This button allows the machine to use the newly created folder of training images of the new registered student or teacher. It uses the concept of SVM and Haar Cascade models provided through OpenCV and TensorFlow algorithms, to detect the faces and add it to the database. 
  
_Mark attendance _  
This button on the application activates the laptop camera again and searches for a face in the captured video feed. The student’s face is immediately recognized and displayed on the screen alongside the face. On the command prompt, the name of the detected student or teacher is displayed along with the accuracy with which the machine guessed the user. 
  
_Check Attendance_   
This button calls the function to display the Attendance sheet for the current class. The name of the student, their role number, the date and time of logging in are also added alongside the entry in the excel file. It is in the csv form and provides easy access to the attendance at all times. 
 
 
