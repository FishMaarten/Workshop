import creature
name = input("Name your dog : ")
try:
    dog = creature.Dog(name)
    print(f"Created {dog.name}")
except: print("Failed to create, Dog not found")

try: dog.bark()
except: print("Failed to speak, bark() not found")
