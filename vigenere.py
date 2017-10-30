"""
Avi Stein
1 November 2016
COMP 112 - 02
Final Project: Vigenere
"""

# this is to start a timer, which will get stopped at the end of the program.
import time
start_time = time.time()

# this is a dictionary to convert between letters and their corresponding numbers.
alpha = dict()
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, len(letters)):
    alpha[letters[i]] = i

# this is the encoder I used to shift the code of lowercase letters based on a shift.
def encode(word, shift):
    strung = []
    if shift > 25:
        shift %= 26
    if shift < 0:
        shift += 26
    for i in range(0, len(word)):
        if ord(word[i]) == 0:
            new_num = ord(word[i])
        else:
            new_num = (ord(word[i]) + shift)
            if new_num > 122:
                new_num -= 26
        strung.append(chr(new_num))
    return ''.join(strung)

# this is the opposite of the above function. It just shifts it the other direction.
def decode(word, shift):
    strung = []
    if shift > 25:
        shift %= 26
    if shift < 0:
        shift += 26
    for i in range(0, len(word)):
        new_num = (ord(word[i]) - shift)
        if new_num > 122:
            new_num -= 26
        if new_num < 97:
            new_num += 26
        strung.append(chr(new_num))
    return ''.join(strung)


# this function is like the above function decode, but I undercut it by forcing it to only shift by one
# no matter what shift it is handed. This came in use later.
def deadcode(word, shift):
    strung = []
    x = shift
    shift = 1
    for i in range(0, len(word)):
        new_num = (ord(word[i]) - shift)
        if new_num > 122:
            new_num -= 26
        if new_num < 97:
            new_num += 26
        strung.append(chr(new_num))
    return ''.join(strung)


# this is a function that encrypts each word based on a given key word. This is the vigenere code in a nutshell.
def encrypt(my_word, key_word):
    vig = []
    for j in range(0,len(my_word)):
        if j >= len(key_word):
            k = j % len(key_word)
            vig.append(encode(my_word[j], alpha[key_word[k]]))
        else:
            vig.append(encode(my_word[j], alpha[key_word[j]]))
    return ''.join(vig)


# print(encrypt('abcde', 'the'))
my_word = encrypt('the', 'abcde')


# this was not actually a decryption technique, because it required knowing the answer beforehand.
# this just displayed what looked like a decryption code.
def decrypt(your_word):
    truth = 'hello world'
    vig = []
    key_length = 1
    for j in range(0, len(truth)):
        for i in range(0,26):
            my_key = i
            wiggles = decode(your_word[j],my_key)
            if wiggles == truth[j]:
                vig.append(wiggles)
            if wiggles == ' ':
                break
        print(('-' * (j - len(vig)) + ''.join(vig) + ('-' * (len(truth) - (j+1)))))
        time.sleep(.50)
    return ''.join(vig)

# print(decrypt('hello world'))


# this function searches through the entirety of the oed dictionary.
def oed_search(word):
    with open('/oeds/oed.txt', 'r') as oed:
        for line in oed:
            if line == str(word + '\n'):
                return line

#print(oed_search('bad')[0:-1])

# this function will search the oed dictionary corresponding to the length of the input word.
# It returns the word if it's in the function. It also filters out words with capital letters.
def selective_search(word, dict_length):
    n = dict_length
    with open('/oeds/oed%s.txt' % n, 'r') as oed_one:
        for line in oed_one:
            if ord(line[0]) > 122 or ord(line[0]) < 97:
                continue
            if line == str(word + '\n'):
                return word

# selective_search('bad',3)


# this function records the length of the dictionary, which helps with the statistics at the bottom.
def oed_length(a):
    k = 0
    with open('/oeds/oed%s.txt' % a, 'r') as oed_len:
        for k, l in enumerate(oed_len):
            pass
        return k + 1



# total = 0
# for i in range(1,25):
#     total += oed_length(i)
#     print(i, oed_length(i))                             # this will give the length of each oed
# print('total', total)                                   # this will give the length of all oeds (235,886)



