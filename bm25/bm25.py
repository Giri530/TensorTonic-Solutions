import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    if not docs:
        return np.array([])
    tokenizer=docs
    N=len(tokenizer)
    averagedl=sum(len(doc) for doc in tokenizer)/N
    all_word=set(w for doc in tokenizer for w in doc)
    idf={}
    for word in all_word:
        n=sum(1 for doc in tokenizer if word in doc)
        idf[word]=math.log((N-n+0.5)/(n+0.5)+1)
    scores=[]
    for doc_tokens in tokenizer:
        doc_len=len(doc_tokens)
        score=0
        for term in query_tokens:
            f=doc_tokens.count(term)
            if f==0:
                continue
            norm=1-b+b*(doc_len/averagedl)
            tf_saturation=(f*(k1+1))/(f+k1*norm)
            score+=idf.get(term,0)*tf_saturation
        scores.append(score)
    return np.array(scores)
            
        