import random

class Field:

	def __init__(self, width, heigth):
		self.row = width
		self.col = heigth
		self._matrix = []
		self._x = int(self.row / 2)
		self._y = int(self.col / 4)

	def set_matrix(self):
		for x in range(self.col):
			self._matrix.append([])
			for y in range(self.row):
					self._matrix[x].append("#")

	def get_matrix(self):
		return self._matrix

	def make_cave(self, n = 25):

		for j in range(n):
			while True:
				new_disp = random.randint(1, 4)
				if new_disp == 1 :
					self._x -= 1
				elif new_disp == 2 :
					self._x += 1
				elif new_disp == 3 :
					self._y += 1
				elif new_disp == 4  :
					self._y -= 1
				if self._y >= self.col :
					y = 1
				elif self._x >= self.row:
					self._x-= self.row
				if self._matrix[self._y][self._x] != ".":
					self._matrix[self._y][self._x] = "."
					break
		return self._matrix

	def print_matrix(self):
		for i in range(len(self._matrix)):
			print("".join(self._matrix[i]))




