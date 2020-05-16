def findJudge(N, trust):
    if len(trust) == 0:
        return N

    N_items = [n + 1 for n in range(N)]
    graph = {}

    # Creating graph
    for a, b in trust:
        if not graph.get(b):
            graph[b] = {a: 1}
        else:
            graph[b][a] = 1

    judge = -1

    for n in N_items:
        if not graph.get(n):
            continue
        
        not_judge = False

        for k in N_items:
            if n == k:
                continue
            if not graph.get(k):
                continue
            if graph[k].get(n):
                not_judge = True
                break

        if not_judge:
            continue
    
        if len(graph.get(n)) == len(N_items) - 1:
            judge = n

    return judge
    
def main():
    print(findJudge(N = 2, trust = [[1,2]]))
    print(findJudge(N = 3, trust = [[1,3],[2,3]]))
    print(findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))
    print(findJudge(N = 3, trust = [[1,2],[2,3]]))
    print(findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))
    print(findJudge(N = 1, trust = []))
    print(findJudge(N = 2, trust = [[1,2],[2,1]]))

if __name__ == "__main__":
    main()