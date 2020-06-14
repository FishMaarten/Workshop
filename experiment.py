import creature
name = input("Name your cat : ")
try:
    cat = creature.Cat(name)
    print(f"Created {cat.name}")
except: print("Failed to create, Cat not found")

try: cat.miao()
except: print("Failed to speak, miao() not found")
