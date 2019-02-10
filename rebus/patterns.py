#!/usr/bin/env python3
import rebus
from rebus import emojis

def r_above(x, y):
    return emojis.emojify(x) + "<br>" + emojis.emojify(y)

def r_after(x, y):
    return emojis.emojify(y) + "\t\t" + emojis.emojify(x)

def r_around(x, y):
    return "<table border=0><tr><td>" + emojis.emojify(x) + "</td><td>" + emojis.emojify(x) + "</td><td>" + emojis.emojify(x) + "</td></tr><tr><td>" + emojis.emojify(x) + "</td><td style='padding: 50px'>" + emojis.emojify(y) + "</td><td>" + emojis.emojify(x) + "</td></tr><tr><td>" + emojis.emojify(x) + "</td><td>" + emojis.emojify(x) + "</td><td>" + emojis.emojify(x) + "</td></tr></table>"

def r_before(x, y):
    return r_after(y, x)

def r_against(x, y):
    return emojis.emojify(x) + " vs. " + emojis.emojify(y)

def r_under(x, y):
    return r_above(y, x)

def r_below(x, y):
    return r_under(x, y)

def r_in(x, y):
    return y[:int(len(y)/2)] + emojis.emojify(x) + y[int(len(y)/2):]

def r_to(x, y):
    return x + "➡️" + y

def r_through(x,y):
    return "<table border=0><tr><td>" + "" + "</td><td>" + emojis.emojify(y) + "</td><td>" + "" + "</td></tr><tr><td>" + emojis.emojify(x) + "</td><td style='padding: 50px'>" + "➡️" + "</td><td>" + "➡️" + "</td></tr><tr><td>" + "" + "</td><td>" + emojis.emojify(y) + "</td><td>" + "" + "</td></tr></table>"

def r_between(x,y):
    return y + " " + x + " " + y

def r_into(x,y):
    return "<table border=0><tr><td>" + "" + "</td><td>" + "" + "</td><td>" + emojis.emojify(y) + "</td><td>" + emojis.emojify(y) + "</td></tr><tr><td>" + emojis.emojify(x) + "</td><td style='padding: 50px'>" + "➡️" + "</td><td style='padding: 50px'>" + "" + "</td><td>" + emojis.emojify(y) + "</td></tr><tr><td>" + "" + "</td><td>" + "" + "</td><td>" + emojis.emojify(y) + "</td><td>" + emojis.emojify(y) + "</td></tr></table>"

def r_from(x,y):
    return x + "⬅️" + y

def r_beyond(x,y):
    return y + "..." + x

def r_color(color, x):
    return "<span style='color:" + color + "'>" + x + "</span>"
