import re

text = "ranjini *(^#$2)@#! T @!#877645438"

# Remove junk characters first, then remove spaces
cleaned = re.sub(r'[^A-Za-z0-9\s]', '', text)
result = re.sub(r'\s+', '', cleaned)

print(result)
