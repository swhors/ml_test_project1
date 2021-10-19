import os
import subprocess
file = open('hello.py')
for line in file:
    if 'Sequential' in line:
        print('sequential')
        os.system("sudo cp /Email/newmail.py /ajproject")
        os.system("sudo docker run -it -v /ajproject:/root --name myrpd anantj1/rcnn:v1")
        os.system("sudo docker exec -d -w /root myrpd -c 'python3 newmail.py'")
        #subprocess.Popen("hello.py 1", shell=True)
        #subprocess.Popen("newmail.py 1",shell=True)
        break
    elif 'Regression' in line:
        print('Regression yol')
        break

