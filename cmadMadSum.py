def find_mad(arr):
    """
    Finds the Maximum Appearing Duplicate (MAD) in the array.
    If no such number exists, returns 0.
    """
    frequency = {}
    mad = 0
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        if frequency[num] > 1:
            mad = max(mad, num)
    return mad

def process_array(arr):
    """
    Processes the array according to the given rules and returns the final sum.
    """
    total_sum = 0
    while any(arr):  # Continue until all elements are 0
        total_sum += sum(arr)
        arr = [find_mad(arr[:i+1]) for i in range(len(arr))]
    return total_sum

def solve():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Size of the array
        arr = list(map(int, input().strip().split()))  # The array itself
        print(process_array(arr))


solve()