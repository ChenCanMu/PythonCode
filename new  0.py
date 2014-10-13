x = int(input("Please enter an integer:"))

if x < 2:
    x = 2
    print("Negative changed to two")
elif 2<= x <= 3:
    print("two or three")
elif x == 4:
    print("four")
else:
    print("more than five")