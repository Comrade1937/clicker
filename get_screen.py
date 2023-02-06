import cv2 as cv 
import numpy as np
import win32gui, win32ui, win32con

def get_vic_screen():
    hwnd = win32gui.FindWindow(None, "Victoria 2")
    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0] 
    height = rect[3] - rect[1] 
    hwndc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwndc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (rect[0], rect[1]), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    #img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)
    #print(width,height)
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndc)
    win32gui.DeleteObject(bmp.GetHandle())
    img = cv.cvtColor(img, cv.COLOR_BGRA2BGR) 
    dtc = [120,100,380,170] # data to crop x1,y1,x2,y2 
    img = img[dtc[1]:dtc[3],dtc[0]:dtc[2]]  # speed factor x10-x30 compared to full screen
    return rect,img 

