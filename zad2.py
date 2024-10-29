x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if x > y:
    y,x = x, y
    if x > z: 
        z, x = x, z

print(f"{x}, {y}, {z}")