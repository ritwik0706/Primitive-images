from Population import Population
import numpy as np
import random
import cv2
import time

original_image = np.random.randint(0, 256, (256, 256, 3) , dtype = np.uint8)
tp = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]
original_image[:] = tp
#original_image = cv2.imread("monalisa.jpg")
resized_image = cv2.resize(original_image, (256, 256))
pop_max = 300
mut_rate = 0.1
size = 16
generated_image = np.zeros(resized_image.shape, dtype = np.uint8)


cv2.imwrite("D:\\Programming\\Projects\\GA\\Primitive Images\\Best\\New Folder\\original.jpg", original_image)

if __name__ == "__main__":
	
	""" The target for the population is a 16x16 (size*size) pixel of the resized image"""
	for i in range(0, 257, size):
		if i+2 <= 256 :
			for j in range(0, 257, size):
				if j+2 <= 256 :
					target = resized_image[i:i+size, j:j+size]
					pop = Population(target, mut_rate, pop_max)
					now = time.time()
					for t in range(50):
						pop.natural_selection()
						pop.generate()
						pop.calc_fitness()
						print(pop.get_average_fitness())
						best = pop.get_best()
						
						"""Finally a 5x5 median filter is appplied on the best generated pixel"""
						median = cv2.medianBlur(best, 5)
						
						"""Apply the max occuring pixel value to all pixels
						temp = best.flatten()
						counts = np.bincount(temp)
						x = np.argmax(counts)"""
						
					generated_image[i:i+size, j:j+size] = median
					outpath = "D:\\Programming\\Projects\\GA\\Primitive Images\\Best\\New Folder\\gen" + str(i) + str(j) + ".jpg"
					cv2.imwrite(outpath, generated_image)
					"""print(f"time elapsed: {time.time() - now}")
					now = time.time()"""