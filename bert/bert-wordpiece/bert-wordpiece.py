from typing import List, Dict

class WordPieceTokenizer:
    """
    WordPiece tokenizer for BERT.
    """
    
    def __init__(self, vocab: Dict[str, int], unk_token: str = "[UNK]", max_word_len: int = 100):
        self.vocab = vocab
        self.unk_token = unk_token
        self.max_word_len = max_word_len
    
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into WordPiece tokens.
        """
        tokens = []
        for word in text.lower().split():
            word_tokens = self._tokenize_word(word)
            tokens.extend(word_tokens)
        return tokens
    
    def _tokenize_word(self, word: str) -> List[str]:
        if len(word)>self.max_word_len:
            return[self.unk_token]
        if word in self.vocab:
            return[word]
        tokens=[]
        start=0
        is_continuation=False
        while start<len(word):
            end=len(word)
            found=False
            while end>start:
                substr=("##" if is_continuation else "")+word[start:end]
                if substr in self.vocab:
                    tokens.append(substr)
                    start=end
                    is_continuation=True
                    found=True
                    break
                end-=1
            if not found:
                return[self.unk_token]
        return tokens
        
        