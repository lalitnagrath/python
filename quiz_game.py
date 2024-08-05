
print("welcome to my QuiZ!")
playing = input("do you want to play? ")

if playing !="yes" :
    print("Bye bye")
    quit()

print("good.let's play")
score=0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print("correct ")
    score = score +1

else:
    print("Incorrect answer")

answer = input("what does RAM stand for? ")
if answer == "random acess memory":
    print("correct ")
    score = score +1

else:
    print("Incorrect answer")
    

answer = input("what does gpu stand for? ")
if answer == "graphics processing unit":
    print("correct ")
    score = score +1

else:
    print("Incorrect answer")


answer = input("what does USB stand for? ")
if answer == "universal serial bus":
    print("correct ")
    score = score +1
    print("Your score is " + str(score))

else:
    print("Incorrect answer")
