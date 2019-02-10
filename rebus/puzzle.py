#!/usr/bin/env python3

import nltk
import patterns

nltk.download('punkt')

impl_binary = {
        "above": patterns.r_above,
        "after": patterns.r_after,
        "around": patterns.r_around,
        "before": patterns.r_before,
        "against": patterns.r_against,
        "under": patterns.r_under,
        "below": patterns.r_below,
        "in": patterns.r_in
        }

def generate_rebus(sentence):
    tokens = nltk.word_tokenize(sentence)
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

generate_rebus("No coffee after midnight")
