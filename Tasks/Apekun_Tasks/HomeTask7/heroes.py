import random
import field


class GameObject:
	def __init__(self):
		self._x = 0
		self._y = 0

	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y



class Entity(GameObject):

	def __init__(self, health=0, defence=0, attack=0, name = None):
		super().__init__()
		self._health = health
		self._defence = defence
		self._attack = attack
		self._name = name


	def set_name(self,name):
		self._name = name

	def get_name(self):

		return self._name

	def set_health(self, health):

		if health in range(0,101):
			self._health = health
		else:
			print(" Bad health input")

	def get_health(self):
			return self._health


	def get_attack(self):
		return self._attack

	def set_attack(self, attack):
		self._attack = attack

	def set_defence(self, defence):
		self._defence = defence

	def get_defence(self):
		return self._defence
	
	def move(self,matr):

		matr[self.get_y()][self.get_x()] = "."

		new_disp = random.randint(1, 4)
		if new_disp == 1 :
			if (self.get_x() - 1) > 0 and matr[self.get_y()][self.get_x()-1] != "#":
				self.set_x(self.get_x() - 1)
			else:
				pass
		elif new_disp == 2 :
			if (self.get_x() + 1) < (len(matr[self.get_y()])-1) \
					and matr[self.get_y()][self.get_x() + 1] != "#":
				self.set_x(self.get_x() + 1)
			else:
				pass
		elif new_disp == 3 :
			if (self.get_y() - 1) > 0 \
					and matr[self.get_y() - 1][self.get_x()] != "#":
				self.set_y(self.get_y() - 1)
			else:
				pass
		elif new_disp == 4:
			if (self.get_y() + 1) < len(matr) \
					and matr[self.get_y()+1][self.get_x()] != "#":
				self.set_y(self.get_y() + 1)

		if matr[self.get_y()][self.get_x()] == ".":
			matr[self.get_y()][self.get_x()] = self.get_name()

	
	def set_players_disposition(self, matr):	
		while True:
			self.set_y(random.randint(1, len(matr)-1))
			self.set_x(random.randint(1, len(matr[self.get_y()])-1))
			if matr[self.get_y()][self.get_x()] == "." :
				matr[self.get_y()][self.get_x()] = self.get_name()
				break
			else:
				continue





class Hero(Entity):
	pass

class Monster(Entity):
	pass

