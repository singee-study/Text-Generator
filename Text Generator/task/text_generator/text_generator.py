import random

from nltk.tokenize import regexp_tokenize


def is_end(c):
    return c == '.' or c == '!' or c == '?'


def is_first_word(token: str):
    if not token[0].isupper():
        return False
    if is_end(token[-1]):
        return False

    return True


def is_last_word(token: str):
    return is_end(token[-1])


if __name__ == '__main__':
    filename = input()

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    tokens = regexp_tokenize(text, r'[^\n\t ]+')

    trigrams = {}

    for i in range(len(tokens) - 2):
        head = (tokens[i], tokens[i+1])
        tail = tokens[i + 2]

        if head not in trigrams:
            trigrams[head] = {}

        if tail in trigrams[head]:
            trigrams[head][tail] += 1
        else:
            trigrams[head][tail] = 1

    first_words = [t for t in trigrams if is_first_word(t[0])]

    count = 0
    while count < 10:
        words = list(random.choice(first_words))

        while not is_last_word(words[-1]):
            pair = (words[-2], words[-1])
            if pair not in trigrams:
                words = None  # invalid
                break

            keys = list(trigrams[pair].keys())
            values = [trigrams[pair][k] for k in keys]
            word = random.choices(keys, weights=values)[0]
            words.append(word)

        if words and len(words) > 5:
            print(' '.join(words))
            count += 1
