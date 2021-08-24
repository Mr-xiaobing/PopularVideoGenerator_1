# 把视频  音频合成
# 使用opencv 把图片统一大小  并且生成视频
import os

import cv2
import moviepy.editor as mp
import random

from pydub import AudioSegment
import time
# 音频视频结合  生成最后的视频
def resultMp4(audioName):
    for root, dirs, files in os.walk("./mp4"):
        mp4List = []
        a = 0
        for i in files:
            mp4List.append(mp.VideoFileClip(root+"/"+i).set_start(a*4).set_pos(("center","top")))
            a=a+1
        resultClip =  mp.CompositeVideoClip(mp4List,size=(1920,1080))
        #resultClip = mp.concatenate_videoclips(mp4List,method="compose")
        videoName = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        audioClip = mp.AudioFileClip("./result/"+audioName+".mp3")
        resultVideo = resultClip.set_audio(audioClip)
        resultVideo.write_videofile("./result/"+videoName+".mp4")


# gif图转MP4
def gifToMp4(name,mp4Name):
    #生成的GIF图视频的长
    clip = mp.VideoFileClip(name)
    clip.write_videofile("tmpVideo.mp4")
    # 统一设置视频为4秒钟
    time = clip.duration
    if time<4:
        number = 4/time
        videoList =[]
        tmpVideo = mp.VideoFileClip("tmpVideo.mp4")
        for i in range(int(number)):
            videoList.append(tmpVideo)
        resultclip = mp.concatenate_videoclips(videoList)
        resultclip.write_videofile(mp4Name)
    else:
        resultClip =clip.subclip(0,4)
        mp.concatenate_videoclips([resultClip]).write_videofile(mp4Name)
    os.remove("tmpVideo.mp4")
# 随机选取GIF图
def gifToVideo(audioName):
    img_root = "./gif/"
    # 获取音频的持续时间
    audio = AudioSegment.from_mp3("./result/"+audioName+".mp3")
    # 4秒显示一个gif图  需要多少张
    imageNum = (int)(audio.duration_seconds / 4)  #每张图片4秒钟
    res = random.sample(range(1, 200), imageNum);
    a=1
    for i in res:
        gifToMp4("./resultNewGif/"+str(i)+".gif","./mp4/"+str(a)+".mp4")
        a=a+1
    resultMp4(audioName)
    a=1
    for i in res:
        os.remove("./mp4/"+str(a)+".mp4")
        a=a+1
