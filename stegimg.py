import os
import pyperclip
from fileselector import selection

def createsi():
	os.system("start cmd")
	pyperclip.copy("steghide --embed -ef data.txt -cf final.jpg  -e none -Z")
def extractdata():
	os.system("start cmd")
	pyperclip.copy("steghide --extract -sf final.jpg -xf fdata.txt")


print("\n1.Select files\n2.Create Stego image \n3.Extract Data")
p=int(input())
if(p==1):
	selection()
elif(p==2):
	createsi()
elif(p==3):
	extractdata()
else:
	print("Incorrect")
