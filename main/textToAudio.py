# 文字转为音频
# 生成文章
from aip import AipSpeech
import os
import requests
import time
from pydub import AudioSegment
APP_ID = '24709957'  #百度API对应的参数
API_KEY = 'YGZOl0PBbPkunmspPnG85LMy'
SECRET_KEY = 'SwpxnZZG5U3GPwsGGlYc0BQKnERMhDim'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# AudioSegment.ffmpeg = "C:\Users\XBin\Desktop\ffmpeg\ffmpeg.exe"
# AudioSegment.ffprobe="C:\Users\XBin\Desktop\ffmpeg\ffprobe.exe"

# 把文字 转换成 音频
def getTextAudio(textData,name):
    result = client.synthesis(textData, 'zh', 1, {'vol': 9, 'spd': 5, 'pit': 5, 'per': '5003'})  # 大约只支持2000个字  所有对data进行拆分
    print(textData)
    if not isinstance(result, dict):
        with open(name, 'wb') as f:
            f.write(result)

def textToMp3Audio():
    mp3list = [] #后面把音频连接起来需要用
    contextList = []
    # 视频长度要控制在8分钟  太长没人看，太短钱收不够
    #文章开头  开头要吸引人
    textHead = open('book/head.txt', 'r', encoding='UTF-8')
    headData = textHead.read();
    getTextAudio(headData,"./mp3/head.mp3")
    #音频混合
    headAudio=  AudioSegment.from_mp3("./mp3/head.mp3")
    headBgm = AudioSegment.from_mp3("./bgm/head.mp3")
    headBgm =  headBgm.apply_gain(-7)
    output =  headAudio.overlay(headBgm)
    output.export("./result/outputHead.mp3",format="mp3")
    mp3list.append("./result/outputHead.mp3")
    #文章主题  瞎扯蛋
    text = open('book/book.txt', 'r', encoding='UTF-8')
    data =text.read()
    length = len(data)
    number = length//2000
    if number>0:
        for i in range(0,number):
            tmpData=data[(2000*i):((i+1)*2000)]
            getTextAudio(tmpData,"./mp3/audio"+str(i)+".mp3")
            contextList.append("./mp3/audio"+str(i)+".mp3")
        tmpData=data[number*2000:]
        getTextAudio(tmpData,"./mp3/audio"+str(number)+".mp3")
        contextList.append("./mp3/audio" + str(i)+".mp3")
    else:
        getTextAudio(data,"./mp3/audio"+str(number)+".mp3")
        contextList.append("./mp3/audio"+str(number)+".mp3")
    # 音频组合起来
    allAudioContext = None
    for tmp in contextList:
        if allAudioContext == None:
            allAudioContext = AudioSegment.from_mp3(tmp)
        else:
            allAudioContext += AudioSegment.from_mp3(tmp)
    allAudioContext.export("./mp3/context.mp3", format="mp3")
    # 音频合成
    contextAudio = AudioSegment.from_mp3("./mp3/context.mp3")
    contextBgm = AudioSegment.from_mp3("./bgm/context.mp3")
    output = contextAudio.overlay(contextBgm)
    output.export("./result/outputContext.mp3", format="mp3")
    mp3list.append("./result/outputContext.mp3")
    #文章结尾  结尾要升华主题  那里大往那里套
    textEnd = textHead = open('book/end.txt', 'r', encoding='UTF-8')
    endData = textEnd.read()
    getTextAudio(endData,"./mp3/end.mp3")
    #音频合成
    endAudio = AudioSegment.from_mp3("./mp3/end.mp3")
    endBgm = AudioSegment.from_mp3("./bgm/end.mp3")
    output = endAudio.overlay(endBgm)
    output.export("./result/outputEnd.mp3", format="mp3")
    mp3list.append("./result/outputEnd.mp3")

    allAudio =None
    for tmp in mp3list:
        print(tmp)
        if allAudio == None:
            allAudio = AudioSegment.from_mp3(tmp)
        else:
            allAudio += AudioSegment.from_mp3(tmp)
    audioName = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    allAudio.export("./result/"+audioName+".mp3", format="mp3")

    return audioName
    #到此文本的内容完成了
if __name__ == '__main__':
    textToMp3Audio()