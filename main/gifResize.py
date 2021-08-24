from PIL import Image

# 统一gif图大小
import os
import imageio
from PIL import ImageSequence, Image

# 提取gif逐帧保存并返回帧数
def getIndex(img):
    index = 1
    # 图片为gif时获取帧数index并逐帧压缩
    if img.is_animated == True :
        try:
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert('RGB') # 逐帧转换成RGB
                frame.save("index%d.jpg" % index) # 保存每一帧
                pressImg('index%d.jpg'% index) # 调用压缩图片函数逐帧压缩
                index = index + 1
            return index
        except Exception as e:
            print('Error:' + e)
    # 非gif时帧数index为1
    else:
        return index

# 压缩图片
def pressImg(ImgName):
    img = Image.open(ImgName)
    img = img.resize((900, 900))
    img.save('press-'+ImgName, quality=95) # 此处quality为保存图片质量 取值范围由1(最差)-95(最好)
    return 'OK'

# 合并gif
def mergeGif(indexnum,name):
    images = []
    for i in range(1, indexnum):
        images.append(imageio.imread('press-index%d.jpg' % i))
    imageio.mimsave(name, images)

# 删除中间产生的图片
def removeImg(indexnum):
    for i in range(1,indexnum):
        af = 'press-index' + str(i) + '.jpg'
        bf = 'index' + str(i) + '.jpg'
        if os.path.exists(af):
            os.remove(af)
        if os.path.exists(bf):
            os.remove(bf)

def gifToResize(count):
    for i in range(1, count):
        try:
            gif = Image.open('./gif/'+str(i)+'.gif')  # 读取文件
            indexnum = getIndex(gif)  # 提取每一帧，保存为jpg格式，返回总帧数，此过程会生成许多jpg文件
            mergeGif(indexnum,'./resultNewGif/'+str(i)+'.gif')  # 压缩jpg，合并jpg成gif
            removeImg(indexnum)  # 删除中间jpg文件
        except:
            print("error")

