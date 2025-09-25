# Context-Free Grammar Parser with NLTK

This project implements a simple natural language parser using **NLTK** and a custom **context-free grammar (CFG)**.  
It parses input sentences into syntax trees and extracts **noun phrase (NP) chunks**.



## Features
- Defines a set of grammar rules (`TERMINALS` and `NONTERMINALS`) for basic English parsing.  
- Preprocesses input sentences:
  - Converts words to lowercase
  - Removes tokens without alphabetic characters  
- Uses **NLTK’s ChartParser** to generate parse trees.  
- Extracts **noun phrase chunks**, defined as:
  - Subtrees labeled `"NP"`
  - That do not contain other `"NP"` subtrees inside  


## Usage

### Run with a file:
```bash
python parser.py sentences.txt
```
### Run without a file 
```bash
python parser.py 
Sentence: 
