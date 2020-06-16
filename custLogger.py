#logger
import time

def log(msg,filename=None):
    if filename is None:
        print(msg);
    else:
        with open(filename,'a') as file:
            file.write(time.asctime( time.localtime(time.time()) ) +" : "+msg+"\n")
    