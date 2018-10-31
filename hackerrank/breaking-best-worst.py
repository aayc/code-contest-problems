def breakingRecords (scores):
    max_score = scores[0]
    min_score = scores[0]
    broke_max = 0
    broke_min = 0
    for i in range(1, len(scores)):
        prev_max = max_score
        max_score = max(max_score, scores[i])
        if max_score != prev_max:
            broke_max += 1

        prev_min = min_score
        min_score = min(min_score, scores[i])
        if min_score != prev_min:
            broke_min += 1

    return [broke_max, broke_min]

