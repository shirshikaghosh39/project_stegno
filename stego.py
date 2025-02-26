import cv2
import os
import string
import random

img = cv2.imread("picture.jpg") 

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

y= int(input("Enter 1 to salt message or press any key: "))
if (y==1):
    def generate_salt(length=5):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    img = cv2.imread("picture.jpg")

    salt = generate_salt()
    salted_msg = salt + msg  

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    n, m, z = 0, 0, 0
    for char in salted_msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  

    cv2.imwrite("encryptedImage.jpg", img)
    print("Message successfully encrypted with salting! \n")
    print("Message is:", salted_msg)
    p = input("To decrypt the image, press 1. Else, press any other key: ")
    if p == "1":
        os.system("start encryptedImage.jpg") 
        message = ""
        n, m, z = 0, 0, 0

        pas = input("Enter passcode for Decryption: ")
        for _ in range(len(salted_msg)):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3 
        if password == pas:
            original_message = message[len(salt):]  
            print("Decryption successful! \n Original message:", original_message)
        else:
            print("Incorrect password! \n Extracted (Salted) Message:", message)
    else:
        print("Exiting...")

else:
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)

    p= int(input("To decrypt the image press 1 else press any other key: "))
    if(p==1):
        os.system("start encryptedImage.jpg")  

        message = ""
        n = 0
        m = 0
        z = 0

        pas = input("Enter passcode for Decryption: ")
        if password == pas:
            for i in range(len(msg)):
                message = message + c[img[n, m, z]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3
            print("Decryption message:", message)
        else:
            print("YOU ARE NOT auth")
    else:
        print("Exiting...")
