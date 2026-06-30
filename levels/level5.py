def level5():
    print("\n--- Level 5 ---")
    print("Paint your own goals (a window will open)\n")

    import pygame
    import os

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    MENU_HEIGHT = 70

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint Your Own Goals")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill((255, 255, 255))

    brush_size = 10
    color = (0, 0, 0)

    SAVE_FILE = "my_dream.png"

    def draw_menu():
        pygame.draw.rect(screen, (180, 180, 180), (0, 0, WIDTH, MENU_HEIGHT))
        pygame.draw.line(screen, (0, 0, 0), (0, MENU_HEIGHT), (WIDTH, MENU_HEIGHT), 2)

        # Brush size previews
        pygame.draw.circle(screen, (255, 255, 255), (35, 35), 20)
        pygame.draw.circle(screen, (255, 255, 255), (95, 35), 15)
        pygame.draw.circle(screen, (255, 255, 255), (155, 35), 10)
        pygame.draw.circle(screen, (255, 255, 255), (215, 35), 5)

        pygame.draw.rect(screen, (230, 230, 230), (250, 15, 80, 40))
        pygame.draw.rect(screen, (0, 0, 0), (250, 15, 80, 40), 2)
        screen.blit(font.render("Eraser", True, (0, 0, 0)), (262, 26))

        pygame.draw.rect(screen, (170, 255, 170), (350, 15, 70, 40))
        pygame.draw.rect(screen, (0, 0, 0), (350, 15, 70, 40), 2)
        screen.blit(font.render("Save", True, (0, 0, 0)), (366, 26))

        pygame.draw.rect(screen, (170, 220, 255), (440, 15, 70, 40))
        pygame.draw.rect(screen, (0, 0, 0), (440, 15, 70, 40), 2)
        screen.blit(font.render("Open", True, (0, 0, 0)), (455, 26))

        pygame.draw.rect(screen, (255, 180, 180), (530, 15, 70, 40))
        pygame.draw.rect(screen, (0, 0, 0), (530, 15, 70, 40), 2)
        screen.blit(font.render("Clear", True, (0, 0, 0)), (543, 26))

        pygame.draw.rect(screen, (255, 0, 0), (650, 10, 25, 25))
        pygame.draw.rect(screen, (0, 255, 0), (680, 10, 25, 25))
        pygame.draw.rect(screen, (0, 0, 255), (710, 10, 25, 25))
        pygame.draw.rect(screen, (255, 255, 0), (740, 10, 25, 25))
        pygame.draw.rect(screen, (0, 0, 0), (770, 10, 25, 25))

    running = True
    while running:
        clock.tick(60)
        screen.blit(canvas, (0, 0))
        draw_menu()

        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and mouse[1] > MENU_HEIGHT:
            pygame.draw.circle(canvas, color, mouse, brush_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < MENU_HEIGHT:
                    if 15 < x < 55:
                        brush_size = 20
                    elif 75 < x < 115:
                        brush_size = 15
                    elif 135 < x < 175:
                        brush_size = 10
                    elif 195 < x < 235:
                        brush_size = 5
                    elif 250 < x < 330:
                        color = (255, 255, 255)
                    elif 350 < x < 420:
                        pygame.image.save(canvas, SAVE_FILE)
                        print("Drawing saved!")
                    elif 440 < x < 510:
                        if os.path.exists(SAVE_FILE):
                            image = pygame.image.load(SAVE_FILE)
                            image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                            canvas.blit(image, (0, 0))
                            print("Drawing loaded!")
                        else:
                            print("No saved drawing found.")
                    elif 530 < x < 600:
                        canvas.fill((255, 255, 255))
                    elif 650 < x < 675:
                        color = (255, 0, 0)
                    elif 680 < x < 705:
                        color = (0, 255, 0)
                    elif 710 < x < 735:
                        color = (0, 0, 255)
                    elif 740 < x < 765:
                        color = (255, 255, 0)
                    elif 770 < x < 795:
                        color = (0, 0, 0)

        pygame.display.flip()

    pygame.quit()