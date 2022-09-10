import pygame


class HeroShip:
    def __init__(self, screen_height, screen_width, image_file):
        self.shape = pygame.image.load(image_file)
        self.top = screen_height - self.shape.get_height()
        self.left = screen_width / 2 - self.shape.get_width() / 2
        self.screen_width = screen_width
        self.screen_height = screen_height

    def ShowHeroShip(self, game_screen):
        game_screen.blit(self.shape, (self.left, self.top))
        # Keep player inside the window/screen
        if self.left <= 0:
            self.left = 0
        if self.left > screen.get_width():
            self.left = self.screen_width
        if self.top <= 0:
            self.top = 0
        if self.top > screen.get_height():
            self.top = screen.get_height()

    # Move horizontally
    def UpdateCoordinates(self, horizontal, vertical):
        self.left = horizontal - self.shape.get_width() / 2
        self.top = vertical - self.shape.get_height() / 2


class ScrollingBackground:
    def __init__(self, height, image_file):
        self.image = pygame.image.load(image_file)
        self.coordinates = [0, 0]
        self.coordinates2 = [0, -height]
        self.yOriginalValue = self.coordinates[1]
        self.yOriginalValue2 = self.coordinates2[1]

    def ShowBackground(self, screen):
        screen.blit(self.image, self.coordinates)
        screen.blit(self.image, self.coordinates2)

    def UpdateCoordinates(self, speed_y, game_time):
        distance_y = speed_y * game_time
        self.coordinates[1] += distance_y
        self.coordinates2[1] += distance_y
        if self.coordinates2[1] >= 0:
            self.coordinates[1] = self.yOriginalValue
            self.coordinates2[1] = self.yOriginalValue2


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screenwidth, screenheight = (600, 600)

screen = pygame.display.set_mode((screenwidth, screenheight), pygame.RESIZABLE)

screen_rect = screen.get_rect()

# Set the frame rate
frame_rate = 60

# Set background scrolling speed
background_speed = 100

# Load Image...

spaceImage = ScrollingBackground(screenheight, "Images/Stars.jpg")
hero = HeroShip(screenheight, screenwidth, "Images/passenger icon_4.png")

mouse_visible = True
pygame.mouse.set_visible(1)

pygame.display.set_caption('Space Age Game')

running = True
while running:

    time = clock.tick(frame_rate) / 1000.0

    # Poll inputs/events...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.VIDEORESIZE:
            old_surface_saved = screen
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screen.blit(old_surface_saved, (0, 0))
            del old_surface_saved
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if mouse_visible:
                    mouse_visible = False
                    pygame.mouse.set_visible(False)
                else:
                    mouse_visible = True
                    pygame.mouse.set_visible(True)

    # Storing the mouse position
    x, y = pygame.mouse.get_pos()
    # Draw Scrolling Background, Set background coordinates & update the screen
    pygame.display.flip()
    spaceImage.UpdateCoordinates(background_speed, time)
    spaceImage.ShowBackground(screen)

    HeroShip.UpdateCoordinates(hero, x, y)
    HeroShip.ShowHeroShip(hero, screen)

pygame.quit()