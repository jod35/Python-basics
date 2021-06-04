from operator import mod
import modules

print(modules.name)

x=int(input("Enter x: "))
y=int(input("Enter y: "))

print(f"{x}+{y}={modules.add(x,y)}")
print(f"{x}-{y}={modules.subtract(x,y)}")
