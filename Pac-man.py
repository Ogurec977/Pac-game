import copy
import random

import pygame

pygame.init()
winows_size = (650, 600)  # размеры экрана
wSurface = pygame.display.set_mode(winows_size, 0, 32)
pygame.display.set_caption("Pac-Man")
yellow = (255, 255, 0)  # жёлтый цвет
FPS = 60


class Walls(object):
    def create_walls(self):  # Создание стенок
        walles = [pygame.Rect((100, 48), (448, 8)), pygame.Rect((100, 55), (7, 152)), pygame.Rect((180, 200), (8, 64)),
                  pygame.Rect((268, 248), (8, 64)), pygame.Rect((140, 88), (48, 32)), pygame.Rect((220, 88), (64, 32)),
                  pygame.Rect((364, 88), (65, 32)), pygame.Rect((460, 88), (49, 32)), pygame.Rect((100, 200), (86, 8)),
                  pygame.Rect((140, 152), (48, 16)), pygame.Rect((316, 55), (16, 65)), pygame.Rect((540, 55), (8, 153)),
                  pygame.Rect((460, 200), (88, 8)), pygame.Rect((460, 152), (49, 16)),
                  pygame.Rect((412, 152), (16, 112)),
                  pygame.Rect((364, 200), (50, 16)), pygame.Rect((268, 152), (112, 16)),
                  pygame.Rect((316, 166), (16, 50)),
                  pygame.Rect((220, 152), (16, 112)), pygame.Rect((235, 200), (49, 16)),
                  pygame.Rect((100, 256), (88, 8)),
                  pygame.Rect((460, 256), (89, 8)), pygame.Rect((460, 296), (89, 8)), pygame.Rect((460, 352), (88, 8)),
                  pygame.Rect((460, 296), (9, 64)), pygame.Rect((412, 296), (17, 65)),
                  pygame.Rect((220, 296), (16, 64)),
                  pygame.Rect((460, 200), (8, 64)), pygame.Rect((100, 296), (88, 8)), pygame.Rect((179, 296), (9, 64)),
                  pygame.Rect((100, 352), (88, 8)), pygame.Rect((100, 352), (8, 193)),
                  pygame.Rect((107, 440), (33, 16)),
                  pygame.Rect((100, 536), (448, 9)), pygame.Rect((540, 352), (8, 193)),
                  pygame.Rect((508, 440), (34, 16)),
                  pygame.Rect((268, 248), (40, 8)), pygame.Rect((340, 248), (41, 8)), pygame.Rect((460, 200), (9, 64)),
                  pygame.Rect((139, 392), (49, 17)), pygame.Rect((171, 406), (17, 51)),
                  pygame.Rect((220, 392), (64, 17)),
                  pygame.Rect((364, 392), (65, 17)), pygame.Rect((460, 392), (49, 17)),
                  pygame.Rect((460, 406), (17, 51)),
                  pygame.Rect((412, 440), (17, 50)), pygame.Rect((364, 488), (145, 17)),
                  pygame.Rect((267, 440), (114, 17)),
                  pygame.Rect((316, 358), (16, 51)), pygame.Rect((220, 440), (16, 50)),
                  pygame.Rect((139, 488), (145, 17)),
                  pygame.Rect((372, 248), (9, 64)), pygame.Rect((268, 304), (113, 7)),
                  pygame.Rect((268, 344), (112, 16)),
                  pygame.Rect((316, 455), (16, 50)), pygame.Rect((268, 248), (112, 64))]

        return walles


class Sound(object):  # загрузка всех звуков игре
    pygame.mixer.init()
    Sounds = pygame.mixer.Channel(2)
    Begin = pygame.mixer.Sound("opening_song.wav")
    small_ball = pygame.mixer.Sound("waka_waka.wav")
    large_ball = pygame.mixer.Sound("eating_cherry.wav")
    Eat_ghost = pygame.mixer.Sound("eating_ghost.wav")
    die = pygame.mixer.Sound("pacmandies.wav")
    game_over = pygame.mixer.Sound("game_over.wav")
    game_win = pygame.mixer.Sound("you_win.wav")


