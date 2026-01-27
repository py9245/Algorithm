package class_B.서비스센터;

import java.util.Arrays;
import java.util.PriorityQueue;

class UserSolution {
	
	static int n, m, lastTime;
	
	static class Order implements Comparable<Order>{
		int time, oID, work, grade;
		
		public Order(int time, int oID, int work, int grade) {
			this.time = time;
			this.oID = oID;
			this.work = work;
			this.grade = grade;
		}
		
		public int compareTo(Order o) {
			return this.time - o.time;
		}
	}
	
	static class Robot implements Comparable<Robot>{
		int rID, work;
		
		public Robot(int rID, int work) {
			this.rID = rID;
			this.work = work;
		}
		public int compareTo(Robot o) {
			if(this.work != o.work) return o.work - this.work;
			return this.rID - o.rID;
		}
	}
	
	static class Task implements Comparable<Task>{
		int endTime, oID, rID;
		boolean isDone;
		public Task(int endTime, int oID, int rID) {
			this.endTime = endTime;
			this.oID = oID;
			this.rID = rID;
			this.isDone = false; 
		}
		public int compareTo(Task o) {
			return this.endTime - o.endTime;
		}
	}
	
	static final int MAXROBOT = 1001;
	static final int MAXORDER = 50001;
	
	static int[] answer;
	
//	크기는 주문 최대 50001 안엔 Task
	static Task[] taskInfo;
	static PriorityQueue<Task> tasking;
	
//	크기는 로봇 ID 최대 1001 안엔 작업중인 주문ID, 주문 미할당 : 0, 삭제됐다면 : -1
	static int[] robotInfo;
	
 	static PriorityQueue<Order> beforePQ;
	static PriorityQueue<Order> normalPQ;
	static PriorityQueue<Order> waitPQ;
	
	void init(int N, int M) {
		lastTime = 0;
		n = N;
		m = M;
		answer = new int[M + 1];
		taskInfo = new Task[MAXORDER];
		tasking = new PriorityQueue<Task>();
		robotInfo = new int[MAXROBOT];
		Arrays.fill(robotInfo, -1);
		beforePQ = new PriorityQueue<Order>();
		normalPQ = new PriorityQueue<Order>((o1, o2) -> {
			if (o2.grade != o1.grade) return o2.grade - o1.grade;
			return o1.time - o2.time;
		});
		waitPQ = new PriorityQueue<Order>();
	}

//	할당된 시간 포함 온전히 다 일 완료한 다음 초가 endTime
	static void update(int target) {
		while (lastTime < target) {
			
		}
	}
	
	void receive(int mTime, int mId, int mWorkload, int mGrade) {
		beforePQ.add(new Order(mTime, mId, mWorkload, mGrade));
		update(mTime);
	}

	void add(int mTime, int rId, int mThroughput) {
		update(mTime);
//		예외적으로 robot 할당하는 로직 구현
	}

	int remove(int mTime, int rId) {
		update(mTime);
//		예외적으로 robot 삭제하는 로직 구현
		return 0;
	}

	int evaluate(int mTime, int mGrade) {
		update(mTime);
		return answer[mGrade];
	}
}
