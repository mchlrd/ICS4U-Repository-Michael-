angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

angle_sum = angle3 + angle1 + angle2

if not(angle_sum == 180):
    print("Error")
elif angle1 == angle2 == angle3:
    print("Equilateral")
elif angle1 != angle2 and angle2 != angle3 and angle1 != angle3:
    print("Scalene")
else:
    print("Isosceles")  