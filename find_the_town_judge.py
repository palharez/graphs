def findJudge(N, trust):
    count = [0] * (N+1)
    for a, b in trust:
        count[a] -= 1
        count[b] += 1

    for n in range(N + 1):
        if count[n] == N - 1:
            return n
    
    return -1

def main():
    print(findJudge(N = 2, trust = [[1,2]]))
    print(findJudge(N = 3, trust = [[1,3],[2,3]]))
    print(findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))
    print(findJudge(N = 3, trust = [[1,2],[2,3]]))
    print(findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))

if __name__ == "__main__":
    main()