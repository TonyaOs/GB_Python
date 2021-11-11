#наверное, в задании имелось ввиду не это:
text = 'aaa what for'
print(text.title())

def my_title(word):
    first_small = word[0]
    first_big = chr(ord(first_small) - ord('a') + ord('A'))
    return first_big + word[1:]

print('Введите текст через пробел ')
text2 = input().split()
line = []
for word in text2:
    line.append(my_title(word))
print(' '.join(line))

