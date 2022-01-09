#pylint:disable=C0411
#pylint:disable=R0915
#pylint:disable=R1724
#pylint:disable=R1702
#pylint:disable=R0912
#pylint:disable=R0914
#pylint:disable=C0114
#pylint:disable=C0303
#pylint:disable=R0913
#pylint:disable=C0116
#pylint:disable=W0622
#pylint:disable=R0903
#pylint:disable=C0115
#pylint:disable=C0103
import pygame as pg
import random
import time

class Bullet:
	def __init__ (self, bX, rY, winSize):
		self.bX = bX
		self.rY = rY
		if winSize == 0:
			self.rect = pg.Rect(self.bX, self.rY, 25, 25)
		elif winSize == 1:
			self.rect = pg.Rect(self.bX, self.rY, 50, 50)
  
class Block:
    def __init__ (self, bX, bY, id):
        self.rect = pg.Rect(bX, bY, 50, 50)
        self.id = id

def scoreDisp(score, mScrn, window, playerX, playerY, hit):
		scoreFont = pg.font.Font('freesansbold.ttf', 50)
		gameOverSurf = scoreFont.render("Bullets: " + str(score) + " " + 
		#str(window.right) + "x" + str(window.bottom)
		 #+ " " + str(playerX) + "x" + str(int(playerY)) + 
		 " Hits: " + str(hit), 
									True, (255, 255, 255))
		gameOverRect = gameOverSurf.get_rect()
		gameOverRect.topleft = (50, 50)
		mScrn.blit(gameOverSurf, gameOverRect)
	
def gameOverDisp(mScrn):
		scoreFont = pg.font.Font('freesansbold.ttf', 50)
		gameOverSurf = scoreFont.render("Game Over", True, (255, 255, 255))
		gameOverSurf2 = scoreFont.render("press 'r' to rest", True, (255, 255, 255))
		gameOverRect = gameOverSurf.get_rect()
		gameOverRect2 = gameOverSurf2.get_rect()
		gameOverRect2.topleft = (mScrn.get_rect().right // 2.7, (mScrn.get_rect().bottom // 2) + 50)
		gameOverRect.topleft = (mScrn.get_rect().right // 2.5, mScrn.get_rect().bottom // 2)
		mScrn.blit(gameOverSurf, gameOverRect)
		mScrn.blit(gameOverSurf2, gameOverRect2)
		
def enemyMovement(enemyList):
	newEList = []
	rangeSet = [(200, 400), (500, 700), (800, 1000), (1100, 1300)]
	for i in range(len(enemyList)):
			newEList.append((Block(random.randint(rangeSet[i][0], rangeSet[i][1]), 150, 0), True))
	return newEList

def main():

	pg.init()

	running = True
	wideScreen = False

	mScrn = pg.display.set_mode((0, 0))
	window = mScrn.get_rect()
	if window.width >= window.height:
		mScrn = pg.display.set_mode((0, 0))
		wideScreen = True
	else:
		mScrn = pg.display.set_mode((0, window.bottom // 2))
	clock = pg.time.Clock()

	effects = [pg.mixer.Sound('sound96.wav')]

	playerX = 100
	playerY = window.bottom // 1.6
	playerSpeed = 100

	shotCycle = 0
	moveCycle = 0

	bullets = []
	remBullets = 10

	enemyBlocks = [(Block(300, 150, 0), True), (Block(500, 150, 1), True), 
				(Block(700, 150, 2), True), (Block(900, 150, 3), True)]

	hits = 0

	while running:
		clock.tick(60)
		
		scoreDisp(remBullets, mScrn, window, playerX, playerY, hits)
		
		rect1 = pg.Rect(playerX, playerY, 50, 50)
	
		for block in enemyBlocks:
			if block[1]:
				pg.draw.rect(mScrn, (0, 255, 0), block[0])
		
		for r in bullets:
			if r.rect.y <= 0:
				bullets.remove(r)
				continue

			for block in enemyBlocks:
				if pg.Rect.colliderect(r.rect, block[0]):
					bullets.remove(r)
					enemyBlocks.remove(block)
					hits += 1
					continue 
			if window.width <= 1920 and window.height <= 1080:
				pg.draw.rect(mScrn, (255, 255, 255), r.rect)
			else:
				pg.draw.rect(mScrn, (255, 255, 255), r.rect)
			r.rect.y -= 20
			
		if moveCycle >= 500:
			enemyBlocks = 			 					enemyMovement(enemyBlocks)
			moveCycle = 0
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
     
				if event.key == pg.K_a:
					if playerX - playerSpeed < (window.left):
						continue
					playerX -= playerSpeed
    
				if event.key == pg.K_d:
					if playerX + 100 + playerSpeed > (window.right):
						continue
					playerX += playerSpeed
     
				if event.key == pg.K_w:
					if playerY - playerSpeed < window.bottom // 2:
						continue
					playerY -= playerSpeed
     
				if event.key == pg.K_s:
					if playerY + 100 + playerSpeed > (window.bottom // 1.5) and not wideScreen:
						continue
					elif playerY + 100 + playerSpeed > window.bottom and wideScreen:
						continue
					playerY += playerSpeed
     
				if event.key == pg.K_j:
					if shotCycle >= 120 and remBullets >= 1:
						effects[0].play()
						remBullets -= 1
						if wideScreen:
							bullets.append(Bullet(rect1.left, rect1.y - 5, 0))
						else:
							bullets.append(Bullet(rect1.left, rect1.y - 5, 1))
						shotCycle = 0

				# DEBUGGING KEYS
				if event.key == pg.K_r:
					main()
						
		moveCycle += 5
		shotCycle += 5
					
		pg.draw.rect(mScrn, (255, 0, 0), rect1)
		
		if remBullets == 0 and len(enemyBlocks) > 0:
			mScrn.fill((0,0,0))
			gameOverDisp(mScrn)
		
		pg.display.flip()
		
		mScrn.fill((0,0,0))


main()

pg.quit()
	