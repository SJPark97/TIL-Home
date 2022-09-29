# 교수님노트

### 최소신장트리(MST), 최단경로(다익스트라)

- 최소신장트리
  - 크루스칼(집합, 서로소집합(Union-Find)) 그리디
  - 프림(cut property) 그리디
- 다익스트라

##### Union-Find 자료구조(서로소 집합, 상호 배타 집합, disjoint set)

집합의 연산
1. membership연산 (in, not in)
2. 합집합, 교집합, 차집합

Union-Find 과정
1. make_set : 집합을 만들기
2. find_set : 집합을 찾기 (해당 집합의 대표원소값 반환)
3. union : find_set을 했을때의 대표값이 다르면 union이 다르다.

##### 크루스칼 알고리즘

최소신장트리
1. 그래프랑 모든 노드를 포함한다.
2. 사이클이 존재하지 않는다.
3. 간선에 비용이 존재할때 비용의 합이 최소가 되는 신장트리


##### 프림 알고리즘

1. 임의 정점 선택
2. MST에서 갈 수 있는 모든 정점 중 가장 최소 비용 선택
3. cost += distance

```python
# 1) 일반적인 프림 알고리즘

def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    distance = [INF] * (n + 1)  # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용
    distance[start] = 0
    cost = 0  # MST의 비용 총합(== 최소 비용)

    # 정점의 개수만큼 반복하면서 모든 정점을 이은 MST 생성
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점 중 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist = INF
        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        # 2. 해당 정점을 MST에 포함하고 비용을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

    return cost


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작
``` 


##### 다익스트라

특정 정점에서 -> 다른 모든 정점으로 갈때 최단거리

1. 출발지점
2. distansce
3. 갱신

```python
# 1) 일반적인 다익스트라 알고리즘

def dijkstra(start):
    visited = [False] * (n + 1)  # 방문 처리 리스트(최단 거리가 확정된 정점)
    visited[start] = True
    distance[start] = 0

    # 시작 정점과 인접한 정점에 대해 최단 거리 초기화
    for e, w in graph[start]:
        distance[e] = w

    # 시작 정점을 제외한 나머지 정점에 대해서만 반복하므로 n - 1 번 반복함
    for _ in range(n - 1):
        # 1. 최단 거리가 확정되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
        min_dist = INF
        for i in range(1, n + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        # 2. 해당 정점 최단 거리 확정
        visited[min_node] = True

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점에서 시작
print(distance)
```