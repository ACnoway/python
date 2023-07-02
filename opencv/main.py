import cv2 as cv
from ctypes import windll
import time
import pygame.camera as pycam
# 识别电脑摄像头并打开
print("正在加载，请稍候")
pycam.init()
cams = pycam.list_cameras()
print("请选择要使用的摄像头：")
for x in range(0, len(cams)):
    print(str(x + 1) + '. ' + cams[x])
usecam = int(input()) - 1
cap = cv.VideoCapture(usecam, cv.CAP_DSHOW)
user32 = windll.LoadLibrary('user32.dll')
# 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
face_detect = cv.CascadeClassifier(
    r'./data/haarcascade_frontalface_default.xml')
rteye_detect = cv.CascadeClassifier(r'./data/haarcascade_righteye_2splits.xml')
lteye_detect = cv.CascadeClassifier(r'./data/haarcascade_lefteye_2splits.xml')
hand_detect = cv.CascadeClassifier(r'./data/hand.xml')
st = time.time()
while True:
    time.sleep(0.5)
    if user32.GetForegroundWindow() == 0:
        st = int(time.time()) + 1
        time.sleep(0.5)
        continue
    # 读取视频片段
    flag, frame = cap.read()
    frame = cv.flip(frame, 1)
    if not flag:  # 读完视频后falg返回False
        break
    frame = cv.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
    # 灰度处理
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
    face_zone = face_detect.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=3)
    rteye_zone = rteye_detect.detectMultiScale(gray,
                                               scaleFactor=1.1,
                                               minNeighbors=3)
    lteye_zone = lteye_detect.detectMultiScale(gray,
                                               scaleFactor=1.1,
                                               minNeighbors=3)
    '''
    # print(face_zone)
    # 绘制矩形和圆形检测人脸
    for x, y, w, h in face_zone:
        cv.rectangle(frame,
                     pt1=(x, y),
                     pt2=(x + w, y + h),
                     color=[0, 0, 255],
                     thickness=2)
        cv.circle(frame,
                  center=(x + w // 2, y + h // 2),
                  radius=w // 2,
                  color=[0, 255, 0],
                  thickness=2)
    cv.imshow('video', frame)  # 显示图片
    #'''
    # 设置退出键q 展示频率
    if ord('q') == cv.waitKey(30):
        break
    if len(face_zone) > 0 or len(rteye_zone) > 0 or len(
            lteye_zone) > 0 or user32.GetForegroundWindow() == 0:
        st = int(time.time())
    elif len(face_zone) == 0 and len(rteye_zone) == 0 and len(
            lteye_zone) == 0 and int(
                time.time()) - st >= 3 and user32.GetForegroundWindow() != 0:
        hand_zone = hand_detect.detectMultiScale(gray,
                                                 scaleFactor=1.1,
                                                 minNeighbors=3)
        if len(hand_zone) == 0:
            user32.LockWorkStation()
        else:
            st = int(time.time())

# 释放资源
cv.destroyAllWindows()
cap.release()
