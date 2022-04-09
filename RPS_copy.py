# Import and initialize the pygame library
import pygame
import random
 
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([800, 500])
#  652 410     
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True

comp_options: list[str] = ["rock", "paper", "scissors"]

screen.fill((0, 176, 240))

beginning = pygame.image.load("assets/beginning_transparent.png")
screen.blit(beginning, (95, 0))
counting = False 
i: int = 3
user_pick : str = " "
comp_pick: str = random.choice(comp_options)


while running:
    clock.tick(1)

    # background fill
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # comp_pick: str = random.choice(comp_options)
            counting = True
            if event.key == pygame.K_DOWN:  # paper
                user_pick = "paper"
            elif event.key == pygame.K_LEFT:  # rock
                user_pick = "rock"
            elif event.key == pygame.K_RIGHT:  # scissors
                user_pick ="scissors"
    print(f"User pick is {user_pick}")

    if counting:
        screen.fill((0, 176, 240))
        if i == 3:
            count = pygame.image.load("assets/count_3-removebg-preview.png")
            screen.blit(count, (200, 0))
        elif i == 2:
            count = pygame.image.load("assets/count_2-removebg-preview.png")
            screen.blit(count, (200, 0))
        elif i == 1:
            count = pygame.image.load("assets/count_1-removebg-preview.png")
            screen.blit(count, (200, 0))
        elif i == 0:
            screen.fill((0, 176, 240))
            counting = False
        i -= 1
                

    if (not counting) and (user_pick == "paper"):
        print("hello")
        if comp_pick == "rock":
            reveal = pygame.image.load("assets/paper_rock-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "paper":
            reveal = pygame.image.load("assets/paper_paper-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "scissors":
            reveal = pygame.image.load("assets/paper_scissors-removebg-preview.png")
            screen.blit(reveal, (80, 0))

    elif (not counting) and (user_pick == "rock"):
        screen.fill((0, 176, 240))
        if comp_pick == "rock":
            reveal = pygame.image.load("assets/rock_rock-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "paper":
            reveal = pygame.image.load("assets/rock_paper-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "scissors":
            reveal = pygame.image.load("assets/rock_scissors-removebg-preview.png")
            screen.blit(reveal, (80, 0))

    elif (not counting) and (user_pick == "scissors"):
        screen.fill((0, 176, 240))
        if comp_pick == "rock":
            reveal = pygame.image.load("assets/scissors_rock-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "paper":
            reveal = pygame.image.load("assets/scissors_paper-removebg-preview.png")
            screen.blit(reveal, (80, 0))
        elif comp_pick == "scissors":
            reveal = pygame.image.load("assets/scissors_scissors-removebg-preview.png")
            screen.blit(reveal, (80, 0))

    pygame.display.flip()

pygame.quit()