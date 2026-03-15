import numpy as np
from collections import Counter
import math
def tfidf_vectorizer(documents):
    if not documents:
        return np.array([[]]), []
    tokenize=[doc.lower().split() for doc in documents]
    vocab=sorted(set(word for doc in tokenize for word in doc))
    if not vocab:
        return np.zeros((len(documents), 0)), []
    word_to_index={word: i for i, word in enumerate(vocab)}
    n_docs=len(documents)
    n_vocab=len(vocab)
    tf_matrix=np.zeros((n_docs, n_vocab))      
    for i, doc in enumerate(tokenize):
        if not doc:
            continue
        word_doc=Counter(doc)
        total_doc=len(doc)
        for word, count in word_doc.items():
            tf_matrix[i][word_to_index[word]]=count / total_doc
    idf=np.zeros(n_vocab)                     
    for j, word in enumerate(vocab):
        df=sum(1 for doc in tokenize if word in doc)
        idf[j]=math.log(n_docs / df)
    tfidf_matrix=tf_matrix * idf
    return tfidf_matrix, vocab