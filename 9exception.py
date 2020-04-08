try:
    age= int(input("age : "))
    income=200
    risk=income/age
    print(age)
except ValueError:
    print("invalid value.")
except ZeroDivisionError:
    print("Age cant be 0.")
