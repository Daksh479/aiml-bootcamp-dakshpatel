# counts how many times each word appears in a sentence

def count(sentence):
    words = sentence.lower().split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


text = "return a dict"

result = count(text)

print(result)