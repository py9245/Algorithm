package class_B.입시예측;

import java.util.*;

class UserSolution {
	static final int MAXST = 20001;
	static int n, m;
	static int[][] weight;

	static int[] schoolSize;
//	static int[] schoolMinmum;
//	erase, suggest 용도 등록된 학생, 삭제되지 않은 학생이 보장됨으로
//	초기값 0 배정 후엔 그 대학의 번호 삭제되면 -1
	static int[] studentInfo;
	static boolean[] studentR;
	static int[][] studentTotal;
	static int[][] studentScore;

	static class Student implements Comparable<Student> {
		int score, sID;

		public Student(int score, int sID) {
			this.score = score;
			this.sID = sID;
		}

		public int compareTo(Student o) {
			if (this.score != o.score) return Integer.compare(o.score, this.score);
			return Integer.compare(this.sID, o.sID);
		}
	}

	static TreeSet<Student>[] univers;
	static TreeSet<Student>[] waitUnivers;

//	학생은 하나의 대학에 입학, 각 대학은 최대 N명 뽑을 수 있음
//	학생들은 되도록 낮은 대학 입학하고 싶음 -> 우선순위
//	각 대학마다 과목별 가중치가 다름 총점 높은 사람 N명 뽑고 총점이 같으면 id 낮은 학생 우선
//	번호 순서대로 선발 이 과정에서 선발되었다면 그 다음 제외

//	객체 학생최대 2만번 한번마다 모두 대학의 가중치를 곱해서 대학에 넣긴 해야함
//	일단 suggest는 O(1)이 되어야함
//	대학 별 N번째로 점수 높은 학생들

	public void init(int N, int M, int[][] mWeights) {
		n = N;
		m = M;
		weight = new int[M + 1][5];
		univers = new TreeSet[M + 1];
		waitUnivers = new TreeSet[M + 1];
		for (int i = 0; i <= M; i++) {
			univers[i] = new TreeSet<Student>();
			waitUnivers[i] = new TreeSet<Student>();
		}
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < 5; j++) {
				weight[i + 1][j] = mWeights[i][j];
			}
		}

//		schoolMinmum = new int[M + 1];
		schoolSize = new int[M + 1];
		studentInfo = new int[MAXST];
		studentR = new boolean[MAXST];
		studentTotal = new int[m + 1][MAXST];
		studentScore = new int[MAXST][5];
		Arrays.fill(studentInfo, m + 1);

		return;
	}

	public void add(int mID, int[] mScores) {
		studentR[mID] = false;
		studentInfo[mID] = m + 1;

		for (int k = 0; k < 5; k++) studentScore[mID][k] = mScores[k];

		for (int i = 1; i <= m; i++) {
			int sum = 0;
			for (int j = 0; j < 5; j++) sum += studentScore[mID][j] * weight[i][j];
			studentTotal[i][mID] = sum;
		}

		int curID = mID;

		for (int i = 1; i <= m; i++) {
			if (studentR[curID]) return;

			int curScore = studentTotal[i][curID];

			if (univers[i].size() < n) {
				univers[i].add(new Student(curScore, curID));
				studentInfo[curID] = i;
				return;
			}

			Student worst = univers[i].last();
			if (curScore > worst.score || (curScore == worst.score && curID < worst.sID)) {
				univers[i].add(new Student(curScore, curID));
				studentInfo[curID] = i;

				Student kicked = univers[i].pollLast();
				waitUnivers[i].add(kicked);

				curID = kicked.sID;
				studentInfo[curID] = m + 1;
			} else {
				waitUnivers[i].add(new Student(curScore, curID));
			}
		}

		return;
	}

	static void update(int uID, int sID) {
		if (uID == m + 1 || uID == 0) return;

		univers[uID].remove(new Student(studentTotal[uID][sID], sID));

		while (univers[uID].size() < n && !waitUnivers[uID].isEmpty()) {
			Student next = waitUnivers[uID].pollFirst();
			if (studentR[next.sID]) continue;
			if (studentInfo[next.sID] <= uID) continue;

			univers[uID].add(next);

			int prev = studentInfo[next.sID];
			studentInfo[next.sID] = uID;

			if (prev != m + 1 && prev != 0) update(prev, next.sID);
		}
	}

	public void erase(int mID) {
		int uniidx = studentInfo[mID];
		studentR[mID] = true;
		studentInfo[mID] = 0;
		if (uniidx == m + 1 || uniidx == 0) return;

		update(uniidx, mID);
		return;
	}

	public int suggest(int mID) {
		int v = studentInfo[mID];
		if (v == m + 1 || v == 0) return -1;
		return v;
	}
}
