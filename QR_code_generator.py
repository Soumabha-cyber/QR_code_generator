# we need a library called pyqrcode
# we pass a text and then it will get converted to a qr code
# we need to install pypng and import it

import pyqrcode  #import package
import png

def qrcode():  #making a method
    q=pyqrcode.create(input()) #will take input text
    q.png('qr_code.png', scale=8)  #the png will be of size 8*8 and name of png will be :-
    print('QR generated')    #after the png is generated this will be printed

if __name__=='__main__':  #main method that will call the function
    qrcode()
