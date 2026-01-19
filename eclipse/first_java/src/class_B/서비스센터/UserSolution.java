package class_B.서비스센터;

import java.util.Comparator;
import java.util.PriorityQueue;

class UserSolution {
	
	static int n, m;
	static int lasttime;
	static int[] result;
	
	static class Robot implements Comparable<Robot>{
		int id, val;
		
		public Robot(int id, int val) {
			this.id = id;
			this.val = val;
		}
		
		public int compareTo(Robot o) {
			if (this.val != o.val) return o.val - this.val;
			return this.id - o.id;
		}
	}
	
	static class Order implements Comparable<Order>{
		int startTime, endTime, cost, rank, grade, rId, oId;
		
		public Order(int time, int oId, int cost, int grade) {
			this.oId = oId;
			this.grade = grade;
			this.startTime = time;
			this.cost = cost;
			this.rank = grade;
		}
		
		@Override
		public int compareTo(Order o) {
			if (this.rank != o.rank) return o.rank - this.rank;
			return this.startTime - o.startTime;
		}
	}
	

	static PriorityQueue<Order> orders;
	static PriorityQueue<Order> tasking;
	static PriorityQueue<Robot> robot;
	static Comparator<Order> workComp = (o1, o2) -> {
		if(o1.endTime != o2.endTime) return Integer.compare(o1.endTime, o2.endTime);
		return o1.rId - o2.rId;
	};
	
	void init(int N, int M) {
		n = N;
		m = M;
		lasttime = 0;
		result = new int[M + 1];
		orders = new PriorityQueue<Order>();
		tasking = new PriorityQueue<Order>(workComp);
		robot = new PriorityQueue<Robot>();
	}

	void receive(int mTime, int mId, int mWorkload, int mGrade) {
		
	}

	void add(int mTime, int rId, int mThroughput) { 
	}

	int remove(int mTime, int rId) {
		return 0;
	}

	int evaluate(int mTime, int mGrade) {
		return 0;
	}
}
