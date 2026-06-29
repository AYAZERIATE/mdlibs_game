def level2():
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