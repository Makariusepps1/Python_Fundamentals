# Author: Makarius Epps
# Presidents List: displays the first N U.S. presidents with an asterisk
# next to any president whose last name starts with A.

presidents = [
    ("George Washington", "1789-1797"),
    ("John Adams", "1797-1801"),
    ("Thomas Jefferson", "1801-1809"),
    ("James Madison", "1809-1817"),
    ("James Monroe", "1817-1825"),
    ("John Quincy Adams", "1825-1829"),
    ("Andrew Jackson", "1829-1837"),
    ("Martin Van Buren", "1837-1841"),
    ("William Henry Harrison", "1841"),
    ("John Tyler", "1841-1845"),
]

while True:
    try:
        count = int(input("How many presidents would you like to see (1-10)? "))
        if 1 <= count <= 10:
            break
        print("Please enter a number between 1 and 10.")
    except ValueError:
        print("That wasn't a number. Please enter a whole number.")

print("For loop:")
asterisk_count = 0
for name, term in presidents[:count]:
    if name.split()[-1].startswith("A"):
        print(f"{name}* - {term}")
        asterisk_count += 1
    else:
        print(f"{name} - {term}")
print(f"{asterisk_count} president(s) have a last name starting with A.")

print("While loop:")
i = 0
while i < count:
    name, term = presidents[i]
    if name.split()[-1].startswith("A"):
        print(f"{name}* - {term}")
    else:
        print(f"{name} - {term}")
    i += 1