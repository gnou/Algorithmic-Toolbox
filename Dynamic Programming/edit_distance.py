# Uses python3
def edit_distance(s, t):
    all_values = []
    for i in range(0, len(s) + 1):
        all_values.append([])
        for j in range(0, len(t) + 1):
            if i == 0:
                all_values[i].append(j)
            elif j == 0:
                all_values[i].append(i)
            else:
                insertion = all_values[i][j-1] + 1
                deletion = all_values[i-1][j] + 1
                match = all_values[i-1][j-1]
                mismatch = all_values[i-1][j-1] + 1
                if s[i-1] == t[j-1]:
                    all_values[i].append(min(insertion, deletion, match))
                else:
                    all_values[i].append(min(insertion, deletion, mismatch))
    return all_values[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
