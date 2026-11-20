# • Find or create a text file with real prose. A few paragraphs is enough.
# • Count word frequencies by hand first: a plain dict, a loop, and .get().
# • Now do it with Counter. Compare your line counts.
# • Print the 10 most common words using most_common().
# • Notice the top words are 'the', 'a', 'and'. Filter out stopwords and rerun. Now it is interesting.

from collections import Counter
with open("sample.txt","r", encoding="utf-8") as file:
    text = file.read().lower()

words = text.split()

manual ={}
for w in words:
    manual[w] = manual.get(w, 0) + 1

counter = Counter(words)

stopwords ={
    "the", "a", "and", "is", "to"
}
filtered =[
    word for word in words
    if word not in stopwords
]
filtered = Counter(filtered)

print("Mannual resualt:",manual)
print("\nCounter result:",dict(counter))
print("\nTop 10 Words:",dict(counter.most_common(10)))
print("\nTop 10 words after removing stopwords:",filtered.most_common(10))