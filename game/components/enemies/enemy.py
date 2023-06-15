import random

class Enemy:
    
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
    
    def update(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == self.LEFT:
            self.rect.x -= self.SPEED_X
        else:
            self.rect.x += self.SPEED_X
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)