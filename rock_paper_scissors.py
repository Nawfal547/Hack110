# Import and initialize the pygame library
import pygame
import random
 
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([652, 410])
                               
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True

comp_options: list[str] = ["rock", "paper", "scissors"]

screen.fill((0, 176, 240))

beginning = pygame.image.load("assets/beginning_transparent.png")
screen.blit(beginning, (20, 0))

while running:
    clock.tick(60)

    # background fill

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            comp_pick: str = random.choice(comp_options)
            if event.key == pygame.K_DOWN:  # paper
                screen.fill((0, 176, 240))

                if comp_pick == "rock":
                    reveal = pygame.image.load("assets/paper_rock-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "paper":
                    reveal = pygame.image.load("assets/paper_paper-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "scissors":
                    reveal = pygame.image.load("assets/paper_scissors-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
            elif event.key == pygame.K_LEFT:  # rock
                screen.fill((0, 176, 240))
                if comp_pick == "rock":
                    reveal = pygame.image.load("assets/rock_rock-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "paper":
                    reveal = pygame.image.load("assets/rock_paper-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "scissors":
                    reveal = pygame.image.load("assets/rock_scissors-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
            elif event.key == pygame.K_RIGHT:  # scissors
                screen.fill((0, 176, 240))
                if comp_pick == "rock":
                    reveal = pygame.image.load("assets/scissors_rock-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "paper":
                    reveal = pygame.image.load("assets/scissors_paper-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
                elif comp_pick == "scissors":
                    reveal = pygame.image.load("assets/scissors_scissors-removebg-preview.png")
                    screen.blit(reveal, (0, 0))
    pygame.display.flip()


pygame.quit()