import json

dictionary = json.loads(open("words_dictionary.json", 'r').read())

words = set([d for d in dictionary if len(d) > 3])

letter_set = set(list('hapcred'))

center_l = 'h'

valid = []

def replace_char(w, c):
    w = w.replace(c, '')
    return w

for word in words:
    check = word
    if center_l not in check:
        continue
    for l in letter_set:
        check = replace_char(check, l)
    if check.strip() == '':
        valid.append(word)

valid_set = set(valid)

open('out.txt', 'w').write('\n'.join(v for v in valid_set))
