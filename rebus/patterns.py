#!/usr/bin/env python3
import rebus
from rebus import emojis

def r_above(x, y):
    return emojis.emojify(x) + "\n" + emojis.emojify(y)

def r_after(x, y):
    return emojis.emojify(y) + "\t,\t" + emojis.emojify(x)

def r_around(x, y):
    return emojis.emojify(x) + "\t" + emojis.emojify(x) + "\t" + emojis.emojify(x) + "\n" + emojis.emojify(x) + "\t" + emojis.emojify(y) + "\t" + emojis.emojify(x) + "\n" + emojis.emojify(x) + "\t" + emojis.emojify(x) + "\t" + emojis.emojify(x)

def r_before(x, y):
    return r_after(y, x)

def r_against(x, y):
    return emojis.emojify(x) + "\tvs.\t" + emojis.emojify(y)

def r_under(x, y):
    return r_above(y, x)

def r_below(x, y):
    return r_under(x, y)

def r_in(x, y):
    return y[:int(len(y)/2)] + emojis.emojify(x) + y[int(len(y)/2):]