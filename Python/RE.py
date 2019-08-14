
## Regular expressions module provides regular expression matching operations.
# Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes).

## Import re module
import re

## prepare a text and file to used
sentence = 'This is regular expressions course'
text1 = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Bob
Mr Tom
Ms Bryan
Mrs. Robinson
Mr. X
'''

text2 = '''
https://www.google.com
http://facebook.com
https://youtube.com
https://www.nasa.gov
'''

text3 = '''
user@gmail.com
my_university_email@university.edu
work-email-456@my-work.net
'''

## Metacharacters
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

## re.compile >> Compile a regular expression pattern into a regular expression object, which can be used for matching.
pattern = re.compile(r'abc')

## re.finditter >> Return an iterator yielding match objects over all non-overlapping matches for the RE pattern in string
matches = pattern.finditer(text1)

## Print all the matches objects
for match in matches :
    print(match)

print()

## Deal with metacharacters (line 48)
# False
# pattern = re.compile(r'.')
# matches = pattern.finditer(text1)
# for match in matches :
#     print(match)

# True
pattern = re.compile(r'\.')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

pattern = re.compile(r'user@gmail\.com')
matches = pattern.finditer(text3)
for match in matches :
    print(match)

print()

## Find matches objects inside a file
with open('additionals/RE_Data.txt', 'r') as f :
    contents = f.read()

    pattern = re.compile(r'Bruce')
    matches = pattern.finditer(contents)
    for match in matches :
        print(match)

print()

## Find a characters with some specefic patterns
# 1
print('1')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

# 2
print('2')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

# 3
print('3')
pattern = re.compile(r'\d\d\d[^*]\d\d\d[^*]\d\d\d\d')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

# 4
print('4')
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

# 5
print('5')
with open('additionals/RE_Data.txt', 'r') as f :
    contents = f.read()
    pattern = re.compile(r'\d\d\d[^*]\d\d\d[^*]\d\d\d\d')
    matches = pattern.finditer(contents)
    for match in matches :
        print(match)

# 6
print('6')
with open('additionals/RE_Data.txt', 'r') as f :
    contents = f.read()
    pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
    matches = pattern.finditer(contents)
    for match in matches :
        print(match)

# 7
# Mr. Bob
# Mr Tom
# Ms Bryan
# Mrs. Robinson
# Mr. X
print('7')
pattern = re.compile(r'M(r|rs|s)\.?\s[a-zA-Z]\w*')
matches = pattern.finditer(text1)
for match in matches :
    print(match)

# 8
# https://www.google.com
# http://facebook.com
# https://youtube.com
# https://www.nasa.gov
print('8')
pattern = re.compile(r'https?://(www)?\.?\w+\.(com|gov)')
matches = pattern.finditer(text2)
for match in matches :
    print(match)

# 9 Make it into group and print the group
print('9')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text2)
for match in matches :
    print(match.group(1), match.group(2), match.group(3))

# 10
# user@gmail.com
# my_university_email@university.edu
# work-email-456@my-work.net
print('10')
pattern = re.compile(r'([a-zA-Z0-9.-])+@([a-zA-Z0-9.-])+\.([a-zA-Z0-9.-])+')
matches = pattern.finditer(text3)
for match in matches :
    print(match)

# 11 Make it into group and print the group
print('11')
pattern = re.compile(r'([a-zA-Z0-9.-]+)(@\w+[-]?[\w]+)(\.\w+)')
matches = pattern.finditer(text3)
for match in matches :
    print(match.group(1), match.group(2), match.group(3))

## re.sub() >> Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.sub(r'\2\3', text2)
print(matches)

## findall() >> Return all non-overlapping matches of pattern in string, as a list of strings
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
matches = pattern.findall(text1)
print(matches)

print()

## match() >> If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object
pattern = re.compile(r'This')
matches1 = pattern.match(sentence)
print(matches1)

pattern = re.compile(r'regular')
matches2 = pattern.match(sentence)
print(matches2)

print()

## search() >> Scan through string looking for the first location where the regular expression pattern produces a match
pattern = re.compile(r'regular')
matches = pattern.search(sentence)
print(matches)

print()

## re.IGNORECASE >> Perform case-insensitive matching
pattern = re.compile(r'm(r|rs|s)\.?\s[a-z]\w*', re.IGNORECASE)
matches = pattern.finditer(text1)
for match in matches :
    print(match)

print()

# or
with open('additionals/RE_Data.txt', 'r') as f :
    contents = f.read()
    pattern = re.compile(r'BARRY', re.I)
    matches = pattern.findall(contents)
    print(matches)
