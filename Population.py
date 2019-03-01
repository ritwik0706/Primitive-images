from DNA import DNA
from random import randint
import numpy as np


class Population:
	def __init__(self, target, mut_rate, pop_max):        
		self.target = target     
		self.mut_rate = mut_rate       	         
		self.pop_max = pop_max
		self.population = []
		self.pop_fitness = []   
		self.mating_pool = []    
		self.generations = 0
		
		for i in range(0, pop_max):
		  self.population.append(DNA(target.shape))
		    
		self.calc_fitness()

    
	def calc_fitness(self):        
		for i in range(0, len(self.population)):
			self.population[i].compute_fitness(self.target)
    
	def natural_selection(self):        
		#self.mating_pool.clear()
		self.pop_fitness.clear()
		
		for i in range(0, len(self.population)):
			self.pop_fitness.append(self.population[i].fitness)
		
		"""Create a probabilty array that contains probabilty of every gene for selection during reproduction"""
		tot = np.sum(self.pop_fitness)
		prob = np.divide(self.pop_fitness, tot)
		
		""" Mating pool array is created that contains genes that are choosed on the basis of their probablities""" 
		self.mating_pool = np.random.choice(self.population, len(self.pop_fitness), p = prob)
		
		"""for i in range(0, len(self.population)):            
			fitness = int(self.population[i].fitness * 100)            
			for j in range(0, fitness):                
				self.mating_pool.append(self.population[i])"""
    
	def generate(self):        
		for i in range(0, len(self.population)):            
			a = randint(0, len(self.mating_pool)-1)            
			b = randint(0, len(self.mating_pool)-1)            
			partner_a = self.mating_pool[a]            
			partner_b = self.mating_pool[b]            
			child = partner_a.crossover(partner_b)            
			child.mutate(self.mut_rate)            
			self.population[i] = child
        
		self.generations += 1
    
	def get_best(self):    
		max_fit = 0
		index = 0
        
		for i in range(0, len(self.population)):            
			if self.population[i].fitness > max_fit:                
				index = i                
				max_fit = self.population[i].fitness
				      
		return self.population[index].get_image()
    
	def get_num_of_generations(self):		   		 
		return self.generations
    
	def get_average_fitness(self):       
		total = np.sum(self.pop_fitness)
        
		return total / len(self.population)