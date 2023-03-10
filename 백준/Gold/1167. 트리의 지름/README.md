# [Gold II] 트리의 지름 - 1167 

[문제 링크](https://www.acmicpc.net/problem/1167) 

### 성능 요약

메모리: 84692 KB, 시간: 824 ms

### 분류

트리(trees)

### 문제 설명

<p>트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.</p>

<p>먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.</p>

### 아이디어
1. 루트노드 혹은 리프노드를 찾는다. 이때, 시작점은 임의의 정점으로 시작하며, 해당 정점으로부터 가장 거리가 먼 노드를 찾는다.
2. 1번에서 찾은 노드를 시작점으로 가장 거리가 먼 노드를 찾는다.
