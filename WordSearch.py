#  File: WordSearch.py

#  Description: Take a word search from a file, find the words, output to a file with the word and its position.

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/13/19

#  Date Last Modified: 9/16/19


# reverses the word
def reverse_string(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverse_string(word[:-1])


# finding all words
def find_words(origional, found_words, dimensions):
    h = int(dimensions[0])
    w = int(dimensions[1])

    # horizontal
    ws = origional[:]

    for word in found_words:
        for i in range(h):
            position = ws[i].find(word)
            if position >= 0:
                found_words[word] = (i + 1, position + 1)
                continue
            reverse_position = ws[i].find(reverse_string(word))
            if reverse_position >= 0:
                found_words[word] = (i + 1, reverse_position + len(word))

    ws = []

    for i in range(w):
        a = []
        for j in range(h):
            a.append(origional[j][i])
        ws.append(''.join(a))

    # verticals
    for word in [x for x in found_words if found_words[x] == (0, 0)]:
        for i in range(w):
            position = ws[i].find(word)
            if position >= 0:
                found_words[word] = (position + 1, i + 1)
            else:
                reverse_position = ws[i].find(reverse_string(word))
                if reverse_position >= 0:
                    found_words[word] = (reverse_position + len(word), i + 1)

    # diagonals
    ws = origional[:]

    for word in [x for x in found_words if found_words[x] == (0, 0)]:
        word_length = len(word)
        for i in range(h - word_length):
            for j in range(w - word_length):
                for x in range(word_length):
                    if x == word_length - 1:
                        if word[x] == ws[i + x][j + x]:
                            found_words[word] = (i + 1, j + 1)
                    elif word[x] == ws[i + x][j + x]:
                        continue
                    else:
                        break

        for i in range(word_length - 1, h):
            for j in range(w - word_length):
                for x in range(word_length):
                    if x == word_length - 1:
                        if word[x] == ws[i - x][j + x]:
                            found_words[word] = (i + 1, j + 1)
                    elif word[x] == ws[i - x][j + x]:
                        continue
                    else:
                        break

    # reverse diagonals
    for word in [x for x in found_words if found_words[x] == (0, 0)]:
        reverse_word = reverse_string(word)
        word_length = len(word)

        for i in range(h - word_length):
            for j in range(w - word_length):
                for x in range(word_length):
                    if x == word_length - 1:
                        if reverse_word[x] == ws[i + x][j + x]:
                            found_words[word] = (i + word_length, j + word_length)
                    elif reverse_word[x] == ws[i + x][j + x]:
                        continue
                    else:
                        break

        for i in range(word_length - 1, h):
            for j in range(w - word_length + 1):
                for x in range(word_length):
                    if x == word_length - 1:
                        if reverse_word[x] == ws[i - x][j + x]:
                            found_words[word] = (i - word_length + 2, j + word_length)
                    elif reverse_word[x] == ws[i - x][j + x]:
                        continue
                    else:
                        break

    return found_words


def main():

    try:
        f = open('hidden.txt', 'r')
        output = open('found.txt', 'w')
    except IOError:
        print("Unable to read file.\n\n")
        exit()

    # put info from file into list
    dimensions = f.readline().split()
    line_count = int(dimensions[0])
    f.readline()

    ws = []
    for line in range(line_count):
        ws.append(f.readline().rstrip('\n').upper().replace(' ', ''))

    f.readline()
    word_count = int(f.readline())

    # dictionary to put words found into
    found_words = []
    for line in range(word_count):
        found_words.append(f.readline().rstrip('\n').upper())
    found_words = dict((x, (0, 0)) for x in found_words)

    have_found = find_words(ws, found_words, dimensions)

    for i in found_words:
        output.write('%-12s%5s%6s\n' % (i, have_found[i][0], have_found[i][1]))

    f.close()
    output.close()


main()
