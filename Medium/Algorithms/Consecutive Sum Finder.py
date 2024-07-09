def find_consecutive_sum(input):
    numbers = input["numbers"]
    target_sum = input["target_sum"]
    n = input["n"]
  # Brute Force
    # if len(numbers) < n:
    #     return []
    # ans = []
    # for i in range(len(numbers)-2):
    #     if(numbers[i]+numbers[i+1]+numbers[i+2]==target_sum):
    #         ans.append([numbers[i],numbers[i+1],numbers[i+2]])
    # return ans
  
# Sliding Window
    current_sum = sum(numbers[:n])
    if current_sum == target_sum:
        ans.append(numbers[:n])
    for i in range(n, len(numbers)):
        current_sum += numbers[i] - numbers[i - n]
        if current_sum == target_sum:
            ans.append(numbers[i - n + 1:i + 1])
    return ans
