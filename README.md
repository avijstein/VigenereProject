# VigenereProject

For COMP 112, the final project was fairly open ended, allowing us to build tic-tac-toe or anything else. I had read a book about the Vigenere cipher a while ago, and how this very simple algorithm was used as a secure encryption method for a long time. It wasn't until the 1860s that people began cracking it. I wanted to see if I could break it using a semester's knowledge of Python. This was that attempt.

My project broke down into three parts:
1. Implement the Vigenere cipher.
2. Break the cipher using a brute force attack.
3. Break the cipher using a dictionary attack.

Both methods were "brute force" in nature, but one used any combination of letters, the other used only words in the dictionary.

The Vigenere cipher is a similar method to the Caeser cipher, but using a word, rather than one letter. While the Caeser cipher picks a letter and shifts all other letters along the alphabet by that letter's numeric value, the Vigenere cipher picks a word and shifts each of the letters by its corresponding letter's value. For example:


| Plaintext     | Key           | Ciphertext   |
| :-----------: |:-------------:| :-----------:|
| ATTACKATDAWN  | LEMONLEMONLE  | LXFOPVEFRNHR |

In this case, the word "lemon" encrypts the message "attack at dawn."

I gave myself a few restrictions to simplify things. First, I made sure that both the key and the message could only be one word. After trying to parse multiple words, I realized the word "that" could break down into "that", "hat", "ha", "at", and "a". Knowing the answer is one word makes things much, much easier. These words were drawn from the dictionary file in unix machines, so it could reference it locally.

In the end, I was only mildly successful, building tools that would *eventually* break the encryption, but it would take a while.

Here are some of the results for the brute force attack. For a...:
+ 1 letter word: .09 seconds.
+ 3 letter word: 11.8 hours.
+ 7 letter word: 150 x the age of the universe.
+ 10 letter word: 6.3e6 x the age of the universe.
+ 24 letter word: 6.3e67 x the age of the universe.

Here are some of the results for the dictionary attack. For a...:
+ 1 letter word: .01 seconds.
+ 3 letter word: 8.863 seconds.
+ 7 letter word: 1.48 hours.
+ 10 letter word: 4.99 hours.
+ 24 letter word: 4.5 seconds.

In the dictionary attack, there are only so many 24 letter words, so although you could use a 1- through 24-letter word to encrypt it, you don't test as many combinations in the end.


In the end, I learned that a handleful of Python can help solve a lot of problems, but a brute force attack is not the way this problem can be solved, and there is still much to learn. My full write-up on the project is also uploaded for more details.
