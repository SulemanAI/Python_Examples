eng = int(input("Enter the English Number: "))
urdu = int(input("Enter the Urdu Number: "))
maths = int(input("Enter the Maths Number: "))
sci = int(input("Enter the Science Number: "))
sst = int(input("Enter the S.St Number: "))
Isl = int(input("Enter the Islamiat Number: "))
comp = int(input("Enter the Computer Number: "))
fre = int(input("Enter the French Number: "))

obt_marks = (eng + urdu + maths + sci + sst + Isl + comp + fre)
print(f" Your obtained marks is: {obt_marks}")
# obt_marks=int(input("Enter 639"))

total_marks = int(input("Enter the Total Marks: "))

percentage = (obt_marks / total_marks) * 100
print(f"\n Your total percentage is: {percentage}%")

if percentage > 80:
    print("Congratulations! You got an A+ Grade.")
elif 70 <= percentage < 80:
    print("Excellent! You got an A Grade.")
elif 60 <= percentage < 70:
    print("Good! You got an B Grade.")
elif 50 <= percentage < 60:
    print("Be Better! You got an C Grade.")
else:
    print("Bad! You failed.")


