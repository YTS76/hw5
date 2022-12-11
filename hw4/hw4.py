from random import randint
import random
k=0
l=0
p=0
i=0
choice=['+','-']
choice1=['*']
choice2=['/']
t=int(float(input("pick the difficulty level: ")))
for i in range(4):
    r=random.choice(choice)
    j=random.choice(choice1)
    m=random.choice(choice2)
    A=randint(1,10)
    B=randint(1,9)
    if t==1:
     print(f"{A}{r}{B}")
     a=int(float(input("")))
    if t==2:
     print(f"{A}{j}{B}{r}{A}")
     a=int(float(input("")))
    if t==3:
     print(f"{A}{m}{B}{j}{A}{r}{B}^2")
     a=int(float(input("")))
    if a==A+B or a==A/B+A or a==A*B-A or a==A*B*A*B or a==A/B-A+A or a==A/B+A/B**2 or a==A-B or a==A*B+A or a==A/B*A+B**2 or a==A/B*A-B**2:
     print("Correct!")
     l+=1
    else:
     print("Wrong!")
     k+=1
    p+=1
s=l/p*100
if s<=59:
    score="score 2"
elif s>=60 and s<=74:
    score="score 3"
elif s>=75 and s<=89:
    score="score 4"
elif s>=90:
    score="score 5"
print(score)