class Ball(object):  # создание шаров
    images = [pygame.image.load("dot.png").convert(),
              pygame.image.load("cherry.jpg").convert()]
    imageRects = [images[0].get_rect(), images[1].get_rect()]
    shifts = [(-images[0].get_width() / 2, -images[0].get_height() / 2),
              (-images[1].get_width() / 2, -images[1].get_height() / 2)]

    def create_List_Small(self):  # маленькие
        pellets = [(350, 72), (350, 423), (485, 185), (125, 185), (445, 424), (485, 136), (125, 378), (395, 378),
                   (485, 72), (395, 424), (445, 72), (445, 136), (165, 424), (255, 185), (395, 136), (125, 104),
                   (205, 424), (205, 136), (395, 474), (165, 520), (255, 136), (165, 72), (205, 72), (255, 378),
                   (395, 330), (205, 330), (350, 104), (525, 185), (525, 378), (525, 474), (485, 474), (445, 185),
                   (525, 424), (300, 72), (350, 474), (350, 232), (485, 520), (445, 520), (485, 424), (445, 280),
                   (165, 378), (395, 185), (445, 378), (125, 474), (205, 520), (205, 185), (350, 185), (255, 520),
                   (350, 378), (350, 136), (300, 136), (300, 104), (445, 232), (205, 232), (445, 330), (300, 474),
                   (125, 424), (255, 72), (125, 136), (300, 520), (395, 520), (205, 281), (205, 104), (300, 185),
                   (255, 330), (165, 185), (165, 136), (205, 474), (205, 378), (255, 474), (395, 232), (165, 474),
                   (255, 232), (300, 378), (350, 330), (255, 280), (525, 104), (300, 330), (525, 136), (395, 72),
                   (485, 378), (445, 104), (350, 520), (300, 424), (300, 232), (445, 474), (395, 280), (255, 424)]
        return pellets

    def create_list_large(self):  # Вишня
        pellets = [(125, 72), (125, 520), (525, 72), (525, 520)]
        return pellets

    def check(self, pellets_s, pellets_l, pacman, ghosts):  # Съедание шаров
        for i, e in enumerate(pellets_s[:]):
            p_rect = Ball.imageRects[0]
            (p_rect.centerx, p_rect.centery) = e
            if p_rect.colliderect(pacman.rect):
                del pellets_s[i]
                pacman.score += 10
                if not Sound.Sounds.get_busy():
                    Sound.Sounds.play(Sound.small_ball)

        for i, z in enumerate(pellets_l[:]):
            p_rect = Ball.imageRects[1]
            (p_rect.centerx, p_rect.centery) = z
            if p_rect.colliderect(pacman.rect):
                for g in ghosts:
                    g.makeBlue()
                del pellets_l[i]
                pacman.score += 50
                if not Sound.Sounds.get_busy():
                    Sound.Sounds.play(Sound.large_ball)


class Character(object):  # класс для всех персонажей
    def __init__(self):
        self.surface = None
        self.rect = None
        self.speed = None

    def can_move(self, direction, walls):  # когда могут двигаться персонажи
        global recttan
        if direction == 0:
            recttan = self.rect.move((0, -self.speed))
        elif direction == 1:
            recttan = self.rect.move((-self.speed, 0))
        elif direction == 2:
            recttan = self.rect.move((0, self.speed))
        elif direction == 3:
            recttan = self.rect.move((self.speed, 0))

        for wall in walls:
            if wall.colliderect(recttan):
                return False
        return True

    def move(self, direction):  # движение
        if direction == 0:
            self.rect.top -= self.speed
        elif direction == 1:
            self.rect.left -= self.speed
        elif direction == 2:
            self.rect.top += self.speed
        elif direction == 3:
            self.rect.left += self.speed


