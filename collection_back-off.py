# defaultdict: given a list of (department, employee) tuples, group employees by department. No KeyErrorchecks allowed.
from collections import defaultdict

employees = [
    ("IT", "Rahul"),
    ("HR", "Priya"),
    ("IT", "Amit"),
    ("Finance", "Neha"),
    ("HR", "Karan")
]
departments = defaultdict(list)
for department, employee in employees:
    departments[department].append(employee)

print(dict(departments))

# namedtuple: rewrite a list of (name, age, city) tuples as namedtuples. Show why p.city beats p[2].
from collections import namedtuple

Person = namedtuple("Person",["name", "age", "city"])
people = [
    ("rahul", 25, "ahmedabad"),
    ("priya", 24, "mumbai"),
    ("amit", 28, "delhi")
]
result = []
for person in people:
    p = Person(*person)
    result.append(p)

for p in result:
    print(p.name, p.age, p.city)

# deque: implement a 'last 5 searches' history. When a 6th arrives, the oldest drops off automatically.
from collections import deque
history = deque(maxlen=5)

history.append("ai")
history.append("ml")
history.append("python")
history.append("java")
history.append("html")

print(history)

history.append("javascript")

print(history)

# Counter: given two texts, find the words common to both, and which words appear in one but not the other.
from collections import Counter
text1 = "python java django machine learning"
text2 = "python django react machine learning"

words1 = text1.split()
words2 = text2.split()

counter1 = Counter(words1)
counter2 = Counter(words2)

common = counter1.keys() & counter2.keys()
only_text1 = counter1.keys() - counter2.keys()
only_text2 = counter2.keys() - counter1.keys()

print("common word:",common)
print("only in text1:",only_text1)
print("only in text2:",only_text2)