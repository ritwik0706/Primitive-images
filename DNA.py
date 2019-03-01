import random
import numpy as np
#import decimal


class DNA:    
	def __init__(self, shape):
		"""Genes contain a random image of the shape passed in the constructor"""
		self.genes = np.random.randint(0, 256, shape , dtype = np.uint8)
		
		"""For genes to have a particular colour we assign all the pixel the same values
		tp = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]
		self.genes[:] = tp"""
		
		self.fitness = 0
    
	def get_image(self):        
		return self.genes
    
	def compute_fitness(self, target):		
		""" Fitness Criteria Based On Euclidean Distance"""
		dif_sq = np.square(target - self.genes, dtype = np.int64)
		score = np.sum(dif_sq)
		
		""" Fitness criteria based on similarity of pixel values
		similar = target == self.genes
		score = np.sum(similar)"""
        
		self.fitness = score / target.size
    
	def crossover(self, partner):
		child = DNA(self.genes.shape)
		mid = random.randint(1, self.genes.shape[0] * self.genes.shape[1] * self.genes.shape[2] - 1)
		
		""" Convert the self and partner genes into a 1D array"""
		temp1 = self.genes.flatten()
		temp2 = partner.genes.flatten()
		
		""" Convert back the 1D array obtained after crossover from mid into 2D array"""
		gene = np.hstack((temp1[:mid], temp2[mid:]))
		child.genes = gene.reshape(self.genes.shape)
		
		"""mid = random.randint(1, self.genes.shape[0])
		child.genes[0:mid] = self.genes[:mid]
		child.genes[mid:] = partner.genes[mid:]"""

		return child
    
	def mutate(self, mut_rate):
		
		"""Mutation using boolean indexing"""
		is_mutate = np.random.randint(0, 2, size=self.genes.shape[:2], dtype=np.bool) < mut_rate
		sh = self.genes[is_mutate].shape
		self.genes[is_mutate] = np.random.randint(0, 256, size=sh, dtype=np.uint8)
		
		""" Mutation using brute force
		for i in range(0, len(self.genes)):
			   for j in range(0, len(self.genes[0])):
				   created_ran_num = np.random.rand()
				   
				   if created_ran_num < mut_rate:
					   tp = np.random.randint(0, 256, (self.genes.shape[1], self.genes.shape[2]) , dtype = np.uint8)
					   #tp[:] = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]
					   self.genes[:i] = self.genes[0:i,:,:]
					   self.genes[i] = tp
					   self.genes[i+1:] = self.genes[i+1:,:,:]"""
					   