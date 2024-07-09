import random

random.seed(0)

def biased_coin_flip(input):
    p = input["probability"]
    N = input["N"]
    results = []
    for _ in range(N):
        result = 1 if random.random() < p else 0
        results.append(result)
    return results
