import pygame
 
def main():

	pygame.init()

	# variable for the play cont
	play = 1
	#Load all images
	background = pygame.image.load("background.jpg")
	background = pygame.transform.scale(background,(300,300))
	backgroundSize = pygame.Surface.get_size(background)

	X = pygame.image.load("X.png")
	X = pygame.transform.scale(X,(80,80))
	XSize = pygame.Surface.get_size(X)

	O = pygame.image.load("O.png")
	O = pygame.transform.scale(O,(80,80))
	OSize = pygame.Surface.get_size(O)

	#Make the table of simbols empty
	table =[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

	#Make the table coordinates as an array of Rects
	coord =[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
			coord[i][j] = pygame.Rect(((int)(i*backgroundSize[0]/3))+10, 
				((int)(j*backgroundSize[1]/3))+10, 
				(int)(backgroundSize[0]/3), 
				(int)(backgroundSize[1]/3))

	#Make the window same size as the background image
	screen = pygame.display.set_mode((backgroundSize[0],backgroundSize[1]))
	#Put the background image
	screen.blit(background, (0,0))
	pygame.display.flip()

	# variable for the main loop
	running = True
	# variable for the simbol player
	player = X
	message = None
	winner = None
    # main loop
	while running:
        # event handling, gets all event from the event queue
		for event in pygame.event.get():
            # only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
				running = False
			# control the click event
			if event.type == pygame.MOUSEBUTTONUP and play < 10:
				pos = pygame.mouse.get_pos()
				# depending on where the click was, blit the image in the correct position
				for i in range(3):
					for j in range(3):
						if coord[i][j].collidepoint(pos) and table[i][j] < 0:
							play+=1
							screen.blit(player, coord[i][j])
							pygame.display.flip()
							# change the player after each click and put the simbol in the table
							if player == X:
								table[i][j] = 1
								player = O
							else:
								table[i][j] = 0
								player = X
				# check if there is a winner
				if play > 5:
					for i in range(3):
						if table[i][i] >= 0:
							if i == 0 and table[i+1][i] == table[i][i] and table[i+2][i] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							if i == 0 and table[i][i+1] == table[i][i] and table[i][i+2] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							if i == 0 and table[i+1][i+1] == table[i][i] and table[i+2][i+2] == table[i][i]:
								play = 10
								winner = table[i][i]
								break

							if i == 1 and table[i+1][i] == table[i][i] and table[i-1][i] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							if i == 1 and table[i][i+1] == table[i][i] and table[i][i-1] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							if i == 1 and table[i-1][i+1] == table[i][i] and table[i+1][i-1] == table[i][i]:
								play = 10
								winner = table[i][i]
								break

							if i == 2 and table[i-1][i] == table[i][i] and table[i-2][i] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							if i == 2 and table[i][i-1] == table[i][i] and table[i][i-2] == table[i][i]:
								play = 10
								winner = table[i][i]
								break
							else:
								winner = -1
			if play > 9:
				# end the game printing the winner
				if winner == 0:
					message = "O's win"
				elif winner == 1:
					message = "X's win"
				else:
					message = "Draw"
				font = pygame.font.Font(None, 80) 
				text = font.render(message, 1, (255, 255, 255), (0,0,250))
				screen.blit(text,((backgroundSize[0]/2)-80,(backgroundSize[1]/2)-40))
				pygame.display.flip()



if __name__=="__main__":
    # call the main function
    main()