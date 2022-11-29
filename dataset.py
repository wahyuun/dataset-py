from symspellpy import SymSpell, Verbosity

# initialize
sym_spell = SymSpell()

# create dictionary
path_corpus = "kompas.txt"
sym_spell.create_dictionary(path_corpus)

list_kata = input('Inputkan Teks Disini : ')
sentence = list_kata.split()

for kata in sentence:
    maxEditDistanceLookup = 2
    include_unknown = True
    suggestion = sym_spell.lookup(kata, Verbosity.TOP, maxEditDistanceLookup, include_unknown)

#display term and edit distance
    for s in suggestion:
      print('Hasil Deteksi Ejaan : ', s.term, end=' ')