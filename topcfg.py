from nltk.corpus.reader import BracketParseCorpusReader
from collections import Counter
import numpy as np
import re, sys, os

def traverse_tree(tree, list_counts_rules):
    if len(tree) == 1:
        leaf = tree.leaves()[0]
        if "\'" in leaf:
            list_counts_rules.append(f"{tree.label()} -> \"{leaf}\"")
        else:
            list_counts_rules.append(f"{tree.label()} -> \'{leaf}\'")
    else:
        list_counts_rules.append(f"{tree.label()} -> {tree[0].label()} {tree[1].label()}")
        traverse_tree(tree[0], list_counts_rules)
        traverse_tree(tree[1], list_counts_rules)


#usage: hw4_topcfg.sh <treebank_filename> <output_PCFG_file>
if __name__ == "__main__":
    PATH_TRAIN = sys.argv[1]
    out = sys.argv[2]

    match = re.search("(?s:.*)/", PATH_TRAIN)
    if match:
        DIR_TRAIN = re.search("(?s:.*)/", PATH_TRAIN).group(0)
    else:
        DIR_TRAIN = os.getcwd()

    # read in parsed corpus
    with open(PATH_TRAIN) as f:
        data = f.read()
    parsed_data = BracketParseCorpusReader(DIR_TRAIN,'parses.train').parsed_sents() 

    # get counts of all non-terminals
    counts_nodes = Counter(re.findall("\(([A-Z_]+) ", data))

    # get counts of all rules
    list_counts_rules = [] 
    for sent in parsed_data:
        traverse_tree(sent, list_counts_rules) 
    counts_rules = Counter(list_counts_rules) 

    prob_rules = dict() 
    for rule in counts_rules:
        node = re.findall("([A-Z_]+)", rule)[0] 
        prob_rules[rule] = counts_rules[rule] / counts_nodes[node] 

    with open(out, 'w') as f:
        for rule in prob_rules:
            f.write(f"{rule} [{prob_rules[rule]}]\n")