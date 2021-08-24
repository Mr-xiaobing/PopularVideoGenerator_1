from main.textToAudio import textToMp3Audio
from main.generateVideo import gifToVideo
from main.gifResize import gifToResize
from main.reptileGIF import getGIF


# 文本内容 请写在 book文件夹
#  bgm在bgm文件夹
#  gif图爬取放在 gif图文件夹
# 统一大小后会放在resultNewGif文件夹
# 生成的音频片段在 mp3文件夹。结果在 result文件夹
# 视频直接生成在result文件夹 包括gif图内容，内容音频，BGM
# genrateText直接生成小文章的AI没有做。大家有兴趣可以来写一下。
if __name__ == '__main__':
    # 可以调一下位置，先生成音频，然后根据音频的长度去爬取gif图也可以（而且是一种更好的选择）
    # 获取gif图
    count =getGIF() #如果已经获取到了Gif图则不需要重新下载了。
    # 统一大小  gifToResize () gif统一大小  默认 900*900  具体尺寸可以在视频内部修改
    gifToResize(count)  #如果已经统一格式则不需要再运行了。
    # 生成音频  并且是合成好的（包括前中后）
    audioName = textToMp3Audio()
    # 有了gif图开始生成视频 已经和音频进行和合并
    gifToVideo(audioName)