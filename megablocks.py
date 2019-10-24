import os
from PIL import Image
from PIL import ImageStat

def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGBA'[i], sep='', end=' ')
	print('')


srcPack = 'assets'	#name of 'recourcepack'
imgSize = 16		#size of images accepted

print('Getting files')
imgList = []
dir = os.path.join(os.getcwd(), srcPack, 'minecraft', 'textures', 'block')
for path, folders, files in os.walk(dir):#add all blocks to imgList
	for file in files:
		imgList.append(os.path.join(path, file))

print('Sorting files')
pixelSubs = {}#images that can replace solid pixels
pixelSubsA = {}#images that can replace transparent pixels
for file in imgList:
	try:
		img = Image.open(file)
		if img.size == (imgSize, imgSize):
			img.convert("RGBA")
			st = ImageStat.Stat(img)
			printRGB(st.mean)
			if st.mean[3] == 255:#all solid
				r, g, b, a = st.mean
				pixelSubs[(r, g, b)] = file
			else:#any transparency
				pixelSubs[st.mean] = file
	except:
		pass
input()
print(pixelSubs)
input()
print(pixelSubsA)
input()