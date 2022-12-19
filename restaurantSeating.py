prompt = "In order for us to find you a table, we will need to know how many people are in your group."
prompt += "\n Please enter the number of people you would like to seet."
table = int(input(prompt ))
if table <= 8:
    print(f"There is currantly a table available with {table} seats. You may be seated.")
else:
        print(f"Currently, we do not have a table with {table} seats. Please wait for another table to open up.")
        