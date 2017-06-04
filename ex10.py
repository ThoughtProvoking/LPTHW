# store a string
tabby_cat = "\tI'm tabbed in."
# store a string
persian_cat = "I'm split\non a line."
# store a string
backslash_cat = "I'm \\ a \\ cat."

# store a multi-line string
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# print a string
print(tabby_cat)
# print a string
print(persian_cat)
# print a string
print(backslash_cat)
# print a string
print(fat_cat)

# ASCII bell (BEL): \a: plays the windows bell sound
# ASCII backspace (BS): \b: removes one character before then resume the rest of the string
# ASCII formfeed (FF): \f: starts new line and resumes string where it left in previous line
# \N{name}: Use names from Unicode Character Names Index
# \uxxxx: UTF-8 encoding
# \UXXXXXXXX: UTF-16 encoding (max value: 0010ffff)
# ASCII vertical tab: \v: same as ASCII formfeed
print('''
What does ASCII bell filler\astuff do ?
What about ASCII backspace filler\b\b\bstuff ?
And ASCII formfeed filler\fstuff ?
Will this show an alarm clock: \N{ALARM CLOCK} ?
Which character will show ? \u6574
What about this one ? \U000a22f1
What's a \v\v\vvertical tab ?
Octal value 245 = \245
Hex value aa = \xaa
''')
