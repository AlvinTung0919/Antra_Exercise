

name = input("What is ur name")
place = input("Where do you live")
personal = input("Describe yourself")


with open("personal_details.txt", "w") as file:
    file.write("Your Personal Details\n")
    file.write("=====================\n")
    file.write(f" My name is {name}\n")
    file.write(f"Location: {place}\n")
    file.write(f"Personal Detail: {personal}\n")