import nltk
from nltk.tokenize import word_tokenize
import sys

nltk.download("punkt")
nltk.download("punkt_tab")

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
S -> S Conj S

NP -> N | Det N | Det AdjP N | N PP | NP Conj NP
VP -> V | V NP | V PP | V NP PP | VP PP | V Adv | VP Conj VP
AdjP -> Adj | Adj AdjP
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert sentence to a list of tokens.

    """
    alphabet= [chr(item) for item in range(65,91)] + [chr(item) for item in range(97,123)] 
    # print(alphabet)
    tokens=nltk.word_tokenize(sentence)
    # print(sentence)
    tokens=[word.lower() for word in tokens]

    tokens=[word for word in tokens if any(ch in alphabet for ch in word)]
    return tokens
    # print(tokens)

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks=[]
    
    subtrees=tree.subtrees()
    for t in subtrees:
        if t.label()=="NP":
            not_unique=0
            for item in t.subtrees():
                if item is t:
                    continue
                if item.label()=="NP":
                    not_unique=1
                    break
            if not_unique==0:
                chunks.append(t)        

    return chunks



if __name__ == "__main__":
    main()
