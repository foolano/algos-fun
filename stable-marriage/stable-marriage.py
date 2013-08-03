#!/usr/bin/python env
import sets

def next_propose(free_m, m_pref, proposed_to):
    if not free_m:
        return (False, (None, None))
    for m in free_m:
        for w in m_pref[m]:
            if w not in proposed_to[m]:
                return (True, (m,w))
    return (False, (None, None))

def w_prefers_new(w, cm, nm, pref):
    if nm not in pref:
        return False
    return pref.index(nm) < pref.index(cm)

def stable_matching(nm, nw, m_pref, w_pref):
    w_engaged_to = {}
    m_set = sets.Set(range(0, nm))
    m_proposed_to = {i:sets.Set() for i in m_set}

    while True:
        free_m = m_set.difference(sets.Set(w_engaged_to.values()))
        free_w = m_set.difference(w_engaged_to.keys())
        (propose_left, (m, w)) = next_propose(free_m, m_pref, m_proposed_to)
        if not propose_left:
            break
        m_proposed_to[m].add(w)
        if w in free_w or w_prefers_new(w, w_engaged_to[w], m, w_pref[w]):
            w_engaged_to[w] = m

    print w_engaged_to

stable_matching(4, 4, {0: [2, 1, 3, 0], 1: [1, 2, 0, 3], 2: [2, 0, 1, 3], 3: [2, 1, 3, 0]}, {0: [3, 2, 0, 1], 1: [1, 0, 2, 3], 2: [0, 2, 3, 1], 3: [3, 2, 0, 1]})
