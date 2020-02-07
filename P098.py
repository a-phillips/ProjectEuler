"""By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a
different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, find all the square
anagram word pairs (a palindromic word is NOT considered to be an anagram
of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

Answer: 18769
Time: 3.5s
"""


import time

def same_form(string, num):
    match = {}
    str_num = str(num)
    for i in xrange(len(string)):
        if match.get(string[i], str_num[i]) != str_num[i]:
            return False
        match[string[i]] = str_num[i]
        if match.values().count(str_num[i]) > 1:
            return False
    return match   

def check_pair(angram, num):
    match = same_form(angram[0], num)
    if match:
        check_square = 0
        mult = 1
        for i in xrange(len(angram[1])-1, -1, -1):
            check_square += (int(match[angram[1][i]])*mult)
            mult *= 10
        if check_square**.5 == int(check_square**.5):
            if len(str(check_square)) == len(angram[1]):
                return max(num, check_square)
        return 0
    
def run():
    t0 = time.time()
    file_path = 'C:\Documents and Settings\zq5586\Desktop\Personal\Coding\words.txt'
    with open(file_path, 'r') as raw_file:
        words = raw_file.read().replace('"', '').split(',')
    angrams = [('care', 'race')]
    for i in xrange(len(words)-1):
        for j in xrange(i+1, len(words)):
            word1 = list(words[i])
            word2 = list(words[j])
            if len(word1) == len(word2):
                for letter in word1:
                    if word2.count(letter) != word1.count(letter):
                        break
                else:
                    angrams.append((word1, word2))

    squares = {2: [],
               3: [],
               4: [],
               5: [],
               6: [],
               7: [],
               8: [],
               9: []}
    for i in xrange(4, 10001):
        num = i**2
        squares[len(str(num))].append(num)
    max_num = 0
    for angram in angrams:
        for square in squares[len(angram[0])]:
            check_num = check_pair(angram, square)
            if check_num > max_num:
                max_num = check_num
    print time.time()-t0
    print max_num
            
if __name__ == '__main__':
    run()


