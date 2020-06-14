import creature
name = input("Name your fish : ")
try:
    fish = creature.Fish(name)
    print(f"Create {fish.name}")
except: print("Failed to create, Fish not found")

try: fish.blub()
except: print("Failed to speak, blub() not found")
