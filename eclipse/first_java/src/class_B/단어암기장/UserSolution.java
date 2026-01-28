package class_B.단어암기장;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.TreeSet;

class UserSolution {
	static class Space implements Comparable<Space>{
		int mID, low, start, end, length;
		public Space(int mID, int low, int start, int end){
			this.low = low;
			this.start = start;
			this.end = end;
			this.length = end - start + 1;
			this.mID = mID;
		}
		public int compareTo(Space o){
			if(this.low != o.low)return this.low - o.low;
			return this.start - o.start;
		}
	}
	
	static class Word{
		int wID, low, start, end, length;
		Word(int wID, int low, int start, int end){
			this.wID = wID;
			this.low = low;
			this.start = start;
			this.end = end;
			this.length = end - start + 1;
		}
	}
	
	static class Node{
		int mID, start, end, length;
		public Node(int mID, int start, int end) {
			this.mID = mID;
			this.start = start;
			this.end = end;
			this.length = end - start + 1;
		}
	}
	static int cnt; //하나씩 늘어나는 빈공간 ID
	static int n, m; //가로, 세로
	static final int MAXWORD = 55001;
	static final int MAXVER = 200000;
	static boolean[] ver = new boolean[MAXVER]; //버전 죽었는지 살았는지 false 죽음 true 살음
	static Word[] word; //단어 정보를 관리 erase를 위함이 큼
	static TreeSet<Integer> have; // 탐색할 lengthPQ 인덱스 보관 내림차순해서 브레이크 걸어야함
	static PriorityQueue<Space>[] lengthPQ; // 우선순위는 Line을 따름
	static PriorityQueue<Space> PQ; // 단어길이 감당 가능한 빈공간들을 모은 큐
	static ArrayList<Node>[] node; //행 별 빈공간을 관리 erase를 위함이 큼
	
	
//	treeset으로 그 길이의 빈공간 보유중 표현 초반엔 M하나만 들어있음 내림차순으로 만들어서 단어보다 작아지면 스탑
//	그리고 priorityqueue[M] 만듬 초반엔 M에 몰려있음
//	단어가 들어오면 트리셋 순회하면서 길이보다 크다면 위에서 만든 곳에서 하나만 픽해옴 픽한건 최종 선택용 큐에 담음
//	그렇게 단어보다 긴 공간의 큐들에서 우선순위가 적용된 peek들이 모인것들 중 최상단 좌측을 픽(우선순위)
//	객체를 보고 그에 맞는 길이의 우선순위큐에서 poll함 start에 길이만큼 더하여 새로운 객체 만들고
//	길이에 맞는 위치 큐에 넣음 혹은 없어지거나 그리고 행마다
//	해쉬맵X 그냥 따로 간단한 객체 만들고 그걸 arraylist로 시작 : 끝 으로 만들어놓음 정보 관리도 해줘야함
//	write 시엔 객체의 스타트를 바꿔주거나 없애버림
//	지우는게 문제임 단어도 관리해야함 단어 클래스 만들어서 행, 시작 끝 관리하고 그 단어 지우는 쿼리 들어오면
//	그 행에 가서 객체 다 순회(최대 60개 부담X) 시작 - 끝, 끝 - 시작 매칭되는거 찾음
//	없으면 단어 정보와같은 빈공간 객체 생성 있다면 연결해줌
//	아니다 길이 M짜리 큐에는 매번 찾아가서 지우지말고 계속 늘어나는 길이 20만짜리 ver을 만들어서 최신 관리를 해줘야겠다.
	
	
	public void init(int N, int M)
	{
		cnt = 0; //하나씩 늘어나는 빈공간 ID
		n = N; //세로
		m = M;
		Arrays.fill(ver, false); //버전 죽었는지 살았는지 false 죽음 true 살음
		
		have = new TreeSet<Integer>((o1, o2) ->{
			return o2 - o1;
		}); // 탐색할 lengthPQ 인덱스 보관 내림차순해서 브레이크 걸어야함
		
		lengthPQ = new PriorityQueue[m + 1]; // 우선순위는 Line을 따름
		node = new ArrayList[N];
		word = new Word[MAXWORD]; //단어 정보를 관리 erase를 위함이 큼
		for (int i = 0; i < m + 1; i++) {
			lengthPQ[i] = new PriorityQueue<Space>();
		}
		have.add(M);
		for (int i = 0; i < N; i++) {
			node[i] = new ArrayList<Node>(); //행 별 빈공간을 관리 erase를 위함이 큼
			Space currS = new Space(cnt, i, 0, M - 1);
			ver[cnt] = true;
			lengthPQ[M].add(currS);
			Node currN = new Node(cnt++, 0, M - 1);
			node[i].add(currN);
		}
	}

	public int writeWord(int mId, int mLen)
	{
		PQ = new PriorityQueue<Space>(); // 단어길이 감당 가능한 빈공간들을 모은 큐
		for (int num : have) {
			if(num < mLen)break;
			while (!lengthPQ[num].isEmpty()) {
				Space curr = lengthPQ[num].peek();
				if (ver[curr.mID]) {
					PQ.add(curr);
					break;
				}
				lengthPQ[num].poll();
			}
		}
		if (PQ.isEmpty())return -1;
		Space target = PQ.poll();
		ver[target.mID] = false;
		word[mId] = new Word(mId, target.low, target.start, target.start + mLen - 1);
		int diff = target.length - mLen;
		for (int i = 0; i < node[target.low].size(); i++) {
			if (node[target.low].get(i).start == target.start) {
				node[target.low].remove(i);
				if (diff > 0) {
					have.add(diff);
					ver[cnt] = true;
					lengthPQ[diff].add(new Space(cnt, target.low, target.start + mLen, target.end));
					node[target.low].add(new Node(cnt++, target.start + mLen, target.end));
				}
			}
		}
		return target.low;
		
	}

	public int eraseWord(int mId)
	{
		if (word[mId] == null)return -1;
		int answer = word[mId].low;
		int newstart = word[mId].start;
		int newend = word[mId].end;
		int[] remove = new int[2];
		Arrays.fill(remove, -1);
		for (int i = 0; i < node[answer].size(); i++) {
			if (newstart != word[mId].start && newend != word[mId].end) break;
			if (word[mId].start - node[answer].get(i).end == 1) {
				newstart = node[answer].get(i).start;
				ver[node[answer].get(i).mID] = false;
				remove[0] = i;
			}
			if (node[answer].get(i).start - word[mId].end == 1) {
				newend = node[answer].get(i).end;
				ver[node[answer].get(i).mID] = false;
				remove[1] = i;
			}
		}
		
		if (remove[0] != -1 && remove[1] != -1) {
			if (remove[0] > remove[1]) {
				node[answer].remove(remove[0]);
				node[answer].remove(remove[1]);
			} else {
				node[answer].remove(remove[1]);
				node[answer].remove(remove[0]);
			}
		} else if (remove[0] != -1) {
			node[answer].remove(remove[0]);
		} else if (remove[1] != -1) {
			node[answer].remove(remove[1]);
		}
		
		int len = newend - newstart + 1;
		have.add(len);
		ver[cnt] = true;
		lengthPQ[len].add(new Space(cnt, answer, newstart, newend));
		node[answer].add(new Node(cnt++, newstart, newend));
		
		word[mId] = null;
		return answer;
	}

}
