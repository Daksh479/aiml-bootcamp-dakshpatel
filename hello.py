# reverse a sring

def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


text = "the cat sat"

result = reverse(text)

print(result)