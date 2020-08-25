import pygame
 
def main():

	pygame.init()

	# variable for the play cont
	play = 0
	#Load all images
	background = pygame.image.load("background.jpg")
	backgroundSize = pygame.Surface.get_size(background)
	X = pygame.image.load("X.png")
	XSize = pygame.Surface.get_size(X)
	O = pygame.image.load("O.png")
	OSize = pygame.Surface.get_size(O)

	#Make the table coordinates as an array of Rects
	table =[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
			table[i][j] = pygame.Rect((i*backgroundSize[0]/3)+5,(j*backgroundSize[1]/3)+5,(backgroundSize[0]/3)-5,(backgroundSize[1]/3)-5)

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
			if event.type == pygame.MOUSEBUTTONUP and play < 9:
				pos = pygame.mouse.get_pos()
				# depending on where the click was blit the image in the correct position
				for i in range(3):
					for j in range(3):
						if table[i][j].collidepoint(pos):
							play+=1
							screen.blit(player, table[i][j])
							pygame.display.flip()
							# eliminate the coordinate where the X or O has been blited
							table[i][j] = pygame.Rect(0,0,0,0)
							# change the player after each click
							if player == X:
								player = O
							else:
								player = X

if __name__=="__main__":
    # call the main function
    main()