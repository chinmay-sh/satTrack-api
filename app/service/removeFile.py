import os

def remFile(fileName):
    if os.path.exists("../../" + fileName +".txt"):
        os.remove("../../" + fileName +".txt")
    else:
        print("The file does not exist") 


def remCall():
    files = ["visual","active","starlink","stations"]
    for i in files:
        remFile(i)