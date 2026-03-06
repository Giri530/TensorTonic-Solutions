def text_chunking(tokens, chunk_size, overlap):
    step=chunk_size-overlap
    chunks=[]
    start=0
    while start<len(tokens):
        chunk=tokens[start:start+chunk_size]
        if len(chunk)==chunk_size or len(tokens)<=chunk_size:
            chunks.append(chunk) 
        start+=step
    return chunks