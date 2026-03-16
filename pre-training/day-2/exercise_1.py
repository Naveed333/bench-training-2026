import string


def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


paragraph = """
Python is a versatile programming language. Python is used for web development,
data science, artificial intelligence, and more. Many developers love Python because
Python is easy to learn and Python has a large community. The Python community is
very welcoming and Python documentation is excellent.
"""

freq = word_frequency(paragraph)
top_5 = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:5]

print("Top 5 most common words:",string.punctuation)
for word, count in top_5:
    print(f"  {word}: {count}")
