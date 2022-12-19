prompt = "This program tells you whether your number is a multiple of 10."
prompt += "\n Please enter a number:"
num = int(input(prompt ))
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")