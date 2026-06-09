import random
def f1():
    balls=['blue','red','green','yellow']
    res=random.choice(balls)
    ch=input("enter your choice from ['blue','red','green','yellow']:")
    p=balls.count(ch)/len(balls)
    print("probability of picking",ch,'is:',p)
    if res==ch:
        return True
    else:
        return False
if f1():
    print("your choice is correct")
else:
    print("your choice is wrong") 