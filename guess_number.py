import random

num = random.randint(1, 100)
running = True
guess_count = 0
while running:
    guess_num = int(input('Guess number : '))

    if guess_num > num:
        print('Lower number please!')
        guess_count += 1
    elif guess_num < num:
        print('Higher number please!')
        guess_count += 1
    else:
        print(f'You have guessed the number {guess_num} correctly in {guess_count} attempt')
        running = False
