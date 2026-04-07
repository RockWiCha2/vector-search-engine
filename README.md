
# Vector Search Engine (Python)

A lightweight document search system built in Python using an inverted index and vector-based similarity.

This project was developed as coursework for a Mathematics for Computer Science module.

## Features

- Builds a dictionary of unique words from a document corpus
- Constructs an inverted index for efficient lookup
- Supports multi-word queries
- Retrieves documents containing all query terms
- Ranks results using vector similarity (angle between vectors)

## How it Works

Each document is represented as a vector where each element corresponds to the frequency of a word in the dictionary.

Each query is represented as a binary vector indicating whether a word appears in the query.

Similarity is calculated using the angle between vectors — smaller angles indicate higher relevance.

## File Structure

- `DocSearch.py` — main program
- `docs.txt` — input documents (one per line)
- `queries.txt` — search queries (one per line)

## Usage

1. Place `docs.txt` and `queries.txt` in the same directory as `DocSearch.py`
2. Run the program:

```bash
python3 DocSearch.py
```

## Example Output

```
Words in dictionary: 42
Query: search systems
Relevant documents: 1 3

1 12.34
3 45.67
```

## Notes

- Input text must be lowercase and contain no punctuation
- Words not present in the dictionary are ignored in queries
- Output formatting must match the specification exactly

## Technologies

- Python 3
- Standard library (`math`)

## Author

James Harvey
