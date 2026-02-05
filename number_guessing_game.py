
import random 

lowest_num = 1
heighest_num = 100
answer= random.randint(lowest_num, heighest_num)
attempts= 0

print(f"please guess a number between {lowest_num} and  {heighest_num}")
attempts= 0
while True:
    guess= int(input(f"Enter your guess betwween {lowest_num} and  {heighest_num}: "))
    if guess < lowest_num or guess > heighest_num:
        print(f"OUT OF RANGE ! Please guess a number between {lowest_num} and  {heighest_num}")
        continue
    if guess < answer:
        print("too low, try again")
        attempts +=1

    elif guess >answer:
        print("too high , try agian")
        attempts +=1
    else:
        print(f"congrats!! you guessed the num {answer} in {attempts} attempts")
        break


