#8.3
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(prime_nums[4])
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(friends[3])

#8.4
fruit = "banana"
print(len(fruit))

sz = len(fruit)
last = fruit[sz-1]

#8.5
ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for c in fruit:
    print(c)

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)

#8.6
s = "Pirates of the Caribbean"
print(s[0:7])
print(s[11:14])
print(s[15:24])
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(friends[2:4])

fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[3:999])

#8.7
word =("F")
if word == "banana":
    print("Yes, we have no bananas!")


if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")

#8.8
greeting = "Hello, world!"
new_greeting ="J"
print(new_greeting+greeting[1:])

#8.9
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels

print(remove_vowels("compsci"))
print(remove_vowels("aAbEefIijOopUus"))

#8.10
def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))

#8.11
def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)

print(count_a("asaasad"))

#8.12
def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(find2("banana", "a", 3))