class Pacman(Character):  # Паакман
    images = [pygame.image.load("player_u0.png").convert(),
              pygame.image.load("player_u1.png").convert(),
              pygame.image.load("player_r1.png").convert()]
    for i in range(len(images)):
        images[i].set_colorkey((0, 0, 0))

    def __init__(self):
        super().__init__()
        self.surface = Pacman.images[0]
        self.isFirstPic = True
        self.frame = 0
        self.rect = self.surface.get_rect()
        self.rect.left = 315
        self.rect.top = 315
        self.direction = 0
        self.speed = 2
        self.moveUp = self.moveLeft = self.moveDown = self.moveRight = False
        self.score = 0
        self.lives = 3

    def reset(self):
        self.surface = Pacman.images[0]
        self.isFirstPic = True
        self.frame = 0
        self.rect.left = 315
        self.rect.top = 315
        self.direction = 0
        self.moveUp = self.moveLeft = self.moveDown = self.moveRight = False

    def getSurface(self):
        self.frame += 1
        if self.frame == 3:
            self.isFirstPic = not self.isFirstPic
            self.frame = 0

        if self.direction == 0:
            self.surface = Pacman.images[self.isFirstPic]
        elif self.direction == 1:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], 90)
        elif self.direction == 2:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], 180)
        elif self.direction == 3:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], 270)

    def move(self, walls):
        if self.moveUp and self.can_move(0, walls):
            Character.move(self, 0)
        if self.moveLeft and self.can_move(1, walls):
            Character.move(self, 1)
        if self.moveDown and self.can_move(2, walls):
            Character.move(self, 2)
        if self.moveRight and self.can_move(3, walls):
            Character.move(self, 3)

    def teleport(self):  # телепорт когда выходишь из поля
        if self.rect.colliderect(pygame.Rect((100, 256), (6, 48))):
            self.rect.left += 400
        if self.rect.colliderect(pygame.Rect((549, 256), (6, 48))):
            self.rect.left -= 400

    def getScoreSurface(self):  # Очки
        global yellow
        return pygame.font.SysFont(None, 48).render("Очки: " + str(self.score), True, yellow)

    def getLivesSurface(self):  # Жизни
        global yellow
        surface = pygame.font.SysFont(None, 48).render("Жизни                             ", True, yellow)
        x = 125
        for i in range(self.lives):
            surface.blit(Pacman.images[2], (x, 5))
            x += 25
        return surface

    def getWinningSurface(self):  # Победа
        global yellow
        return pygame.font.SysFont(None, 72).render("Ты выйграл!   Очки: " + str(self.score), True, yellow)

    def getLosingSurface(self):  # Проигрыш
        global yellow
        return pygame.font.SysFont(None, 72).render("Ты проиграл(   Очки:" + str(self.score), True, yellow)


