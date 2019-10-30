#  File: Reducible.py

#  Description: Print a list of reducable words from a dictionary

#  Student Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/25/2019

#  Date Last Modified: 10/29/2019


# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


def nxt_prime(n):
  # base case
    if n <= 1:
        return 2
    prime = 2 * n
    found = False
  # loop continously until is_prime() returns True for a number greater than n
    while not found:
        prime += 1
        if is_prime(prime):
            found = True
    return prime


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hash_idx = 0
    for i in range(len(s)):
        letter = ord(s[i]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size(s, const):
    hash_val = 0
    pow26 = 1
    for i in range(len(s) - 1, -1, -1):
        letter = ord(s[i]) - 96
        hash_val += pow26 * letter
        pow26 *= 26
    return const - (hash_val % const)


# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    hash_index = hash_word(s, len(hash_table))
    if hash_table[hash_index] == '':
        hash_table[hash_index] = s
    else:
        step = step_size(s, 13)
        hash_index = (hash_index + step) % len(hash_table)
        while hash_table[hash_index] != '':
            hash_index = (hash_index + step) % len(hash_table)
        hash_table[hash_index] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    word_index = hash_word(s, len(hash_table))
    index = 0

    if hash_table[word_index] == s:
        return True

    elif hash_table[word_index] == '':
        return False

    else:
        step = step_size(s, 13)
        index = (word_index + step) % len(hash_table)
        while index != word_index:
            if hash_table[index] == s:
                return True
            elif hash_table[index] == '':
                return False
            else:
                index = (index + step) % len(hash_table)
    return False


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def reducible(s, hash_table, hash_memo):
    candidates = [s]
    while len(candidates) > 0:
        word = candidates[0]
        if word == '':
            return True
        for i in range(len(word)):
            # if word[:i] + word[:i + 1] in hash_table:
            if find_word(word[:i] + word[:i + 1], hash_table):
                hash_memo.append(word)
                return True
            else:
                return False


def removing_one(s, hash_table):
    words = []
    for i in range(len(s)):
        child = s[:i] + s[i + 1:]
        if find_word(child, hash_table):
            words.append(child)

    return words


def is_reducible(s, hash_table, hash_memo):
    if 'a' not in s and 'i' not in s and 'o' not in s:
        return False
    if len(s) == 2:
        if 'a' in s or 'i' in s or 'o' in s:
            hash_memo.append(s)
            return True
    for word in removing_one(s, hash_table):
        return is_reducible(word, hash_table, hash_memo)

    return False


# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    max_length = len(string_list[0][0])

    for new_word in string_list:
        max_length = max(max_length, len(new_word[0]))

    longest_strings = []

    for words in string_list:
        if len(words[0]) == max_length:
            longest_strings.append(words[0])

    longest_strings.sort()
    return longest_strings


def main():
    # import time
    # start = time.time()
  # create an empty word_list
    word_list = []

  # open the file words.txt
    file = open('words.txt', 'r')

  # read words from words.txt and append to word_list
    for line in file:
        line = line.split()
        word_list.append(line)

  # close file words.txt
    file.close()

  # find length of word_list
    word_list_len = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
    N = nxt_prime(word_list_len * 2)
    # print(N)
  # create and empty hash_list
    hash_list = []

  # populate the hash_list with N blank strings
    for i in range(0, N):
        hash_list.append('')

  # hash each word in word_list into hash_list
  # for collisions use double hashing
    for word in word_list:
        insert_word(word[0], hash_list)

  # create an empty hash_memo
    hash_memo = []

  # populate the hash_memo with M blank strings
    M = 27000
    while not is_prime(M):
        M += 1
    # print(M)
    for i in range(0, M):
        hash_memo.append('')
  # create and empty list reducible_words
    reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word[0], hash_list, hash_memo):
            reducible_words.append(word)

  # find words of the maximum length in reducible_words
    max_words = []
    max_words.append(get_longest_words(reducible_words))


  # print the words of maximum length in alphabetical order
  # one word per line
    for words in max_words:
        print(words[0])

    # print('It took', time.time()-start, 'seconds.')

# This line above main is for grading purposes. It will not
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
