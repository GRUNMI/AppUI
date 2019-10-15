# coding:utf-8
__author__ = 'GRUNMI'


# a = "//android.widget.TextView[@resource-id='com.seuic.kysy:id/tv_sel_destination' and @text='{}']".format("西安长安点部")
# print(a)
#
# b = "ww搜索"
# if "搜" in b:
#     print(111)
# else:
#     print(222)


# def a(ww):
#     for s in str(ww).strip():
#         for i in s:
#             print(i, type(i))
# a(12121)


# b = [('020CH',)]
#
# for i in b[0]:
#     print(i)

# import threading
# print([x for x in range(9)])
# thread = threading.current_thread()
# thread.setName('主线程mmm')
# print('线程名称：' , thread.getName())
# print('正在运行的线程：',threading.enumerate())
# print('正在运行的线程个数：',threading.activeCount())

# import threading
# import time
# import random
# start_time =time.time()
# def do_something():
#     print ("{thread_name} start at {now}\n".format(thread_name=threading.currentThread().name,now=time.time()) )
#     time.sleep(1)
#     print ("{thread_name} stop at {now}".format(thread_name=threading.currentThread().name,now=time.time()) )
# if __name__== "__main__":
#     threads = []
#     # start all threading.
#     for i in range(1,8):
#         t = threading.Thread(target=do_something)
#         t.start()
#         threads.append(t)
#     # #wait until all the threads terminnates.
#     for thread in threads:
#         thread.join()
#     print ("all threads deid." )
#     print ("this run take {t} seconds".format(t = (time.time()-start_time)))

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt  #绘制图像的模块
# import  jieba                    #jieba分词
#
#
# path_txt='C:/Users/Administrator/Desktop/all.txt'
# f = open(path_txt,'r').read()
#
# # 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
# cut_text = " ".join(jieba.cut(f))
#
# wordcloud = WordCloud(
#    #设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
#    font_path="C:/Windows/Fonts/simfang.ttf",
#    #设置了背景，宽高
#    background_color="white",width=1000,height=880).generate(cut_text)
#
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()


from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba
def GetWordCloud():
   path_txt = 'C://Users/Administrator/Desktop/all.txt'
   path_img = "C://Users/Administrator/Desktop/jing.jpg"
   f = open(path_txt, 'r').read()
   background_image = np.array(Image.open(path_img))
   # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云,感兴趣的朋友可以去查一下，有多种分词模式
   #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
   cut_text = " ".join(jieba.cut(f))

   wordcloud = WordCloud(
       # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
       font_path="C:\Windows\Fonts\FZSTK.TTF",
       background_color="white",
       # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
       mask=background_image).generate(cut_text)
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()

if __name__ == '__main__':
   GetWordCloud()






