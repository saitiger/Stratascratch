def find_common_words(input):
    import re 


# sentence1 = re.findall(r'\b\w+\b',input[0])
# sentence2 = re.findall(r'\b\w+\b',input[1])


    s1 = [x.lower() for x in input[0].split(" ")]
    s2 = [x.lower() for x in input[1].split(" ")]
    s1.sort()
    s2.sort()


    seen = set()

    for s in s1:
        if s not in seen:
            seen.add(s)
    res = [] 
    for x in s2:
        if x in seen:
            res.append(x)
    return res
    
    
import string

def find_common_words(input):
    sentence1 = input[0].lower()
    sentence2 = input[1].lower()
    
    words1 = set(sentence1.split())
    words2 = set(sentence2.split())
    
    common_words = words1.intersection(words2)
    
    return sorted(common_words)
