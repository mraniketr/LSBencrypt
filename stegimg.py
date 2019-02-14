import os
import webbrowser			

def createsi():
	os.system("steghide --embed -ef data.txt -cf final.jpg  -e none -Z")
def extractdata():	
	os.system("steghide --extract -sf final.jpg -xf fdata.txt")


print("\n1. Create Stego image \n2.Extract Data \n 3. Install Stego") 
p=int(input())
if(p==1):
    createsi()
elif(p==2):
    extractdata()
else:
	webbrowser.open("http://steghide.sourceforge.net/download.php")
