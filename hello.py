import random
print("じゃんけん開始 /n 0=グー,1=チョキ,2=パー")

def syouhai(a: int, i: int):
    if(a == i):
        print("あいこで...")
        return(0)
    elif(i == 0 and a == 2):
        print("you win")
        return(2)
    elif(i == 2 and a == 0):
        print("you lose")
        return(1)
    elif(i < a):
        print("you lose")
        return(1)
    elif(a < i):
        print("you win")
        return(2)

end=0
while(end == 0):
    a = int(input())
    i = random.randint(1,300)
    print("君:{} 相手:{}".format(a,i%3))
    end = syouhai(a, i%3)