#pylint:disable=C0103
import pygame as pg

class  Bullet:
	def __init__ (self, bX, rY):
		self.bX = bX
		self.rY = rY

def scoreDisp(score):
	scoreFont = pg.font.Font('freesansbold.ttf', 50)
	gameOverSurf = scoreFont.render("Bullets: " + str(score) + "; " + str(window.right) + "x" + str(window.bottom) + "; " + str(playerX) + "x" + str(int(playerY)), True, (255, 255, 255))
	gameOverRect = gameOverSurf.get_rect()
	gameOverRect.topleft = (50, 50)
	mScrn.blit(gameOverSurf, gameOverRect)

pg.init()

running = True
mScrn = pg.display.set_mode((0, 0))
window = mScrn.get_rect()
mScrn = pg.display.set_mode((0, window.bottom // 2))
clock = pg.time.Clock()

effect = pg.mixer.Sound('sound96.wav')

playerX = window.right // 2
playerY = window.bottom // 1.6
playerSpeed = 100

cycle = 0

bullets = []

while running:
	clock.tick(60)
	
	scoreDisp(len(bullets))
	
	rect1 = pg.Rect(playerX, playerY, 100, 100)
	
	for r in bullets:
		if r.rY <= 0:
			bullets.remove(r)
			continue
		pg.draw.rect(mScrn, (255, 255, 255), pg.Rect(r.bX, r.rY, 50, 50))
		r.rY -= 18
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

		if event.type == pg.KEYDOWN:
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
				if playerY + 100 + playerSpeed > (window.bottom // 1.5):
					continue
				playerY += playerSpeed

			if event.key == pg.K_c:
				mScrn.fill((0,0,0))
			if event.key == pg.K_j:
				if cycle >= 120:
					effect.play()
					bullets.append(Bullet(playerX + 25, playerY + 5))
					cycle = 0
					
	cycle += 5
				
	pg.draw.rect(mScrn, (255, 0, 0), rect1)
	
	pg.display.flip()
	
	mScrn.fill((0,0,0))
	
pg.quit()
	