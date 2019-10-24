import os
from PIL import Image
from PIL import ImageStat

def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGB'[i], sep='', end=' ')
	print('\n')


srcPack = 'assets'

print('Getting files')
imgList = []
dir = os.path.join(os.getcwd(), srcPack, 'minecraft', 'textures', 'block')
for path, folders, files in os.walk(dir):#add all blocks to imgList
	for file in files:
		imgList.append(os.path.join(path, file))
print(imgList)

print('Sorting files')
for file in imgList:
	try:
		img = Image.open(file)
		st = ImageStat.Stat(img)
		printRGB(st.mean)
	except:
		pass
input()