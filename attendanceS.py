
import sqlite3
import csv
import datetime
import time

def data(name1,time):
    
    with open('new4.csv','w') as f:
        fieldname = ['Teacher_name','Time']
        field = [{'Teacher_name':name1,'Time':time}]
        csv_writer = csv.DictWriter(f,fieldname)
        
        csv_writer.writeheader()
        csv_writer.writerows(field)

def append1(rollno,name):
    with open('new4.csv','a') as f1:
        fieldname1 = ['RollNo','Name','Attendance','Date','Time']
        writer = csv.DictWriter(f1,fieldname1)
        writer.writeheader()
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        for r,n in zip(rollno,name):
            writer.writerows([{'RollNo':r,
                              'Name':n,
                              'Attendance':'Present',
                              'Date':date,
                              'Time':timeStamp}])
def DB(present):
    
    conn = sqlite3.connect('FaceRec.db')
    cursor = conn.cursor()
    time = '9:15-10:15'
    cursor.execute('SELECT "'+time+'" FROM TimeTable where Days="Monday"')
    for row1 in cursor.fetchall():
        a = row1[0]
        data(a,time)
        
    cursor.execute('SELECT RollNo,FirstName FROM StudentRec')
    rollno = []
    for row in cursor.fetchall():
        for p in present:
            if row[1] == p:   
                rollno.append(row[0])
    append1(rollno,present)
            
     

if __name__ == "__main__":
    DB(present)
