#!/usr/bin/env python3

import nltk
from rebus import patterns
import random

nltk.download('punkt')

impl_binary_terminators = {
		#"around": patterns.r_around,
		}

impl_unary_terminators = {}

impl_binary = {
		# TODO function aliases happen here
		"above": patterns.r_above,
		"after": patterns.r_after,
		#"before": patterns.r_before,
		"against": patterns.r_against,
		"under": patterns.r_under,
		"below": patterns.r_below,
		#"in": patterns.r_in,
		"over" : patterns.r_above,
		#"to" : patterns.r_to,
		"through" : patterns.r_through,
		"between" : patterns.r_between,
		"into" : patterns.r_into,
		#"from" : patterns.r_from,
		"beyond" : patterns.r_beyond
		}

impl_unary = {}

file_lines = 2300;
def request_puzzle():
	while True:
		linenum = random.randint(0, file_lines);
		with open("../fixedidioms.txt") as f:
			x = f.readlines()[linenum].lower()
			reb = get_rebus(x)
			if reb == "":
				continue
			else:
				return (
					{
					'answer': x,
					'puzzle': reb
					}
					)

def get_rebus(sentence):
	articles = { "a", "an" }
	tokens = nltk.word_tokenize(sentence)
	tokens[:] = (value for value in tokens if value not in articles)
	foo = " ".join(tokens)
	bar = rebus_magic(tokens, True)
	if foo == " ".join(bar):
		return ""
	else:
		return bar

def rebus_magic(tokens, terminators_allowed=False):
	for t in tokens:
		i = tokens.index(t)

		# binary terminator functions
		if terminators_allowed:
			if (t in impl_binary_terminators.keys()):
				if (i == 0) or (i == len(tokens) - 1):
					pass
				else:
					leftSide = rebus_magic(" ".join(tokens[:i]))
					rightSide = rebus_magic(" ".join(tokens[i + 1:]))
					return impl_binary_terminators[t](leftSide, rightSide)

		# unary terminator functions
		if terminators_allowed:
			if (t in impl_unary_terminators.keys()):
				if i == len(tokens) - 1:
					pass
				else:
					rightSide = rebus_magic(" ".join(tokens[i + 1:]))
					return impl_unary_terminators[t](rightSide)

		# binary functions
		if t in impl_binary.keys():
			if (i == 0) or (i == len(tokens) - 1):
				pass
			else:
				leftSide = rebus_magic(" ".join(tokens[:i]))
				rightSide = rebus_magic(" ".join(tokens[i + 1:]))
				return impl_binary[t](leftSide, rightSide)

		# unary functions
		if t in impl_unary.keys():
			if i == len(tokens) - 1:
				pass
			else:
				rightSide = rebus_magic(" ".join(tokens[i + 1:]))
				return impl_unary[t](rightSide)
	return tokens
