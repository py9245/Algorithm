package class_B.입시예측;

import java.util.*;

class UserSolution
{
	
	static int n, m;
	static int[][] weight;
	
	static int[] schoolSize;
	static int[] schoolMinmum;
//	erase, suggest 용도 등록된 학생, 삭제되지 않은 학생이 보장됨으로
//	초기값 0 배정 후엔 그 대학의 번호 삭제되면 -1
	static int[] studentInfo;
	
	static class Student implements Comparable<Student>{
		int score, sID;
		public Student(int score, int sID) {
			this.score = score;
			this.sID = sID;
		}
		public int compareTo(Student o) {
			if(this.score != o.score) return o.score - this.score;
			return this.sID - o.sID;
		}
	}
	static TreeSet<Student>[] univers;

	
//	학생은 하나의 대학에 입학, 각 대학은 최대 N명 뽑을 수 있음
//	학생들은 되도록 낮은 대학 입학하고 싶음 -> 우선순위
//	각 대학마다 과목별 가중치가 다름 총점 높은 사람 N명 뽑고 총점이 같으면 id 낮은 학생 우선
//	번호 순서대로 선발 이 과정에서 선발되었다면 그 다음 제외

//	객체 학생최대 2만번 한번마다 모두 대학의 가중치를 곱해서 대학에 넣긴 해야함
//	일단 suggest는 O(1)이 되어야함
//	대학 별 N번째로 점수 높은 학생들
	
	public void init(int N, int M, int[][] mWeights)
	{
		n = N;
		m = M;
		weight = new int[M + 1][5];
		univers = new TreeSet[M + 1];
		for (int i = 0; i < M; i++) {
			univers[i] = new TreeSet<Student>();
			for (int j = 0; j < 5; j++) {
				weight[i + 1][j] = mWeights[i][j];
			}
		}
		univers[M] = new TreeSet<Student>();
		schoolMinmum = new int[M + 1];
		schoolSize = new int[M + 1];

		return;
	}

	public void add(int mID, int[] mScores)
	{
		boolean update = false;
		int newScore = 0;
		for (int i = 1; i < m + 1; i++) {
			for (int j = 0; j < 5; j++) {
				newScore += mScores[j] * weight[i][j];
			}
			if (schoolSize[i] < n || (schoolSize[i] == n && newScore > schoolMinmum[i])) {
				studentInfo[mID] = i;
				univers[i].add(new Student(newScore, mID));
			}
		}
		return;
	}

	public void erase(int mID)
	{
		return;
	}

	public int suggest(int mID)
	{
		return -1;
	}
}