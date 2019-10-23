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
		imgList.append(os.path.join(path, file))
print(imgList)

input()
print('Sorting files')
file = imgList[0]
print(file)
'''
for file in imgList:
	try:
		img = Image.open(file)
		st = ImageStat.Stat(img)
		printRGB(st.mean)
	except:
		pass
'''
try:
	img = Image.open(file)
	st = ImageStat.Stat(img)
	printRGB(st.mean)
except:
	pass
#'''
input()