#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
import time
# from tkinter import filedialog
# from tkinter import *

print('Please input token')
token = input()

def _lineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+token}
    r = requests.post(url, headers=headers , data = payload, files=file)
    print (r.text)

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': ' '}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)
while True:
    print("Menu \n1.Message \n2.Img \n3.Sticker \n4.loop message \n5.Exit")
    print("Please input number")
    menu = input()
    while True:
        if(menu == '1'):
            print('input message:'),
            lineNotify(input())
            break
        elif(menu == '2'):
            # root = Tk()
            # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            # print (root.filename)
            # notifyFile(root.filename)
            # root.destroy()
            break
        elif(menu == '3'):
            print("input ID sitcker")
            stickerID = input()
            print("input sticker PackageID")
            stickerPackageID = input()
            notifySticker(stickerID,stickerPackageID)
            break
        elif(menu == '4'):
            print('input message:'),
            text = input()
            print('input Loop'),
            for x in range(int(input())):
                lineNotify(text)
            break
        elif(menu == '5'):
            print("ลาก่อนไอ้เด็กเหี้ย")
            exit()
        else:
            print("Please input number")
            menu = input()