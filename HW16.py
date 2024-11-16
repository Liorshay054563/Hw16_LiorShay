#start
#1
##A
import random
import statistics



cities : list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
#a:
print(sorted(cities, key=lambda c: (len(c),c))) #sort from the shortest to the longest
#b
print(sorted(cities, key=lambda c: len(c.split()))) #sort by len of words
#c
print(sorted(cities, key=lambda c: c[-1])) #sort by the last letter
#d
print(sorted(cities, key=lambda c: c[:-1])) #sort by the uposite word
#e
print(sorted(cities, key=lambda c: c.lower().count('a'))) #sort by the number of times with "a"
#f
# cities.append(["Tokyo",5760,"asia"])
# print(cities)

##B
l_random100: list[int] = [random.randint(1,101) for _ in range(50)]
print(l_random100)
#1
print(sorted(l_random100, key=lambda n: n))
#2
print(sorted(l_random100, key=lambda n: statistics.mean(l_random100)))

###2 Dict
text = ("This chocolate cake is rich, moist,"
        " and full of delicious chocolate flavor To make the cake, "
        "you will need chocolate, flour, sugar, eggs, and butter After "
        "baking the chocolate cake, let the cake cool before adding the chocolate frosting.")
words_dict: dict[str,int] = dict()
words = text.split()
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

print(words_dict)
sort_d = sorted(words_dict.items(),key= lambda n: n[1])
max_val = sort_d[::-1]
print(f"The word {max_val[0]},{max_val[1]} showed the max")

#b
letter_dict: dict[str,int] = dict()
letters = [letter for letter in text if letter !=" "]
for letter in letters:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

print(words_dict)
sort_d = sorted(letter_dict.items(),key= lambda n: n[1])
min_val = sort_d[0]
print(f"The letter {min_val[0]},{min_val[1]} showed the min")

#3
#
hezka_3: dict[int, int] = {}

for i in range(1, 21):
    hezka_3[i] = i ** 3

print(hezka_3)

user_input = int(input("Enter number between 1-20: "))

if user_input in hezka_3:
    print(f"The result of {user_input} **3 = {hezka_3[user_input]}")
else:
    print("not in the range")