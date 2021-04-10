d = int(input())
if d % 4 == 0 and d % 100 != 0 or d % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
