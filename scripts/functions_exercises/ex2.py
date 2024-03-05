def count_occurrences(word: str, char: str) -> int:
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count

print(count_occurrences(word='Hello World', char='l'))


def count_occurrences_2(word: str, char: str) -> int:
    return sum(1 for letter in word if letter == char)

print(count_occurrences_2(word='Hello World', char='z'))