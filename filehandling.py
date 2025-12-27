with open("file.py","w") as f:
    f.write("********** Your Daily Work **********\nPlease follow the tasks listed below.\n************************************\n")
    f.close()
try:
    c=open("file.py","r")
    print(c.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("execution ended")