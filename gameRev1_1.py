import pygame as pg

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

def main():
	def scoreDisp(score):
		scoreFont = pg.font.Font('freesansbold.ttf', 50)
		gameOverSurf = scoreFont.render("Bullets: " + str(score) + "; " + str(window.right) + "x" + 
									str(window.bottom) + "; " + str(playerX) + "x" + str(int(playerY)) +
									"; Hits: " + str(hit), 
									True, (255, 255, 255))
		gameOverRect = gameOverSurf.get_rect()
		gameOverRect.topleft = (50, 50)
		mScrn.blit(gameOverSurf, gameOverRect)

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

	cycle = 0

	bullets = []

	enemyBlocks = [(Block(300, 150, 0), True), (Block(500, 150, 1), True), 
				(Block(700, 150, 2), True), (Block(900, 150, 3), True)]

	hit = 0

	while running:
		clock.tick(60)
		
		scoreDisp(len(bullets))
		
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
					hit += 1
					continue 
			if window.width <= 1920 and window.height <= 1080:
				pg.draw.rect(mScrn, (255, 255, 255), r.rect)
			else:
				pg.draw.rect(mScrn, (255, 255, 255), r.rect)
			r.rect.y -= 20
		
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
					if cycle >= 120:
						effects[0].play()
						if wideScreen:
							bullets.append(Bullet(rect1.left, rect1.y - 5, 0))
						else:
							bullets.append(Bullet(rect1.left, rect1.y - 5, 1))
						cycle = 0

				# DEBUGGING KEYS
				if event.key == pg.K_r:
					main()
						
		cycle += 5
					
		pg.draw.rect(mScrn, (255, 0, 0), rect1)
		
		pg.display.flip()
		
		mScrn.fill((0,0,0))


main()

pg.quit()
	