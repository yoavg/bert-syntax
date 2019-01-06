import csv
cases_we_care_about=['1','2','3','4']
from utils import vinfl

def inflect(verb):
    return vinfl[verb]

for record in csv.DictReader(open('agr_50_mostcommon_10K.tsv','r'), delimiter='\t'):
    orig = record['orig_sentence']
    n_i  = record['n_intervening']
    n_di = record['n_diff_intervening']
    vindex = int(record['verb_index'])-1
    if n_i != n_di: continue
    if n_di in cases_we_care_about:
        sorig = orig.split()
        verb = sorig[vindex]
        iverb = inflect(verb)
        #if verb in ['is','are']: continue # skip because of copular agreement
        sorig[vindex] = "***mask***"
        masked = " ".join(sorig)
        print("\t".join([n_di,orig,masked,verb,iverb]))
