import os
from PIL import Image
from PIL import ImageStat

def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGB'[i], sep='', end=' ')
	print('\n')


print('Getting files')
imgList = []
for path, folders, files in os.walk(os.getcwd()):#add all files to imgList
	for file in files:
		imgList.append(file + path)
print(imgList)
#print('Sorting files')
#for file in imgList:
input()