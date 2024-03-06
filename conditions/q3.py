user1 = str(input("USER1: Enter rock paper or scissors: "))
user2 = str(input("USER2: Enter rock paper or scissors: "))

user1 = user1.upper()
user2 = user2.upper()

if user1 == user2:
    print("Tie")

elif user1 == "ROCK" and user2 == "SCISSORS":
    print("USER1 WINS")

elif user1 == "SCISSORS" and user2 == "ROCK":
    print("USER2 WINS")

elif user1 == "PAPER" and user2 == "ROCK":
    print("USER1 WINS")

elif user1 == "ROCK" and user2 == "PAPER":
    print("USER2 WINS")

elif user1 == "SCISSORS" and user2 == "PAPER":
    print("USER1 WINS")

elif user1 == "PAPER" and user2 == "SCISSORS":
    print("USER2 WINS")

