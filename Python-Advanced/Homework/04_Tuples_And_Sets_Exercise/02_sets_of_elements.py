n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

result = n_set.intersection(m_set)

print(*result, sep="\n")
