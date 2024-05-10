word = input("Введите слово: ")
count_vowels = 0
count_consonant = 0

for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += 1
    else:
        count_consonant += 1

print(f"Число согласных: {count_consonant}\nЧисло гласных: {count_vowels if count_vowels > 0 else False}")

