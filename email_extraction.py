# Extract every email address using re.findall.
import re
text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these'''

email = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}\b"
emails = re.findall(email, text)
print(emails)

# Extract every phone number too. Indian formats vary — handle at least two.
import re
text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these'''

phone = r"(?<!\d)(?:\+91[- ]?|0)?[6-9]\d{4}[- ]?\d{5}(?!\d)"
phones = re.findall(phone, text)
print(phones)

# Use a capture group to split each email into username and domain separately.
import re
text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these'''

pattern = r"\b([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,})\b"
result = re.findall(pattern, text)
for username, domain in result:
    print("Username:", username)
    print("Domain:", domain)
    print()

#  Count how many emails belong to each domain using Counter.
import re
from collections import Counter
text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these'''

pattern = r"\b([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,})\b"
result = re.findall(pattern, text)
domains = [domain.lower() for username, domain in result]
domain_count = Counter(domains)

print(domain_count)