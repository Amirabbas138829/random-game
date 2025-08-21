import random 
number=random.randint(1,100)
print("guess my mind , choose number between 1 to 100!(you have 3 times to try)")
for i in range(3):
    guess=int(input(f"guess{i+1}:"))
    if guess==number:
        print("you win!")
        break
    else :
        print("it's false!")
if guess!=number:
    print(f"{number} it's correct number!")
            