class Ghost(Character):  # Класс призраков
    images = [pygame.image.load("orange.png").convert(),
              pygame.image.load("blue.jpg").convert()]
    for i in range(len(images)):
        images[i].set_colorkey((0, 0, 0))
    ISBLUE_TIME = int(10 * FPS)
    ADD_TIME = int(30 * FPS)
    add_time = ADD_TIME

    def __init__(self):
        super().__init__()
        self.surface = Ghost.images[0]
        self.rect = self.surface.get_rect()
        self.rect.left = 315
        self.rect.top = 275
        self.speed = 1
        self.course = [0] * round(50 / self.speed)
        self.isBlue = False
        self.isBlue_time = 0

    def makeBlue(self):  # Синий
        self.isBlue = True
        self.isBlue_time = Ghost.ISBLUE_TIME
        self.surface = Ghost.images[1]
        self.course = []

    def makeNotBlue(self):  # Оранжевый
        self.surface = Ghost.images[0]
        self.course = []
        self.isBlue = False
        self.isBlue_time = 0

    def checkBlue(self):  # Проверка на синего
        self.isBlue_time -= 1
        if self.isBlue_time <= 0:
            self.makeNotBlue()

    def reset(self):  # Делать обратно в оранжегого
        self.makeNotBlue()
        self.rect.left = 315
        self.rect.top = 275
        self.course = ([0] * round(50 / self.speed))

    def add(self, ghosts):  # Добавление призрака
        Ghost.add_time -= 1
        if len(ghosts) == 0:
            if Ghost.add_time > int(Ghost.ADD_TIME / 10.0):
                Ghost.add_time = int(Ghost.ADD_TIME / 10.0)

        if Ghost.add_time <= 0:
            ghosts.append(Ghost())
            Ghost.add_time = Ghost.ADD_TIME

    def canMove_distance(self, direction, walls):  # На каком расстояние
        test = copy.copy(self)
        counter = 0
        while True:
            if not Character.can_move(test, direction, walls):
                break
            Character.move(test, direction)
            counter += 1
        return counter

    #
    #
    #
    def moves(self, walls, pacman):  # Их движение
        if len(self.course) > 0:
            if self.can_move(self.course[0], walls) or self.rect.colliderect(pygame.Rect((268, 248), (112, 64))):
                Character.move(self, self.course[0])
                del self.course[0]
            else:
                self.course = []

        else:
            x_distance = pacman.rect.left - self.rect.left
            y_distance = pacman.rect.top - self.rect.top
            choices = [-1, -1, -1, -1]

            if abs(x_distance) > abs(y_distance):
                if x_distance > 0:
                    choices[0] = 3
                    choices[3] = 1
                elif x_distance < 0:
                    choices[0] = 1
                    choices[3] = 3

                if y_distance > 0:
                    choices[1] = 2
                    choices[2] = 0
                elif y_distance < 0:
                    choices[1] = 0
                    choices[2] = 2
                else:
                    if self.canMove_distance(2, walls) < self.canMove_distance(0, walls):
                        choices[1] = 2
                        choices[2] = 0
                    elif self.canMove_distance(0, walls) < self.canMove_distance(2, walls):
                        choices[1] = 0
                        choices[2] = 2

            elif abs(y_distance) >= abs(x_distance):
                if y_distance > 0:
                    choices[0] = 2
                    choices[3] = 0
                elif y_distance < 0:
                    choices[0] = 0
                    choices[3] = 2

                if x_distance > 0:
                    choices[1] = 3
                    choices[2] = 1
                elif x_distance < 0:
                    choices[1] = 1
                    choices[2] = 3
                else:
                    if self.canMove_distance(3, walls) < self.canMove_distance(1, walls):
                        choices[1] = 3
                        choices[2] = 1
                    elif self.canMove_distance(1, walls) < self.canMove_distance(3, walls):
                        choices[1] = 1
                        choices[2] = 3

            if self.isBlue:
                choices.reverse()
            choices_original = choices[:]
            for i, x in enumerate(choices[:]):
                if x == -1 or (not Character.can_move(self, x, walls)):
                    del choices[choices.index(x)]

            if len(choices) > 0:
                Character.move(self, choices[0])
                if choices_original.index(choices[0]) >= 2:
                    global FPS
                    for i in range(int(FPS * 1.5)):
                        self.course.append(choices[0])


# Загрузка основных классов
background = pygame.image.load("bg.png").convert()
pacman = Pacman()
ghosts = [Ghost()]
walls = Walls.create_walls(Walls())
pellets_small = Ball.create_List_Small(Ball())
pellets_large = Ball.create_list_large(Ball())
clock = pygame.time.Clock()
pygame.mixer.music.load("backgrond.wav")
pygame.mixer.music.set_volume(0.5)

# закрузка шаров и музыки
Sound.Sounds.play(Sound.Begin)
wSurface.fill((0, 0, 0))
wSurface.blit(background, (100, 0))
wSurface.blit(pacman.getScoreSurface(), (10, 10))
wSurface.blit(pacman.getLivesSurface(), (winows_size[0] - 200, 10))
for p in pellets_small:
    wSurface.blit(Ball.images[0], (p[0] + Ball.shifts[0][0], p[1] + Ball.shifts[0][1]))
