import java.util.*;

class UserSolution {
    static int maxCnt;
    static Deque<String> queue = new LinkedList<>();
    static HashMap<String, Integer> string_counter = new HashMap<>();

    @SuppressWarnings("unchecked")
    static HashMap<String, Set<String>>[] linked_list = new HashMap[8]; // 길이 3~10

    void init(int N) {
        maxCnt = N;
        queue.clear();
        string_counter.clear();
        for (int i = 0; i < 8; i++) linked_list[i] = new HashMap<>();
    }

    void addKeyword(String mKeyword) {
        // 슬라이딩 윈도우
        if (queue.size() == maxCnt) {
            String first = queue.removeFirst();
            int nv = string_counter.get(first) - 1;
            if (nv <= 0) string_counter.remove(first);
            else string_counter.put(first, nv);
        }
        queue.addLast(mKeyword);
        string_counter.put(mKeyword, string_counter.getOrDefault(mKeyword, 0) + 1);

        int idx = mKeyword.length() - 3;
        if (idx < 0 || idx >= 8) return; // 안전막 (길이 3~10 이외 무시)

        // CME 방지: 기존 키 목록 스냅샷
        List<String> keys = new ArrayList<>(linked_list[idx].keySet());

        // 나 자신 등록 (Set으로 중복 방지)
        Set<String> mySet = linked_list[idx].computeIfAbsent(mKeyword, k -> new HashSet<>());

        // 같은 길이 기존 단어들과 유사(한 글자 차이)하면 양방향 연결
        for (String other : keys) {
            if (other.equals(mKeyword)) continue;
            if (isSimilar(mKeyword, other)) {
                Set<String> oSet = linked_list[idx].get(other);
                oSet.add(mKeyword);
                mySet.add(other);
            }
        }
    }

    // 한 글자만 다르면 true
    boolean isSimilar(String a, String b) {
        if (a.length() != b.length()) return false;
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
                if (diff > 1) return false;
            }
        }
        return diff == 1;
    }

    int top5Keyword(String[] mRet) {
        Set<String> visited = new HashSet<>();
        List<Group> groups = new ArrayList<>();

        // 현재 창 안에 "살아있는" 단어들만 시드로 BFS
        for (String seed : string_counter.keySet()) {
            if (visited.contains(seed)) continue;

            int total = 0;            // 그룹 합계 (멤버들의 개별 카운트 합)
            String rep = null;        // 대표 (그룹 내 개별 카운트 최댓값, 동률 사전순 앞)
            int repCnt = -1;

            Deque<String> dq = new ArrayDeque<>();
            dq.add(seed);
            visited.add(seed);

            while (!dq.isEmpty()) {
                String cur = dq.removeFirst();
                int cnt = string_counter.getOrDefault(cur, 0);
                if (cnt > 0) total += cnt;

                // 대표 갱신: 개별 카운트가 큰 단어 우선, 동률이면 사전순 앞선 단어
                if (cnt > repCnt || (cnt == repCnt && (rep == null || cur.compareTo(rep) < 0))) {
                    repCnt = cnt;
                    rep = cur;
                }

                int idx = cur.length() - 3;
                if (idx < 0 || idx >= 8) continue;

                // 이웃 확장: **현재 창에서 count>0인 단어만** 큐에 넣어 연결 확장
                Set<String> neighbors = linked_list[idx].get(cur);
                if (neighbors != null) {
                    for (String nxt : neighbors) {
                        if (!visited.contains(nxt) && string_counter.getOrDefault(nxt, 0) > 0) {
                            visited.add(nxt);
                            dq.add(nxt);
                        }
                    }
                }
            }

            if (total > 0) {
                groups.add(new Group(total, rep));
            }
        }

        // 그룹 정렬: 합계 내림차순, 동률이면 대표(사전순) 오름차순
        groups.sort((a, b) -> {
            if (b.count != a.count) return b.count - a.count;
            return a.rep.compareTo(b.rep);
        });

        int retSize = Math.min(5, groups.size());
        for (int i = 0; i < retSize; i++) mRet[i] = groups.get(i).rep;
        return retSize;
    }

    static class Group {
        int count;
        String rep;
        Group(int c, String r) { count = c; rep = r; }
    }
}
