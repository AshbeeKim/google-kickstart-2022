for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    print(f"Case #{str(t)}: {str(sum(C)%M)}")