a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print("Normal")
if h > b:
    print("Excess")
if h < a:
    print("Deficiency")




