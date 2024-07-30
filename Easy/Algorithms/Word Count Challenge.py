def count_words(sentence):

    in_word = False
    word_count = 0
    length = len(sentence)
    
    for i in range(length):
        char = sentence[i]
        
        if char.isalnum() or char == '_':
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False
    return word_count
 # Method 2 
    import re    
    sentence = sentence.strip()
    words = re.findall(r'\b\w+\b', sentence) # Splits the word by boundary. w means letter or digits.
    return len(words)
