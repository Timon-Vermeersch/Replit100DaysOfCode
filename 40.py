#https://www.youtube.com/watch?v=TkKsEq6ODNs
uName = input("Name?: ")
uAge = input("Age?: ")
uDob = input("Date of birth?: ")
uTell = input("Telephone nr?: ")
uMail = input("Mail adress?: ")
uAdress = input("Adress?: ")

user = {"name": uName, "age" : uAge, "DateofBirth"
         : uDob, "Telephone number": uTell, 
         "Email" : uMail, "Adress" :uAdress}
print(f"\nHere's your contact info:\n\nName: {user['name']}\nAge: {user['age']}\nDoB: {user['DateofBirth']}\nTelly: {user['Telephone number']}\nEmail: {user['Email']}\nadress: {user['Adress']}\n")