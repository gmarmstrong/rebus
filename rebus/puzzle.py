#!/usr/bin/env python3

import nltk
import patterns

nltk.download('punkt')

sentence = "No coffee after midnight"
tokens = nltk.word_tokenize(sentence)   # tokenize words

impl_binary = {
        "above": patterns.r_above,
        "after": patterns.r_after,
        "against": patterns.r_against
        }

for word in tokens:
    i = tokens.index(word)
    if word in impl_binary.keys():
        leftSide = " ".join(tokens[:i])
        if i == len(tokens) - 1:
            rightSide = ""
        else:
            rightSide = " ".join(tokens[i + 1:])
        result = impl_binary[word](leftSide, rightSide)
        print(result)
