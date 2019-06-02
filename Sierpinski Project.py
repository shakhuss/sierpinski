#Shakeb H.
#Project 1
#10/10/18

import numpy as np
import random
from matplotlib import pyplot as plt

class die:
	def roll(self):
   		return random.randint(1,6)



class Sierpinski(object):

	def __init__(self, vertex, nofi, currentx, currenty):
		self.vertex = vertex
		self.nofi = nofi
		self.currentx = currentx
		self.currenty = currenty
		self.d = die()
		self.px = []
		self.py = []


	def generate_data(self):
		vectorpoint = [self.currentx, self.currenty]
		dice = self.d

		for i in range(self.nofi):

			roll = dice.roll()

			if roll == 1 or roll == 2:
				newp = self.vertex[0]
				x = ((newp[0]+vectorpoint[0])/ 2);
				y = ((newp[1]+vectorpoint[1])/ 2);
				#mids = midp(vectorpoint, newp)
				vectorpoint[0] = x
				vectorpoint[1] = y
				self.px.append(x)
				self.py.append(y)

			elif roll == 3 or roll == 4:
				newp = self.vertex[1]
				x = ((newp[0]+vectorpoint[0])/ 2);
				y = ((newp[1]+vectorpoint[1])/ 2);
				#mids = midp(vectorpoint, newp)
				vectorpoint[0] = x
				vectorpoint[1] = y
				self.px.append(x)
				self.py.append(y)

			else:
				newp = self.vertex[2]
				x = ((newp[0]+vectorpoint[0])/ 2);
				y = ((newp[1]+vectorpoint[1])/ 2);
				#mids = midp(vectorpoint, newp)
				vectorpoint[0] = x
				vectorpoint[1] = y
				self.px.append(x)
				self.py.append(y)



	def plot_data(self):
		plt.scatter(self.px, self.py)
		plt.show()


def main():
	#S = Sierpinski([[P1x,P1y],[P2x,P2y],[P3x,P3y]], number_of_iterations, current_pos_x, current_pos_y)
	S = Sierpinski([[0,0],[20,20],[40,0]], 1000, 1, 1)
	S.generate_data()
	S.plot_data()


	

main()