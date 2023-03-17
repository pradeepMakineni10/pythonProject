
# excercise:-
height = float(input("what is the height"))
weight = int(input("what is the weight"))
bmi = weight/height**2
print(round(bmi, 2))
if bmi < 1:
    print(f"you are under weight {bmi}")
elif bmi < 1.5:
    print(f"you are normal weight {bmi}")
elif bmi < 2:
    print(f"you are above average weight {bmi}")
elif bmi < 2.5:
    print(f"you are above more weight {bmi}")
elif bmi < 3:
    print(f"you are above over weight {bmi}")
else:
    print(f"you are above clinical weight {bmi}")