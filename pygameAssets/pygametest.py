import sys
import pygame
import pyautogui as pg
from random import randint as rn

pygame.init()

size = width, height = 1920, 1080
black = 0, 0, 0
screen = pygame.display.set_mode(size=size)
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# gets position of mouse and stores x and y coordinates in x, y
	x, y = pg.position()
	if (x, y) != pg.position():
		# Fills screen with black so next frame can be drawn
		# (without this we would have a brush trailing effect)
		#screen.fill(black)

		# sets cursor visibility	
		pygame.mouse.set_visible(False)
		for i in range(54):
			pygame.draw.lines(screen, (255, 255, 255), closed=False, points=[[0, i*20], [width, i*20]])
		# draws a circle at location x, y
		pygame.draw.circle(screen, [240, 95, 123], [x, y], 30, width=2)
		
		pygame.display.update()
