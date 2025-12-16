import random
name=input("Enter your full name: ").replace(" ","")
nums=('1234567890')
char=('!@#$%&*')   
x1=random.choice(nums)
x2=random.choice(nums)
x3=random.choice(nums)
y1=random.choice(char)
y2=random.choice(char)
z=name[0:3]
y=name[-4:-1]
password=(f"{x1}{z}{y1}{x2}{x3}{y}{y2}")
print(f"Your password is: {password}")
