import math
import sys
import os
current_set = "set1"

# Read input files  
def read_docs(filename):
    docs = []
    with open(filename, "r") as f:
        for line in f:
            docs.append(line.strip().split())
    return docs

def read_queries(filename):
    queries = []
    with open(filename, "r") as f:
        for line in f:
            queries.append(line.strip().split())
    return queries


# Build dictionary  
def build_dictionary(docs):
    return sorted(set(word for doc in docs for word in doc))


# Build inverted index  
def build_inverted_index(docs):
    inverted = {}
    for i, doc in enumerate(docs):
        doc_id = i + 1
        for word in doc:
            if word not in inverted:
                inverted[word] = set()
            inverted[word].add(doc_id)
    return inverted


# Vector functions  
def build_doc_vectors(docs, dictionary):
    word_index = {word: i for i, word in enumerate(dictionary)}
    vectors = []

    for doc in docs:
        vec = [0] * len(dictionary)
        for word in doc:
            vec[word_index[word]] += 1
        vectors.append(vec)

    return vectors


def build_query_vector(query, dictionary, word_index):
    vec = [0] * len(dictionary)
    for word in query:
        if word in word_index:
            vec[word_index[word]] = 1
    return vec


def angle(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))

    # avoid division by zero
    if mag1 == 0 or mag2 == 0:
        return 90.0

    cos_theta = dot / (mag1 * mag2)

    # clamp due to floating point errors
    cos_theta = max(-1.0, min(1.0, cos_theta))

    return math.degrees(math.acos(cos_theta))

# Main  
def main():
    # Check if file paths are provided as arguments
    if len(sys.argv) == 3:
        docs_path = sys.argv[1]
        queries_path = sys.argv[2]
    else:
        # Default paths for testing (same directory as DocSearch.py)
        base_path = os.path.dirname(os.path.abspath(__file__))
        docs_path = os.path.join(base_path, "docs.txt")
        queries_path = os.path.join(base_path, "queries.txt")

    # Read documents and queries
    docs = read_docs(docs_path)
    queries = read_queries(queries_path)

    # Build dictionary and inverted index
    dictionary = build_dictionary(docs)
    print(f"Words in dictionary: {len(dictionary)}")
    inverted_index = build_inverted_index(docs)

    # Precompute vectors for efficiency
    doc_vectors = build_doc_vectors(docs, dictionary)
    word_index = {word: i for i, word in enumerate(dictionary)}

    # Process queries
    for query in queries:
        print(f"Query: {' '.join(query)}")

        # Filter valid words
        valid_words = [w for w in query if w in dictionary]

        # Find relevant docs (intersection)
        if not valid_words:
            relevant_docs = set()
        else:
            relevant_docs = inverted_index[valid_words[0]].copy()
            for w in valid_words[1:]:
                relevant_docs &= inverted_index[w]

        # Print relevant docs
        if relevant_docs:
            print("Relevant documents:", *relevant_docs)
        else:
            print("Relevant documents:")

        # Rank documents by angle
        query_vec = build_query_vector(valid_words, dictionary, word_index)
        results = []
        for doc_id in relevant_docs:
            doc_vec = doc_vectors[doc_id - 1]
            ang = angle(query_vec, doc_vec)
            results.append((doc_id, ang))

        # Sort by smallest angle
        results.sort(key=lambda x: x[1])
        for doc_id, ang in results:
            print(f"{doc_id} {ang:.2f}")

if __name__ == "__main__":
    main()