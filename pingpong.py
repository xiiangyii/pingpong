from pygame import*

bg = (255, 255, 255)
width = 500
height = 300
win = display.set_mode((width, height))
win.fill(bg)

clock = time.Clock()
FPS = 60
game = True

ballsprite = 'ball.png'
paddlesprite1 = 'thunder.png'
paddlesprite2 = 'thunder.png'

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
        keys = keys.get_pressed()
        if keys[K_u] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_d] and self.rect.y < 5:
            self.rect.y += self.speed

    def updateR(self):
        keys = keys.pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed


paddle1 = Player(paddlesprite1, 70, 100, 50, 100, 10)
paddle2 = Player(paddlesprite2, 430, 100, 50, 100, 10)

speed_x = 3
speed_y = 3

while game():
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:
            win.fill(bg)
            paddle1.updateL()
            paddle2.updateR()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

    display.update()
    clock.tick(FPS)