"""
OED WORD/COMBINATION RATIO:
1: 2.0
2: 0.23668639053254437
3: 0.08079198907601275
4: 0.01153671089947831
5: 0.0008610113845399725
6: 5.731659363359934e-05
7: 2.971808281939157e-06
8: 1.4360686466042757e-07
9: 5.9679488063467305e-09
10: 2.1873369184996444e-10
11: 7.087345640776262e-12
12: 2.1442129009690993e-13
13: 6.020991355002777e-15
14: 1.5137193968704042e-16
15: 3.5325485156788945e-18
16: 7.743860004834552e-20
17: 1.5990089279019889e-21
18: 2.8562211321937173e-23
19: 5.584061047775037e-25
20: 9.935694531447316e-27
21: 1.5826086860502717e-28
22: 3.043478242404369e-30
23: 4.853576934415973e-32
24: 5.490471645266938e-34

"""




# this was my first attempt at a brute force attack, which failed because I couldn't build n-nested for loops.
# it did work on three letter words, though.

##### BRUTE FORCE ATTACK #####

def brute_force(your_word):
    global letters
    global oed
    test_word = list(your_word)
    hits = []
    combos = []
    true_hit = []
    true_combo = []
    for i in range(0,10):
        test_word = [test_word[0], test_word[1], deadcode(str(test_word[2]), i)]
        for j in range(0,10):
            test_word = [test_word[0], deadcode(str(test_word[1]), j), test_word[2]]
            for k in range(0,10):
                test_word = [deadcode(str(test_word[0]), k), test_word[1], test_word[2]]
                test_word = ''.join(test_word)
                print(test_word)
                x = oed_search(test_word)
                if x == test_word:
                    print("IT TRUE")
                    hits.append(test_word)
                    combos.append(''.join([letters[i], letters[j], letters[k]]))
    print(hits)
    print(combos)
    for i in range(0,len(hits)):
        if oed_search(combos[i]) == combos[i]:
            true_combo.append(combos[i])
            true_hit.append(hits[i])
            print("true combo: ", hits[i], combos[i])
    print(true_hit)
    print(true_combo)
    return 'yay'

#print(brute_force('the'))


test_word = list('words')

# a quick attempt a building a disjointing function to segment words for decrypting.

# for j in range(0,len(test_word)):
#     for k in range(0, 26):
#         head = test_word[:j]
#         seg = decode(test_word[j], k)
#         tail = test_word[j+1:]
#         scramble = ''.join(head + list(seg) + tail)
#         print(scramble)


# this was my attempt at nesting for loops and recursion at the same time (neither worked separately), but it also
# failed. I felt the need to keep it for documentation's sake.

def nesting(word):
    global test_word
    #print(word)
    if len(word) > 1:
        new_word = word[1:]
        nesting(new_word)
        print('up a level')
        #print(word)
        for j in range(0,5):
            change = decode(word[0], j)
            #print(word)
            over_word = ''.join(list(test_word[:-len(word)]) + list(change) + list(test_word[len(word)+2:]))
            print('over_word: ' + over_word)
            nesting(over_word[-1])
        return 'done'
    else:
        print('base level')
        for i in range(0,5):
            change = decode(word[0], i)
            print(''.join(list(test_word[:-1]) + list(change)))
        return



# this is the method that actually worked.

##### FACTORING BRUTE FORCE ATTACK #####

# this takes a really big number and breaks it down into a string of letters. Very simple, very clever.
#Thanks to Zach Berkowitz for this idea.

def factoring(number):
    r = number % 26
    q = number // 26
    if q != 0:
        x = factoring(q) + letters[r]
        return x
    else:
        return letters[r]

# this fills in extra space so a five letter word would start with "aaaaa" instead of "a".

def filling(length, factored):
    fill = 'a'*(length - len(factored))
    return fill + factored

# this gives a big number for a word in base-26. It was never used in the function, but good to understand what
# was going on.

