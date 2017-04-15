from PIL import Image
import numpy as np
import random

input_image = Image.open('image.jpg').convert('L')
pixel_array = np.array(input_image)

def bound(input_value, minimum, maximum):
	if input_value > maximum:
		return maximum
	elif input_value < minimum:
		return minimum
	else: return input_value


def  kernalMap(kernal, pixels, brightness = 1):
	output = np.zeros(shape=(len(pixels)-len(kernal)+1,len(pixels[0])-len(kernal[0])+1))
	
	for y in range(len(pixels)-len(kernal)+1):
		for x in range(len(pixels[0])-len(kernal[0])+1):
			kernalAverage = 0
			for ky in range(len(kernal)):
				for kx in range(len(kernal[0])):
					kernalAverage += pixels[y-1+ky][x-1+kx]*kernal[ky][kx]*brightness
				
			kernalAverage /= len(kernal[0])*len(kernal)
			output[y][x] = kernalAverage
	
	return output


def edgeDetect(pixels):
	kernal = [[-1, 0, 1],
			  [-2, 0, 2],
			  [-1, 0, 1]]
	horizontalOutput = kernalMap(kernal, pixels)
	kernal = [[1 , 2 , 1 ],
			  [0 , 0 , 0 ],
			  [-1, -2, -1]]
	verticalOutput = kernalMap(kernal, pixels)
	
	output = np.zeros(shape=(len(pixels)-2,len(pixels[0])-2))

	
	for y in range(len(pixels)-2):
		for x in range(len(pixels[0])-2):
			output[y][x] = bound(abs(verticalOutput[y][x] + horizontalOutput[y][x]), 0, 255)
	
	return output
	
	
def blur(pixels, size = 3):
	kernal = [];
	for y in range(size):
		kernal.append([])
		for x in range(size):
			kernal[y].append(1)
	
	return kernalMap(kernal, pixels)

def gaussianBlur(pixels):
	kernal = [[1.5, 3, 1.5],
			  [3  , 6,   3],
			  [1.5, 3, 1.5]]
	return kernalMap(kernal, pixels)

pixel_array = gaussianBlur(pixel_array)
pixel_array = edgeDetect(pixel_array)

im = Image.fromarray(pixel_array.astype('uint8')).convert('L')
im.save('output2.png')