for p in pellets_large:
    wSurface.blit(Ball.images[1], (p[0] + Ball.shifts[1][0], p[1] + Ball.shifts[1][1]))
for g in ghosts:
    wSurface.blit(g.surface, g.rect)
wSurface.blit(pacman.surface, pacman.rect)
pygame.display.update()
while True:
    if not pygame.mixer.get_busy():
        break

keepGoing_game = True
while keepGoing_game:
    keepGoing_round = True
    pygame.mixer.music.play(-1, 0.0)
    while keepGoing_round:
        clock.tick(FPS)

        # управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing_game = keepGoing_round = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.moveUp = True
                    pacman.moveLeft = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 0
                elif event.key == pygame.K_LEFT:
                    pacman.moveLeft = True
                    pacman.moveUp = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 1
                elif event.key == pygame.K_DOWN:
                    pacman.moveDown = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveRight = False
                    pacman.direction = 2
                elif event.key == pygame.K_RIGHT:
                    pacman.moveRight = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveDown = False
                    pacman.direction = 3

            elif event.type == pygame.KEYUP:
                pacman.moveUp = pacman.moveLeft = pacman.moveDown = pacman.moveRight = False

        # Загрузка поля
        pacman.move(walls)

        pacman.teleport()

        pacman.getSurface()

        Ball.check(Ball(), pellets_small, pellets_large, pacman, ghosts)

        Ghost.add(Ghost(), ghosts)

        for g in ghosts:
            if g.isBlue:
                g.checkBlue()

        # Загрузка графики
        for g in ghosts:
            g.moves(walls, pacman)
        wSurface.fill((0, 0, 0))
        wSurface.blit(background, (100, 0))
        wSurface.blit(pacman.getScoreSurface(), (10, 10))
        wSurface.blit(pacman.getLivesSurface(), (winows_size[0] - 200, 10))
        for p in pellets_small:
            wSurface.blit(Ball.images[0], (p[0] + Ball.shifts[0][0], p[1] + Ball.shifts[0][1]))
        for p in pellets_large:
            wSurface.blit(Ball.images[1], (p[0] + Ball.shifts[1][0], p[1] + Ball.shifts[1][1]))
        for g in ghosts:
            wSurface.blit(g.surface, g.rect)
        wSurface.blit(pacman.surface, pacman.rect)
        pygame.display.update()

        for g in ghosts[:]:
            if pacman.rect.colliderect(g.rect):
                if not g.isBlue:
                    keepGoing_round = False
                    pacman.lives -= 1
                    if pacman.lives == 0:
                        keepGoing_game = False
                    else:
                        Sound.Sounds.play(Sound.die)
                    break
                else:
                    del ghosts[ghosts.index(g)]
                    pacman.score += 100
                    Sound.Sounds.play(Sound.Eat_ghost)
        else:
            if len(pellets_small) == 0 and len(pellets_large) == 0:
                keepGoing_game = keepGoing_round = False

    pygame.mixer.music.stop()
    pacman.reset()
    for g in ghosts:
        g.reset()
    while True:
        if not pygame.mixer.get_busy():
            break

wSurface.fill((0, 0, 0))
surface_temp = None

if pacman.lives == 0:  # Проверка на жизни
    Sound.Sounds.play(Sound.game_over)
    surface_temp = pacman.getLosingSurface()

# Проверка на шары
elif len(pellets_small) == 0 and len(pellets_large) == 0:
    Sound.Sounds.play(Sound.game_win)
    surface_temp = pacman.getWinningSurface()

if surface_temp is not None:
    rect_temp = surface_temp.get_rect()
    rect_temp.center = wSurface.get_rect().center
    wSurface.blit(surface_temp, rect_temp)
    pygame.display.update()

while True:
    if not pygame.mixer.get_busy():
        pygame.quit()
        break
