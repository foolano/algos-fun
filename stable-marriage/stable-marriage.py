#!/usr/bin/python env
import sys

def propose(man, woman, women, marriages):
    if woman not in marriages:
        current_pref = sys.maxint
    else:
        current_pref = women[woman].index(marriages[woman])
    if man not in women[woman]:
        new_pref = sys.maxint
    else:
        new_pref = women[woman].index(man)
    return (new_pref < current_pref)

def stable_marriage(men, women):
    marriages = {}
    for man, prefer in men.items():
        for woman in prefer:
            if propose(man, woman, women, marriages):
                marriages[woman] = man
                break
    print marriages

stable_marriage({"m1": ["w1", "w2"], "m2": ["w1", "w2"]}, {"w1": ["m1", "m2"], "w2": ["m1", "m2"]})
