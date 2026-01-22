package class_B.OTT;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class UserSolution {

    static int n, movieCreatedAt;
    static int[] watchAt;

    // PQ 노드(스냅샷). total/createdAt로 정렬
    static class Movie implements Comparable<Movie> {
        int mID, createdAt, total, genre, ver;
        boolean isRemove;

        Movie(int mID, int genre, int total) {
            this.mID = mID;
            this.genre = genre;
            this.total = total;
        }

        public int compareTo(Movie o) {
            if (this.total != o.total) return o.total - this.total;
            return o.createdAt - this.createdAt;
        }
    }

    // 유저 시청 기록(최근 5개 선택용)
    static class UserMovie {
        Movie movie;
        int uID, userScore, watchedAt;

        UserMovie(Movie movie, int userScore, int uID) {
            this.movie = movie;
            this.userScore = userScore;
            this.uID = uID;
            this.watchedAt = watchAt[uID]++;
        }
    }

    static Map<Integer, Movie> movies;                 // mID -> 최신 상태
    static Map<Integer, Integer> ver;                  // mID -> 최신 버전
    static PriorityQueue<Movie> allGenreMovies;        // 전체 추천용
    static PriorityQueue<Movie>[] genreMovies;         // 장르별 추천용
    static ArrayList<UserMovie>[] user;                // 유저 히스토리
    static HashMap<Integer, Boolean>[] userWatched;    // 유저가 본 영화 체크

    @SuppressWarnings("unchecked")
    void init(int N) {
        n = N;
        movieCreatedAt = 0;

        movies = new HashMap<>();
        ver = new HashMap<>();

        allGenreMovies = new PriorityQueue<>();

        genreMovies = new PriorityQueue[6]; // 1~5 사용
        for (int g = 1; g <= 5; g++) genreMovies[g] = new PriorityQueue<>();

        watchAt = new int[N + 1];

        user = new ArrayList[N + 1];
        userWatched = new HashMap[N + 1];
        for (int u = 1; u <= N; u++) {
            user[u] = new ArrayList<>();
            userWatched[u] = new HashMap<>();
        }
    }

    int add(int mID, int mGenre, int mTotal) {
        if (movies.get(mID) != null) return 0;

        Movie curr = new Movie(mID, mGenre, mTotal);
        curr.createdAt = movieCreatedAt++;

        ver.put(mID, 0);
        curr.ver = 0;

        movies.put(mID, curr);
        allGenreMovies.add(curr);
        genreMovies[mGenre].add(curr);

        return 1;
    }

    // PQ에서 바로 제거하지 않고 버전을 올려서 ghost 처리
    int erase(int mID) {
        Movie curr = movies.get(mID);
        if (curr == null || curr.isRemove) return 0;

        curr.isRemove = true;

        int v = ver.get(mID) + 1;
        ver.put(mID, v);
        curr.ver = v;

        return 1;
    }

    // total 갱신은 기존 노드 수정 대신 새 노드 push (ghost 방식)
    int watch(int uID, int mID, int mRating) {
        Movie curr = movies.get(mID);
        if (curr == null) return 0;
        if (curr.isRemove) return 0;
        if (userWatched[uID].getOrDefault(mID, false)) return 0;

        userWatched[uID].put(mID, true);

        ver.put(mID, ver.get(mID) + 1);

        Movie newMovie = new Movie(mID, curr.genre, curr.total + mRating);
        newMovie.createdAt = curr.createdAt;
        newMovie.ver = curr.ver + 1;

        movies.put(mID, newMovie);
        allGenreMovies.add(newMovie);
        genreMovies[newMovie.genre].add(newMovie);

        user[uID].add(new UserMovie(newMovie, mRating, uID));

        return 1;
    }

    Solution.RESULT suggest(int uID) {
        Solution.RESULT res = new Solution.RESULT();
        for (int i = 0; i < 5; i++) res.IDs[i] = 0;

        // 최근 5개(삭제 제외) 수집
        int startIdx = user[uID].size() - 1;
        UserMovie[] last5 = new UserMovie[5];
        int k = 0;

        while (startIdx >= 0 && k < 5) {
            UserMovie um = user[uID].get(startIdx--);
            Movie now = movies.get(um.movie.mID);
            if (now == null || now.isRemove) continue;
            last5[k++] = um;
        }

        // 최근 5개 중 최고 평점의 장르 선택(동점이면 더 최근 watchedAt)
        int bestScore = -1, bestWatchedAt = -1, topGenre = -1;
        for (int i = 0; i < k; i++) {
            UserMovie um = last5[i];
            if (um.userScore > bestScore || (um.userScore == bestScore && um.watchedAt > bestWatchedAt)) {
                bestScore = um.userScore;
                bestWatchedAt = um.watchedAt;
                topGenre = um.movie.genre;
            }
        }

        PriorityQueue<Movie> pq = (topGenre == -1) ? allGenreMovies : genreMovies[topGenre];

        // poll로 꺼낸 유효 노드는 다시 넣어 PQ 유지(watched는 유저별 조건)
        ArrayList<Movie> buf = new ArrayList<>();
        int cnt = 0;

        while (cnt < 5 && !pq.isEmpty()) {
            Movie node = pq.poll();
            if (node == null) break;

            Movie now = movies.get(node.mID);
            if (now == null || now.isRemove) continue;
            if (node.ver != ver.get(node.mID)) continue;

            if (userWatched[uID].getOrDefault(node.mID, false)) {
                buf.add(node);
                continue;
            }

            res.IDs[cnt++] = node.mID;
            buf.add(node);
        }

        for (Movie m : buf) pq.add(m);

        res.cnt = cnt;
        return res;
    }
}
