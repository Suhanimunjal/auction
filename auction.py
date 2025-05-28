import time
import os

print("""
  ____  _     _           _     _             _             
 | __ )(_) __| | ___ _ __(_)___(_) ___  _ __ | | _____ _ __ 
 |  _ \| |/ _` |/ _ \ '__| / __| |/ _ \| '_ \| |/ / _ \ '__|
 | |_) | | (_| |  __/ |  | \__ \ | (_) | | | |   <  __/ |   
 |____/|_|\__,_|\___|_|  |_|___/_|\___/|_| |_|_|\_\___|_|   
                                                          
""")

d = {}
while True:
    n = input("Enter name: ")
    b = int(input("Enter bid amount: $"))
    d[n] = b
    more = input("Add another bidder? (y/n): ")
    if more != 'y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')

print("\nCalculating winner", end='')
for _ in range(3):
    time.sleep(0.5)
    print('.', end='')

m = max(d, key=d.get)
print(f"\n\n🏆 The winner is **{m}** with a bid of ${d[m]}! 🥇")
