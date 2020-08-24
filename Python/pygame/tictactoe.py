import pygame
 
def main():

	pygame.init()

	#Load all images
	background = pygame.image.load("background.jpg")
	backgroundSize=pygame.Surface.get_size(background)
	X = pygame.image.load("X.jpg")
	O = pygame.image.load("O.jpg")

	#Make the table coordinates as an array of Rects
	table =[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
			table[i][j] = pygame.Rect(i*backgroundSize[0]/3,j*backgroundSize[1]/3,backgroundSize[0]/3,backgroundSize[1]/3)
	print(table)

	#Make the window same size as the background image
	screen = pygame.display.set_mode(backgroundSize)
	#Put the background image
	screen.blit(background, (0,0))
	pygame.display.flip()

	# variable for the main loop
	running = True
	# variable for the simbol player
	player = X
    # main loop
	while running:
        # event handling, gets all event from the event queue
		for event in pygame.event.get():
            # only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
				running = False
			# control the click event
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				# depending on where the click was blit the image in the correct position
				for i in range(3):
					for j in range(3):
						if table[i][j].collidepoint(pos):
							screen.blit(player, table[i][j])
							pygame.display.flip()
							# change the player after each click
							if player == X:
								player = O
							else:
								player = X

if __name__=="__main__":
    # call the main function
    main()