text = input("Введите текст: ")
words = text.split()
freq = {word: words.count(word) for word in words}
most_common = max(freq, key=freq.get)
longest_word = max(words, key=len)
print(f"Самое частое слово: {most_common}")
print(f"Самое длинное слово: {longest_word}")