from pygame import*

imgbg = 'bg.jpg'
width = 800
height = 500
win = display.set_mode((width, height))
#win.fill((255, 255, 255))
bg = transform.scale(image.load(imgbg), (width, height))

ballsprite = 'ball.png'
paddlesprite1 = 'thunder.png'
paddlesprite2 = 'thunder.png'

font.init()
font = font.SysFont('Arial', 80)
win1 = font.render('Hey the one on the left, you won', True, (255, 255, 255))
win2 = font.render('Hey the one on the right, you won', True, (255, 255, 255))

class GameSprite(sprite.Sprite):

  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

  def reset(self):
      win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def updateL(self):
        keys = key.get_pressed()
        if keys[K_u] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_d] and self.rect.y < 5:
            self.rect.y += self.speed

    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed


paddle1 = Player(paddlesprite1, 70, 200, 50, 100, 10)
paddle2 = Player(paddlesprite2, 700, 200, 50, 100, 10)
ball = GameSprite(ballsprite, 400, 250, 80, 70, 15)


clock = time.Clock()
FPS = 60
game = True
finish = False

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if game != True:
            win.fill((255, 255, 255))
            win.blit(bg, (0, 0))
            paddle1.updateL()
            paddle2.updateR()

            ball.update()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

            if sprite.collide_rect(paddle1, ball) or sprite.collide_rect(paddle2, ball):
                speed_x *= -1
                speed_y *= -1

            if ball.rect.y > height - 50 or ball.rect.y < 0:
                speed_y *= -1

            if ball.rect.x < 0:
                win.blit(win2, (350, 200))
                finish = True

            if ball.rect.x > width:
                win.blit(win1, (350, 200))
                finish = True

            paddle1.updateL()
            paddle2.updateR()
            paddle1.reset()
            paddle2.reset()
            ball.reset()
            
            display.update()
            clock.tick(FPS)
