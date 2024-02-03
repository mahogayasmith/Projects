x=0

print("Hello Welcome to our Quiz Game")
name=input("What is your Name: ")
print("Ok ",name," Let's Continue")

Fq = input("1. What is the color of Apple: ")
if Fq=="Red" or "red":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Sq = input("2. Who is the founder of Apple Company: ")
if Sq=="Steve Jobs" or "steve jobs":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Tq = input("3. Answer of 3*2/3*5/10: ")
if Tq=="1":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Forq = input("4. What is latest version of windows: ")
if Forq=="Windows 11" or "windows 11" or "11":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Fiveq = input("5. Is Mint OS also a Linux: ")
if Fiveq=="Yes" or "yes":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

sixq = input("6. Say a popular online shoppoing platform: ")
if sixq=="Ebay" or "ebay" or "daraz" or "Daraz" or "Aliexpress" or "aliexpress":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Sevq = input("7. Name a color in RGB: ")
if Sevq=="Red" or "red" or "Green" or "green" or "Blue" or "blue":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Eighq = input("8. Name a best language for programming: ")
if Eighq=="java" or "python" or "c++" or "c#":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Ninq = input("9. Name a cartoon, which includes a cat as a main character: ")
if Ninq=="Garfield" or "garfield":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

Tenq = input("10. What is the latest MS Office Version: ")
if Tenq=="2022" or "2023":
    print("Yes You are correct.")
    x+=1
else:
    print("Sorry you're wrong")

print("Oh! You finished thw quiz game and next see your marks..")
input("Are you happy: ")

markss=x/10*100

print("Congratulations you got ",markss,"% Marks..")
print(" ")
input("Confirm Exit: ")
