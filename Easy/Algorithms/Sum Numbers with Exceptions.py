# def calculate_sum(N):
#     s = 0
#     for i in range(1,N+1):
#         if((i%3!=0) and (i%7!=0)):
#             s+=i
#     return s
#     # return sum(i for i in numList if i%7!=0 and i%3!=0) #Python One Liner

# Avoiding Looping and division check 
def calculate_sum(N):
    def sum_divisible_by(k):
        p = N // k
        return k * (p * (p + 1))/2
    
    total_sum = N * (N + 1)/2
    sum_div_3 = sum_divisible_by(3)
    sum_div_7 = sum_divisible_by(7)
    sum_div_21 = sum_divisible_by(21)
    
    result = total_sum - (sum_div_3 + sum_div_7 - sum_div_21)
    return int(result)

