LETTER_SCORES = {chr(n): n - ord("A") + 1 for n in range(ord("A"), ord("Z") + 1)}

triangles = [1]


def word_score(word):
    return sum(LETTER_SCORES[letter] for letter in word)


def is_triangle(i):
    global triangles

    while triangles[-1] < i:  # calculate triangles
        n = len(triangles) + 1
        triangles.append(int(n * (n + 1) / 2))

    return i in triangles


words = []

with open("0042_words.txt") as f:
    words = f.read().replace('"', "").split(",")

triangle_words = [
    (word, word_score(word)) for word in words if is_triangle(word_score(word))
]

print(triangle_words)
print(len(triangle_words))
