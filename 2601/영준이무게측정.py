# import sys

# sys.stdin = open("input.txt", "r")

# from collections import defaultdict

# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())

#     # 하루마다 N개의 샘플
#     # 오늘 하루는 이 N개의 샘플만 사용
#     # 1 ~ N의 번호가 붙어있음 정수!
#     # M은 query 갯수
#     # ! a b w = a, b무개 비교 b가 a 보다 w그램 무거움
#     # 들어온 기록으로 유추를 해야함... 모든정보를 파악해서 저장하기엔 메모리 부족할듯
#     # N은 10만개 N log N 이어야함
#     # 무게의 차이는 최대 100만 차이가 100만이니 계속 커질 수 있어 인덱스 관리 무리 딕셔너리로


#     # !!!!!!클러스터별로  line인접 딕셔너리를 만들고 합쳐질때 딕셔너리도 합쳐버리기
#     # 클러스터별로 기준 노드 설정하고 무게 0으로 설정
#     # 클러스터별 라인에 따라 무개도 관리함 (항상 간선을 타며 무개를 알아내기엔 시간 폭발하니까
#     # 간선은 간선대로 클러스터별 설정한 기준노드 기준으로 무게를 가정함


#     #인덱스로 클러스터를 관리 
#     cluster = [set()] # 클러스트 집단
#     cluster_root = [] # 클러스터 집단의 기준노드
#     line = [defaultdict(dict)] # 클러스터의 간선들 양방향으로

#     for _ in range(M):
#         query = input().strip().split()
#         a, b = map(int, query[1:3])
#         cmd = query[0]

#         if cmd == "!":
#             w = int(query[3])
#             line[a][b] = -w
#             line[b][a] = w
            
    
          
import sys

# 입출력 속도 향상
sys.stdin = open("input.txt", "r")

def solve():
    T_str = input().strip()
    if not T_str: return
    T = int(T_str)

    for tc in range(1, T + 1):
        line = input().split()
        N = int(line[0])
        M = int(line[1])

        parent = list(range(N + 1))
        # dist[i]: parent[i]와 i의 무게 차이
        dist = [0] * (N + 1)

        # [핵심] 재귀 없는 반복문 Find 함수
        def find(x):
            # 1. 루트 찾기
            root = x
            while parent[root] != root:
                root = parent[root]
            
            # 2. 경로 압축 및 무게 갱신 (스택 활용)
            # x에서 root까지 가는 경로에 있는 노드들의 무게를 갱신해야 함
            cur = x
            # 경로상의 노드들을 추적하기 위한 임시 변수들이 필요 없음
            # 단순히 부모를 따라가며 갱신하는 것이 아니라,
            # 위에서부터 아래로 갱신값이 전파되어야 하므로 '경로 저장'이 필요함.
            
            path = []
            while cur != root:
                path.append(cur)
                cur = parent[cur]
            
            # 경로를 역순(루트와 가까운 쪽부터)으로 처리
            # path[-1]은 루트의 바로 직계 자식 -> 이미 dist는 정확함 (루트 기준이므로)
            # 하지만 parent가 루트가 아닌 중간 보스일 수 있으므로 갱신 필요
            
            for node in reversed(path):
                # parent[node]는 아직 갱신 전의 부모(한 단계 위)
                # find 로직상, 역순으로 내려오면 상위 노드는 이미 root를 가리키고 dist도 root 기준임
                
                # 내 부모의 dist(루트 기준 누적치)를 내 dist에 더함
                dist[node] += dist[parent[node]]
                
                # 부모를 루트로 변경 (경로 압축)
                parent[node] = root
                
            return root

        def union(a, b, w):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                # root_b를 root_a에 붙임
                parent[root_b] = root_a
                # 무게 갱신 식: w + dist[a] - dist[b]
                dist[root_b] = dist[a] - dist[b] + w

        answer = [f"#{tc}"]
        
        for _ in range(M):
            query = input().split()
            cmd = query[0]
            a, b = int(query[1]), int(query[2])

            if cmd == "!":
                w = int(query[3])
                union(a, b, w)
            else:
                if find(a) != find(b):
                    answer.append("UNKNOWN")
                else:
                    # 두 노드의 무게 차이 출력
                    answer.append(dist[b] - dist[a])
        print(*answer)

if __name__ == "__main__":
    solve()