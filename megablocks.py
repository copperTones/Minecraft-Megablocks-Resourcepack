import os
from PIL import Image
from PIL import ImageStat

pixelSubs = {} #images that can replace solid pixels
pixelSubsA = {}#images that can replace transparent pixels
def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGBA'[i], sep='', end=' ')
	print('')
def dist(a, b):
	c, d = [a[i]-b[i] for i in range(len(a))], 0#vector subt.
	for i in range(len(a)):
		d = d + c[i]**2
	return sqrt(d)
def closest(point, alpha=False):
	minDist, recordP = 1024, 0#tuple([0]*4)
	for p, f in pixelSubs.items():
		if dist(p, point) < minDist:
			recordP = p
			minDist = dist(p, point)
	if alpha:
		for p, f in pixelSubsA.items():
			if dist(p, point) < minDist:
				recordP = p
				minDist = dist(p, point)
	return recordP


srcPack = 'assets'	#name of 'recourcepack'
imgScl = 16			#size of images accepted

print('Getting files')
imgList = []
packDir = os.path.join(os.getcwd(), srcPack, 'minecraft', 'textures', 'block')
for path, folders, files in os.walk(packDir):#add all blocks to imgList
	for file in files:
		imgList.append(os.path.join(path, file))

print('Sorting files')
for file in imgList:
	try:
		img = Image.open(file)
		if img.size == (imgScl, imgScl):
			img.convert("RGBA")
			st = ImageStat.Stat(img)
			if st.mean[3] == 255:#all solid
				pixelSubs[tuple(st.mean)] = file
			else:#any transparency
				pixelSubsA[tuple(st.mean)] = file
	except:
		pass

print('Making mosaics')
imgList = []
packDir = os.path.join(os.getcwd(), srcPack)
for path, folders, files in os.walk(packDir):
	#for #create if nonexistent
	for file in files:
		try:
			srcImg = Image.open(os.path.join(path, file))
			res = [imgScl*i for i in list(srcImg.size)]
			# img = Image.new('RGBA', tuple(res))#scale by imgScl
			# img.save(os.path.join(os.getcwd(), 'assets2', file), 'PNG')
			srcImg = srcImg.resize(tuple(res))#scale by imgScl
			srcImg.save(os.path.join(os.getcwd(), 'assets2', file), 'PNG')
			print(srcImg.size, tuple(res))
		except BaseException:
			pass
input()