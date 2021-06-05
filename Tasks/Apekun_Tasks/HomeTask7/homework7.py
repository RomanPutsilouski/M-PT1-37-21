import heroes
import random , array
import field

def game_loop(field):
	print("Hero coordinates:" ,pl1.get_x() , pl1.get_y())
	print("Monster coordinates: ", pl2.get_x(),pl2.get_y())
	while True:
		if ((pl1.get_y() - pl2.get_y() == 1) and (pl1.get_x() == pl2.get_x()) or
				(pl2.get_y() - pl1.get_y() == 1) and (pl1.get_x() == pl2.get_x())) \
				or ((pl1.get_x() - pl2.get_x() == 1) and (pl1.get_y() == pl2.get_y())
					 or ((pl2.get_x() - pl1.get_x() == 1)) and (pl1.get_y() == pl2.get_y())):
			print("lets fight!")
			break

		else:
			pl1.move(my_field.get_matrix())
			pl2.move(my_field.get_matrix())
			print("Hero coordinates:", pl1.get_x(), pl1.get_y())
			print("Monster coordinates: ", pl2.get_x(), pl2.get_y())
			my_field.print_matrix()

	
def fight():
	while pl1.get_health() or pl2.get_health() <= 0:
		pl1_rand_cube = random.randint(0, 6)
		pl2_rand_cube = random.randint(0, 6)
		print(f"{pl1.get_name()} score {pl1_rand_cube}, {pl2.get_name()} score {pl2_rand_cube}")
		pl1.set_attack(random.randint(0, 5))
		pl2.set_attack(random.randint(0, 5))
		if pl1_rand_cube > pl2_rand_cube:
			print(f"{pl1.get_name()} attacks {pl1.get_attack()} points")
			if (pl1.get_attack()-pl2.get_defence()) > 0:
				pl2.set_health(pl2.get_health() - (pl1.get_attack()-pl2.get_defence()))
				print(f"{pl2.get_name()}health: ")
			else:
				print(f"missed {pl1.get_name()}")
		elif pl1_rand_cube < pl2_rand_cube:
			print(f"{pl2.get_name()} attacks {pl2.get_attack()} points")
			if (pl2.get_attack()-pl1.get_defence()) > 0:
				pl1.set_health(pl1.get_health() - (pl2.get_attack()-pl1.get_defence()))
				print(f"{pl1.get_name()} health: {pl1.get_health()}")
			else:
				print(f"missed {pl2.get_name()}")
		else:
			continue
		if pl1.get_health() <= 0:
			print(f'{pl2.get_name()} wins')
			break
		elif pl2.get_health() <= 0:
			print(f'{pl2.get_name()} wins')
			break

if __name__ == '__main__':
	my_field = field.Field(20, 10)
	my_field.set_matrix()
	my_field.make_cave()

	pl1 = heroes.Hero(20, 1, 0, "H")
	pl2 = heroes.Monster(20, 1, 0, "M")

	pl1.set_players_disposition(my_field.get_matrix())
	pl2.set_players_disposition(my_field.get_matrix())

	game_loop(my_field.get_matrix())
	fight()