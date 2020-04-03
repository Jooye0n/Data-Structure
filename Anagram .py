def generate_anagrams(S):
    if len(S) == 0:
        return[]
    if len(S) == 1:
        return[S]
    word_tmp = []
    for i in range(len(S)):
        c = S[i]
        remain = S[:i] + S[i+1:]
        for p in generate_anagrams(remain):
            word_tmp.append(c + p)
    return (word_tmp)

if __name__ == "__main__":
    print(generate_anagrams('abc'))

