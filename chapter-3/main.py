# Strings
# 1 ==> Strings are immutable
name = '''hello,
hritik,
how are you?'''

# print(name[-1])

# print(len(name))

name_short = name[0:5]

char1 = name[1]

# print(name_short)
# print(char1)

negative_slicing = name[-5:-1];

# print(negative_slicing)

# Skip Value

word = "amazing"
# print(len(word))
skipped_value = word[0:7:5]
# print(skipped_value)
count_char = word.count("g");
# print(count_char)

replace_char = word.replace("a","h");
# print(replace_char)


# Skip Sequence
a = 'riitk pathak\nbut not a bad \'boy\''

print(a)