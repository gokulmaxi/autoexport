import os
import getpass
import sys
import time
user=getpass.getuser()
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 

def checkfile(search_word):
    with open("/home/{}/.bashrc".format(user),'r+') as file:
        contents = file.read()
        if search_word in contents:
            return True
        else:
            return False
def append(apath):
    file_object = open("/home/{}/.bashrc".format(user),'a')
    export='export PATH=$PATH:{}'.format(apath)
    file_object.write(export)
    print(dir)
pat=input("enter the path you want to export:")
if(checkfile(pat)):
    print("your file is already exported")
else:
    print("preparing to export your path")
    time.sleep(2)
    append(pat)