def big_number(your_word):
    total = 0
    for i in range(0,len(your_word)):
        total += (26**((len(your_word)-1)-i))*alpha[your_word[i]]
    return total


# this is the full "brute force" attack using this factoring technique. the structure is just two for loops
# and a predicate at its basis, but gets a little more involved as you can see. There were a couple debugging
# flags I had that I ended up leaving in because they're fun and helpful to know where in the function
# it is (because it takes so long to run).

def brute_factor(your_word):
    hits = []
    keys = []
    m = len(your_word)
    for i in range(0,(26**m)-1):
        long = filling(m, factoring(i))
        print(i)
        for j in range(0,(26**m)-1):
            if j == 26:
                with open('apache.txt', 'r') as apache:
                    for line in apache:
                        subshort = line[:-1]
                        if selective_search(subshort, len(subshort)) == subshort and selective_search(long, m) == long:
                            if encrypt(long, subshort) == your_word:
                                hits.append(long)
                                keys.append(subshort)
                                print('we got a hit!')
            short = factoring(j)
            print(long, short)
            if selective_search(short,len(short)) == short and selective_search(long,m) == long:
                if encrypt(long, short) == your_word:
                    hits.append(long)
                    keys.append(short)
                    print('we got a hit!')
    for i in range(0,len(hits)):
        print(hits[i], keys[i])
    print(sorted(hits))
    print(len(hits))
    return str(hits) + ' ' + str(keys)



# this next function was somehow much easier.

##### DICTIONARY ATTACK #####

# this is the dictionary attack, which was built on the same basis of the brute force attack, but simpler.

def dictionary(word):
    hits = []
    keys = []
    m = len(word)
    for i in range(1,m+1):
        n = i
        print(i)
        with open('/oeds/oed%s.txt' % m, 'r') as oed_long:
            for lineA in oed_long:
                # print(lineA[:-1])
                if ord(lineA[0]) > 122 or ord(lineA[0]) < 97:
                    continue
                with open('/oeds/oed%s.txt' % n, 'r') as oed_short:
                    for lineB in oed_short:
                        #print(lineB[:-1])
                        if ord(lineB[0]) > 122 or ord(lineB[0]) < 97:
                            continue
                        if word == encrypt(lineA[0:-1], lineB[0:-1]):
                            hits.append(lineA[0:-1])
                            keys.append(lineB[0:-1])
    for i in range(0,len(hits)):
        print(hits[i], keys[i])
    print(sorted(hits))
    print(len(hits))
    # return str(hits)  + ' ' +  str(keys)



##### EXAMPLES TO RUN #####

# this will show what the encryption gives you back. This result gets plugged into the attack functions.
# print(encrypt('at','c'))

# this is the brute_factor attack. If you accidentally run a large word, Mx-Mc is your best friend.
# brute_factor('cv')

# this is the dictionary attack. It's much more forgiving about long words.
# dictionary('cv')

# this is an example to show the speed at which the dictionary attack can test long words.
# print(encrypt('thyroparathyroidectomize','ai'))
# dictionary('tpyzoxazabhgrwilektwmqzm')

# this function stops and returns the time from the beginning of the program until now. You can add multiple of these
# lines.
print("--- %s seconds ---" % (time.time() - start_time))

# If it’s having trouble accessing the dictionaries, double check to see if it’s pulling from the right directory.



"""
Some fun facts:

Assuming no slowdown or anything else, the brute force attack processes data at 7,551 guesses / second.

For a...
1 letter word: .09 seconds.
3 letter word: 11.8 hours.
7 letter word: 150 x the age of the universe.
10 letter word: 6.3e6 x the age of the universe.
24 letter word: 6.3e67 x the age of the universe.


The dictionary attack processes data at 261,468 guesses / second.

For a...
1 letter word: .01 seconds.
3 letter word: 8.863 seconds.
7 letter word: 1.48 hours.
10 letter word: 4.99 hours.
24 letter word: 4.5 seconds.

*24 letter words actually take ~39 seconds due to the structure of the dictionary attack.

"""