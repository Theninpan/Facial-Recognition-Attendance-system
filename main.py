import StudentAttendance
import sys

if(len(sys.argv) != 3 ):
    print("Argument Error.")
    print("""use python 0 IN/OUT
    where 0 is the camera index
    IN/OUT is the camera in which it is placed.""")
    quit(0)

if sys.argv[1].isdigit(): 
    camera_index = int(sys.argv[1])
else:
    camera_index = sys.argv[1]
type_IO = str(sys.argv[2])


image_source = 'Images/'
user_path = 'Data/student_list.txt'
reference = "Data/reference.yml"

sql_ip = "localhost"  #localhost
sql_user = "root"
sql_password = "theniusr"
sql_database = "Attendance"

obj = StudentAttendance.Recognise(image_source, user_path, reference,camera_index,type_IO)
obj.connect(sql_ip,sql_user,sql_password,sql_database)

while(1):
    opt = input("\n1.Enroll New Student to class\n2.Track & Mark Attendance \n3.Exit\nEnter your option:")
    if(opt == '1'):
        obj.enroll()
    if(opt == '2'):
        obj.run()
    if(opt == '3' or opt == 'e'):
        quit(0)
