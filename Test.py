
text = """MATCHING
DATA
‒‒‒‒‒"""

Matching = "MATCHING"

text = text.strip()


print(text)

if Matching in text:
    text = "MATCHING"
    print(text)


if ratio(text, Matching) >= 0.75:
    print("A")
else:
    print("B")