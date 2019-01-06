# from Linzen's code repo
import inflect

infl_eng = inflect.engine()

def gen_inflect_from_vocab(vocab_file, freq_threshold=1000):
    vbp = {}
    vbz = {}
    nn = {}
    nns = {}
    from_pos = {'NNS': nns, 'NN': nn, 'VBP': vbp, 'VBZ': vbz}

    for line in file(vocab_file):
        if line.startswith(' '):   # empty string token
            continue
        word, pos, count = line.strip().split()
        count = int(count)
        if len(word) > 1 and pos in from_pos and count >= freq_threshold:
            from_pos[pos][word] = count

    verb_infl = {'VBP': 'VBZ', 'VBZ': 'VBP'}
    for word, count in vbz.iteritems():
        candidate = infl_eng.plural_verb(word)
        if candidate in vbp:
            verb_infl[candidate] = word
            verb_infl[word] = candidate

    noun_infl = {'NN': 'NNS', 'NNS': 'NN'}
    for word, count in nn.iteritems():
        candidate = infl_eng.plural_noun(word)
        if candidate in nns:
            noun_infl[candidate] = word
            noun_infl[word] = candidate

    return verb_infl, noun_infl

vinfl, ninfl = gen_inflect_from_vocab('wiki.vocab')
