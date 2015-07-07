# -- coding: utf-8 --
import requests
import re
import numpy as np   
from matplotlib import pyplot as plt   
from matplotlib import animation
import random

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111)
axes.set_title('Shangzheng')
axes.set_xlabel('time')
# axes.set_xlim(0, 100)
# axes.set_ylim(2000, 5000)
# axes.set_ylabel('')
line, = axes.plot([], [], linewidth=1.5, linestyle='-')
alldata = []

def dapan(code):
	url = 'http://hq.sinajs.cn/?list='+code
	r = requests.get(url)
	data = r.content[21:-3].decode('gbk').encode('utf8').split(',')
	alldata.append(data[3])
	axes.set_ylim(float(data[5]), float(data[4]))
	# alldata.append(float(data[3])+random.uniform(-50, 50))
	# print alldata
	return alldata

def init():
	line.set_data([], [])
	return line

def animate(i):
	# x = np.linspace(0, 2, 100)
  	# y = np.sin(2 * np.pi * (x - 0.01 * i))  
  	axes.set_xlim(0, i+10)
  	x = range(i+1)
  	y = dapan('sh000001')
  	line.set_data(x, y)
  	print x
  	print y
  	return line

anim=animation.FuncAnimation(fig, animate, init_func=init,  frames=10000, interval=5000)
# dapan('sh000001')

plt.show()