import os,time,traceback


def checkFile():
    files = os.listdir()

    if "quicksave.txt" not in files:
        print("save not in files")


def reName():
    os.rename("FileToRename.txt","renamedFile.csv")


def idk():
    filename = os.path.join("DirFolder/","dirFilename")

    f = open(filename, "w")
    f.write("hi")
    f.close()

                            
