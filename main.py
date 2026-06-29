print("level 1")
print("The Story of a Successful Boy")

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person): ")
adjective2 = input("Enter another adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter one more adjective (description): ")

print(f"Once upon a time, there was a {adjective1} boy named {noun1}.")
print(f"Although he came from a small town, he dreamed of achieving great things in life.")
print(f"Every single day, he spent hours {verb1} because he believed that hard work was the key to success.")
print(f"Many people thought his dreams were impossible, but {noun1} never listened to negative comments.")
print(f"He remained {adjective2}, determined, and focused on improving himself every day.")
print(f"Whenever he faced difficulties, he treated them as opportunities to learn instead of giving up.")
print(f"His teachers, friends, and family were amazed by his dedication and strong mindset.")
print(f"After many years of patience, effort, and determination, {noun1} finally reached his goals.")
print(f"He became a {adjective3} entrepreneur who inspired thousands of young people around the world.")
print(f"His story reminds us that success does not come from luck but from believing in yourself, working hard, and never giving up on your dreams.")

print(" Level 2")
print("How about creating your own success story?\n")

gender = input("Are you a girl or a boy? ").strip().lower()

if gender == "girl":
    adjective1 = input("Enter an adjective that describes you: ")
    name = input("Enter your name: ")
    adjective2 = input("Enter another adjective: ")

    print("\n --- Your Success Story ---\n")
    print(f"My name is {name}. I am a {adjective1} girl who believes that {adjective2} work and determination can achieve anything. "
          "Every day I learn something new, face challenges with courage, and never give up on my dreams. "
          "Although life is not always easy, I stay positive and keep moving forward. "
          "I know that every mistake is a lesson and every success is a reward for my effort. "
          "I will continue working hard until I reach my goals and inspire others to believe in themselves.")

if gender == "boy":
    adjective1 = input("Enter an adjective that describes you: ")
    name = input("Enter your name: ")
    adjective2 = input("Enter another adjective: ")

    print("\n --- Your Success Story ---\n")
    print(f"My name is {name}. I am a {adjective1} boy who believes that {adjective2} work and perseverance lead to success. "
          "I never stop learning, even when things become difficult. "
          "Every challenge makes me stronger, every failure teaches me an important lesson, and every achievement motivates me to dream bigger. "
          "I know that success comes to those who are patient, determined, and willing to work hard. "
          "I will continue chasing my dreams and creating a future that makes me proud.")
print("level 3")
print("manage your own live")
print("this level is going to make you improve your goals in live")

import calendar
import json
from datetime import datetime

FILE_NAME = "goals.json"
def load_goals():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_goals(goals):
    with open(FILE_NAME, "w") as file:
        json.dump(goals, file, indent=4)



def show_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print()
    print(calendar.month(year, month))



def add_goal(goals):
    date = input("Enter date (YYYY-MM-DD): ")
    goal = input("Enter your goal: ")

    goals[date] = goal
    save_goals(goals)

    print("\n Goal saved successfully!\n")



def view_goals(goals):

    if not goals:
        print("\nNo goals found.\n")
        return

    print("\n===== MY GOALS =====")

    for date, goal in sorted(goals.items()):
        print(f"{date} → {goal}")

    print()



def delete_goal(goals):

    date = input("Enter the date of the goal to delete: ")

    if date in goals:
        del goals[date]
        save_goals(goals)
        print(" Goal deleted.\n")
    else:
        print("Goal not found.\n")


def main():

    goals = load_goals()

    while True:

        print("=" * 35)
        print("      MY GOAL CALENDAR")
        print("=" * 35)

        print("1. Show Calendar")
        print("2. Add Goal")
        print("3. View Goals")
        print("4. Delete Goal")
        print("5. Today's Date")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_calendar()

        elif choice == "2":
            add_goal(goals)

        elif choice == "3":
            view_goals(goals)

        elif choice == "4":
            delete_goal(goals)

        elif choice == "5":
            today = datetime.now()
            print("\nToday's date:", today.strftime("%A, %d %B %Y"))
            print()

        elif choice == "6":
            print("\nGood luck achieving your goals! ")
            break

        else:
            print("\nInvalid option.\n")


main()

print("Level 4")
print("Goal Priorities\n")

goal = input("Enter your goal: ")
months = int(input("In how many months do you want to achieve it? "))

if months > 4:
    priority = "High"
elif months == 4:
    priority = "Medium"
else:
    priority = "Low"

print("\n----- Goal Information -----")
print(f"Goal: {goal}")
print(f"Time: {months} months")
print(f"Priority: {priority}")

print("level 5")
print("paint your own goals")
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
    pygame.draw.line(screen, (0, 0, 0), (0, MENU_HEIGHT),
                     (WIDTH, MENU_HEIGHT), 2)

    pygame.draw.circle(screen, (255,255,255), (35,35),20)
    pygame.draw.circle(screen, (255,255,255), (95,35),15)
    pygame.draw.circle(screen, (255,255,255), (155,35),10)
    pygame.draw.circle(screen, (255,255,255), (215,35),5)

    pygame.draw.rect(screen,(230,230,230),(250,15,80,40))
    pygame.draw.rect(screen,(0,0,0),(250,15,80,40),2)
    screen.blit(font.render("Eraser",True,(0,0,0)),(262,26))

    pygame.draw.rect(screen,(170,255,170),(350,15,70,40))
    pygame.draw.rect(screen,(0,0,0),(350,15,70,40),2)
    screen.blit(font.render("Save",True,(0,0,0)),(366,26))

    pygame.draw.rect(screen,(170,220,255),(440,15,70,40))
    pygame.draw.rect(screen,(0,0,0),(440,15,70,40),2)
    screen.blit(font.render("Open",True,(0,0,0)),(455,26))

    pygame.draw.rect(screen,(255,180,180),(530,15,70,40))
    pygame.draw.rect(screen,(0,0,0),(530,15,70,40),2)
    screen.blit(font.render("Clear",True,(0,0,0)),(543,26))

    pygame.draw.rect(screen,(255,0,0),(650,10,25,25))
    pygame.draw.rect(screen,(0,255,0),(680,10,25,25))
    pygame.draw.rect(screen,(0,0,255),(710,10,25,25))
    pygame.draw.rect(screen,(255,255,0),(740,10,25,25))
    pygame.draw.rect(screen,(0,0,0),(770,10,25,25))


running = True

while running:

    clock.tick(60)

    screen.blit(canvas, (0, 0))

    draw_menu()

    mouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:

        if mouse[1] > MENU_HEIGHT:
            pygame.draw.circle(canvas, color, mouse, brush_size)

    # Events
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
                    color = (255,255,255)

                elif 350 < x < 420:
                    pygame.image.save(canvas, SAVE_FILE)
                    print("Drawing saved!")

                elif 440 < x < 510:
                    if os.path.exists(SAVE_FILE):
                        image = pygame.image.load(SAVE_FILE)
                        image = pygame.transform.scale(image,
                                                       (WIDTH, HEIGHT))
                        canvas.blit(image,(0,0))
                        print("Drawing loaded!")
                    else:
                        print("No saved drawing found.")

                elif 530 < x < 600:
                    canvas.fill((255,255,255))

                elif 650 < x < 675:
                    color = (255,0,0)

                elif 680 < x < 705:
                    color = (0,255,0)

                elif 710 < x < 735:
                    color = (0,0,255)

                elif 740 < x < 765:
                    color = (255,255,0)

                elif 770 < x < 795:
                    color = (0,0,0)

    pygame.display.flip()

pygame.quit()

