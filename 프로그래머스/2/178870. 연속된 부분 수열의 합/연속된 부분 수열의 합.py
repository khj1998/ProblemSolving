def solution(sequence, k):
    n = len(sequence)
    start = end = 0
    current_sum = sequence[0]

    best_range = (0, n - 1)

    while start <= end and end < n:
        if current_sum == k:
            if (end - start) < (best_range[1] - best_range[0]):
                best_range = (start, end)
            start += 1
            if start <= end:
                current_sum -= sequence[start - 1]
            else:
                end += 1
                if end < n:
                    current_sum = sequence[end]
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
        else:  
            current_sum -= sequence[start]
            start += 1

    return list(best_range)