dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
if input() in dictionary:
    print("Correct")
else:
    print("Incorrect")

print("Hello! My name is Aid.")
print("I was created in 2020.")
print("Please, remind me your name.")
user_name = input("")
print("What a great name you have, " + user_name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7")
remainder3 = input()
remainder5 = input()
remainder7 = input()
your_age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is " + str(your_age) + " ; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
user_n = int(input())
n = 0
while n <= user_n:
    print(str(n) + ' !')
    n += 1
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while True:
    answer = input()
    correct = "2"
    if answer == correct:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        exit()
    else:
        print("Please, try again.")

        number = int(input())
        end_count = number + 1

        # read a number and count to it here
        p = 0
        while (p != end_count):
            print("{}!".format(p))
            p = p + 1
            if p == (end_count):
                break
