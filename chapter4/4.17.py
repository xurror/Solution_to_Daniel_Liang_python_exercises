import random

# Generate a number
num = random.randint(0, 2)
scissor, rock, paper = 'scissor', 'rock', 'paper' 
player = eval(input("scissor (0), rock (1), paper (2): "))
if num == 0:
    num = scissor
elif num == 1:
    num = rock
elif num == 2:
    num = paper

if player == 0:
    player = scissor
elif player == 1:
    player = rock
elif player == 2:
    player = paper

if player == num:
    player = num
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          " too. It is a draw")
elif player == 0 and num == 1:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You lose.")
elif player == 0 and num == 2:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You win.")
elif player == 1 and num == 2:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You lose.")
elif player == 1 and num == 0:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You win.")
elif player == 2 and num == 0:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You lose.")
elif player == 2 and num == 1:
    print("The computer is " +
          str(num) + ". You are " +
          str(player) +
          ". You win.")



    

