#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL) #sets level for logging
logger = logging.getLogger(__name__) #get logger

screen_size = (800,600) #sets reslution
FPS = 60 # sets fps
red = (255,0,0) #rgb for red
black = (0,0,0) #rgb for black

class Block(pygame.sprite.Sprite): #creates Block class
	def __init__(self, position, direction): # autoruns
		pygame.sprite.Sprite.__init__(self) # intializes sprite
		self.image = pygame.Surface((50, 50)) # sets dimensions for the block
		self.image.fill(red) # sets color for the block
		self.rect = self.image.get_rect() #gets rectangle
		(self.rect.x,self.rect.y) = position #sets position
		self.direction = direction #allows for movement

	def update(self):
		(dx,dy) = self.direction #assigns a variable for direction
		self.rect.x += dx #x = to position (change in x)
		self.rect.y += dy #y = to position (change in y)
		(WIDTH,HEIGHT) = screen_size  #assigns witdh and height to screen_size
		if self.rect.left > WIDTH: #checks if sprite reaches the edge of the screen (x)
			self.rect.right = 0 #places it on opposite side
		if self.rect.right < 0: #checks if sprite reaches the edge of the screen (x)
			self.rect.left = WIDTH  #places it on opposite side
		if self.rect.top > HEIGHT:#checks if sprite reaches the edge of the screen (y)
			self.rect.bottom = 0 #places it on opposite side
		if self.rect.bottom < 0: #checks if sprite reaches the edge of the screen (y)
			self.rect.top = HEIGHT #places it on opposite side


def main(): # defines main
	pygame.init() #required for all programs using pygame
	screen = pygame.display.set_mode(screen_size) # sets screen size to previously defined resolution
	clock = pygame.time.Clock() #assigns clock

	blocks = pygame.sprite.Group()  #puts blocks in sprite group
	block = Block((200,200),(-1,1)) #sets dimensions and starting point of block
	blocks.add(block) #add block to list

	while True: #infinite loop as long as True
		clock.tick(FPS) #sets FPS to assigned value
		screen.fill(black) #background = black

		for event in pygame.event.get(): #game loop
			if event.type == pygame.QUIT: #if quit event is called
				pygame.quit() #quit
				sys.exit(0) #exit

		blocks.update() #updates blocks
		blocks.draw(screen) #draws the blocks
		pygame.display.flip() #displays all at once

if __name__ == '__main__': #to see if module or not
	main() #runs main