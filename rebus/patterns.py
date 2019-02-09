#!/usr/bin/env python3
import rebus
from rebus import emojis

def r_above(x, y):
    return emojis.to_emoji(x) + "\n" + emojis.to_emoji(y)

def r_after(x, y):
    return emojis.to_emoji(y) + "\t,\t" + emojis.to_emoji(x)

def r_around(x, y):
    return emojis.to_emoji(x) + "\t" + emojis.to_emoji(x) + "\t" + emojis.to_emoji(x) + "\n" + emojis.to_emoji(x) + "\t" + emojis.to_emoji(y) + "\t" + emojis.to_emoji(x) + "\n" + emojis.to_emoji(x) + "\t" + emojis.to_emoji(x) + "\t" + emojis.to_emoji(x)

def r_before(x, y):
    return r_after(y, x)

def r_against(x, y):
    return emojis.to_emoji(x) + "\tvs.\t" + emojis.to_emoji(y)

def r_under(x, y):
    return r_above(y, x)

def r_below(x, y):
    return r_under(x, y)

