#Задача 1
str = str(input())
word = 0 #длина слова
longest = 0 #длина самого длинного слова
a = 0 #1-й индекс слова
for i in range(len(str)):
    if str[i] != ' ':
        word += 1
    elif word > longest:
        longest = word
        a = i - longest
        word = 0
print('самое длинное слово в строке:', str[a: a + longest])


#Задача 2
#вариант 1
str = str(input())
while str[0] == ' ':
    str = str[1:]
while str[len(str)-1] == ' ':
    str = str[:-1]
i=0
while i < (len(str) - 1):
    if str[i] == ' ' and str[i + 1] == ' ':
        str = str.replace(str[i]+str[i+1], ' ')
    else:
        i += 1
print('Нормированая строка:', str)

#вариант 2
str = str(input())
for i in range(len(str)):
    if str[0] == ' ':
        str = str[1:]
    if str[len(str)-1] == ' ':
        str = str[:-1]
i=0
while i < (len(str) - 1):
    if str[i] == ' ' and str[i + 1] == ' ':
        str = str.replace(str[i]+str[i+1], ' ')
    else:
        i += 1
print('Нормированная строка:', str)


#дополнительная задача
str = str(input())
words = 0
word = 0
for i in range(len(str)):
    if str[i] != ' ' and word == 0:
        words += 1
        word = 1
    elif str[i] == ' ':
            word = 0
print('в строке', words, 'слов')


