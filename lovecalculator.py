print("Welcome to love calculator")
name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))

concat_name = name1 + name2
concat_name = concat_name.lower()

t = concat_name.count("t")
r = concat_name.count("r")
u = concat_name.count("u")
e = concat_name.count("e")

true = t + r + u + e
l = concat_name.count("l")
o = concat_name.count("o")
v = concat_name.count("v")
e = concat_name.count("e")

love = l + o + v + e

score = int(str(true)+str(love))

if score > 85 or score < 10:
   print(f"Your score is {score}, you are like cake and cherry")
elif score >= 40 and score <= 70:
   print(f"Your score is {score} , you look good.")
else:
   print(f"Your score is {score}")
