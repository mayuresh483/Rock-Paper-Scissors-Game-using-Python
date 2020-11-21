import random
count1 = 0
count2 = 0
n = 1
a = input("Enter player Name ==> ")
print("Welcome ", a)
print("--------------------------------")
rounds = int(input("Enter number of rounds ==> "))
while n <= rounds:
        print("Select your Choice 1 : Rock , 2 : Paper, 3 : Scissor")
        x = int(input("Enter input number "))
        if x == 1:
            x_name = 'Rock'
        if x == 2:
            x_name = 'Paper'
        if x == 3:
            x_name = 'Scissor'
        if x >= 4:
            print("Invalid Value Please Enter the correct Value ")
            continue
        print('Your choice is ==> ', x_name)
        comp = random.randint(1,3)
        if comp == 1:
            comp_name = 'Rock'
        if comp == 2:
            comp_name = 'Paper'
        if comp == 3:
            comp_name = 'Scissor'
        print("Computer Choice is ==> ", comp_name)
        print(x_name + " V/s " + comp_name)
        while True:
            if(x == 1 and comp == 2) or (x == 2 and comp == 1):
                print("Paper Wins ==> ")
                result = "Paper"
            elif (x == 1 and comp == 3) or (x == 3 and comp == 1):
                print("Rock Wins ==> ")
                result = "Rock"
            elif x_name == comp_name:
                print("Tie")
                result = "Tie"
            else:
                print("Scissor wins ==>")
                result = "Scissor"
            if result == "Tie":
                print("<==Game is Tie ==>")
                n -= 1
            elif result == x_name:
                print("<== " + a + " wins ==>")
                count1 += 1
            else:
                print("<== Computer Wins ==>")
                count2 += 1
            n += 1
            break
print("---------------------------------")
print("Final Score")
if count1 > count2:
    print(a + " Wins by ",count1,"-",count2)
else:
    print("Computer Wins by ",count2,"-",count1)




