import os
from PIL import Image
from PIL import ImageStat

def printRGB(rgb):
	for i, c in enumerate(rgb):
		print(f'{c:.0f}', 'RGB'[i], sep='', end=' ')
	print('\n')

for path, folders, files in os.walk(os.getcwd()):
	print(path, folders, files)
input()