import pyautogui as pg

while True:
	x, y = pg.position()
	temp = x, y
	if temp != pg.position:
		print(x, y)