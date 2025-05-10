import random


def love_calculator(name1,name2):
    
    love_score = random.randint(50,100)

    print(f"love_score for {name1} & {name2} : {love_score}% ")

    if love_score >=85 :
        print(" WOW! you have a perfect match! ")

    elif love_score >= 70 :
        print("you have a stong relationship")

    elif love_score >=50:
        print("there is a potential love")

    else:
        print("It's a complicated....but who knows..")   


name1 = input("enter the first name:  ")    

name2 = input("enter the second name" )


love_calculator(name1,name2)             


