import sys
import math

def test(did_Pass):
    lintenum = sys._getframe(1).f_lineno
    if did_Pass:
        mag = "Test at line (0) ok".format(lintenum)
    else:
        mag = ("Test at line (0) wrong").format(lintenum)
    print(mag)

aa = "Python atrings have some interesting methods"
if (aa.find("have"))>=0:
    print("have is in the string")
else:
    print("no have")
print(aa.find("have"))

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    s_sans_punct= ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct
str = 'well, I never did!", sa<id >Alice.'
my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

wds = remove_punctuation(my_story).split()
print(wds)

words = remove_punctuation(my_story).split()
print(remove_punctuation(str))

king = "Arthur"
knight="Shell"

s1 = "{0} His name is {1}!".format(knight,king)
print(s1)

print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t", i**10, "\t", i**20)

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
