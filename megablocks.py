import os
from PIL import Image
from PIL import ImageStat

pixelSubs = [] #images that can replace solid pixels
pixelSubsA = []#images that can replace transparent pixels
def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGBA'[i], sep='', end=' ')
	print('')
def distSq(a, b):
	c, d = [a[i]-b[i] for i in range(len(a))], 0#vector subt.
	for i in range(len(a)):
		d = d + c[i]**2
	return d #only a closest search
def closest(point, alpha=False):
	if len(point) > 3:
		if point[3] != 255:#is transparent
			alpha = True
	minDist, recordP, recordF = 4000000, 0, '???'
	for p, f in pixelSubs:
		if distSq(p, point) < minDist:
			recordP = p
			recordF = f
			minDist = distSq(p, point)
	if alpha:#then also...
		for p, f in pixelSubsA:
			if distSq(p, point) < minDist:
				recordP = p
				recordF = f
				minDist = distSq(p, point)
	return recordF


srcPack = 'assets'	#where to take block textures
newPack = 'assets2'	#name of new resource pack
imgScl = 16			#size of images accepted

print('Getting files')
imgList = []
packDir = os.path.join(srcPack, 'minecraft', 'textures', 'block')
for path, folders, files in os.walk(packDir):#add all blocks to imgList
	for file in files:
		imgList.append(os.path.join(path, file))

print('Sorting files')
for file in imgList:
	try:
		img = Image.open(file)
	except OSError:#skip .meta
		pass
	else:
		if img.size == (imgScl, imgScl):
			img = img.convert("RGBA")
			avg = ImageStat.Stat(img).mean
			if avg[3] == 255:
				pixelSubs.append((avg, file))
			else:
				pixelSubsA.append((avg, file))

print('Making images')
# imgList = []
if not os.path.isdir(newPack):
	os.mkdir(newPack)
for srcPath, folders, files in os.walk(srcPack):
	path = srcPath.replace(srcPack, newPack, 1)
	if not os.path.isdir(path):
		os.mkdir(path)
	for file in files:
		try:
			srcImg = Image.open(os.path.join(srcPath, file))
		except OSError:#skip .meta
			pass
		else:
			srcImg = srcImg.convert("RGBA")
			pix = srcImg.load()
			srcRes = srcImg.size
			res = [i*imgScl for i in srcRes]
			srcImg = srcImg.resize(tuple(res))#scale by imgScl
			
			for y in range(srcRes[1]):
				for x in range(srcRes[0]):
					replace = Image.open(closest(pix[x, y]))
					srcImg.paste(replace, (x*imgScl, y*imgScl))
			srcImg.save(os.path.join(path, file), 'PNG')
			print('saved', os.path.join(path, file))
input()