package class_B.cafe2;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

class UserSolution
{
	static int n, orderCnt, createdAt;
	
	static class Order{
		int oID, m, orderAt, ver;
		int[] need, have;
		boolean isCancle, isFinished;
		
		public Order(int oID, int m, int[] need, int[] have) {
			this.oID = oID;
			this.m = m;
			this.need = need;
			this.have = have;
		}
	}
	
	static class Node implements Comparable<Node>{
		int id, remain,orderAt, ver;
		
		public Node(Order o) {
			this.id = o.oID;
			this.remain = o.m;
			this.orderAt = o.orderAt;
			this.ver = o.ver;
		}
		public int compareTo(Node o) {
			if (this.remain != o.remain) return o.remain - this.remain;
			return this.orderAt - o.orderAt;
		}
	}
	
	static HashMap<Integer, Order> orderInfo;
	static PriorityQueue<Node> hurryPQ;
	static ArrayDeque<Order>[] deque;
    
	
	
	public void init(int N)
    {
		n = N;
		orderCnt = 0;
		createdAt = 0;
		orderInfo = new HashMap<Integer, Order>();
		hurryPQ = new PriorityQueue<Node>();
		deque = new ArrayDeque[N + 1];
		for (int i = 0; i < N + 1; i++) {
			deque[i] = new ArrayDeque<Order>();
		}
        return;
    }
	
	
    public int order(int mID, int M, int mBeverages[])
    {	
//    	주문 들어오면 orderCnt ++
    	orderCnt++;
    	
    	int[] need = new int[n + 1];
    	for (int idx = 0; idx < M; idx++) {
    	    int b = mBeverages[idx];
    	    need[b]++;
    	}
    	Order curr = new Order(mID, M, need, new int[n + 1]);
    	curr.orderAt = createdAt++;
    	curr.ver = 0;
    	orderInfo.put(mID, curr);
    	for (int b = 1; b <= n; b++) {
    	    if (need[b] > 0) deque[b].add(curr);
    	}
    	hurryPQ.add(new Node(curr));
//    	if (curr.oID == 686850365) {
//    		System.out.println(Arrays.toString(mBeverages));
//    		System.out.println(Arrays.toString(curr.need));
//    	}
        return orderCnt;
    }

    static boolean CheckFinished(Order o) {
    	if(o.m == 0) {
    		o.isFinished = true;
    		orderCnt--;
    		return true;
    	}
    	return false;
    }

    public int supply(int mBeverage)
    {
    	while (!deque[mBeverage].isEmpty()) {
    		Order curr = deque[mBeverage].poll();
    		if (curr.isCancle || curr.isFinished ||
    				curr.need[mBeverage] == curr.have[mBeverage]) continue;
    		curr.have[mBeverage]++;
    		curr.m--;
    		curr.ver++;
    		if (!CheckFinished(curr)) {
    			hurryPQ.add(new Node(curr));
    			if (curr.have[mBeverage] != curr.need[mBeverage])deque[mBeverage].addFirst(curr);
    		}
    		return curr.oID;
    	}
    	
        return -1;
    }

    public int cancel(int mID)
    {	
    	Order curr = orderInfo.get(mID);
    	if (curr.isFinished) return 0;
    	if (curr.isCancle) return -1;
    	curr.ver++;
    	curr.isCancle = true;
    	orderCnt--;
    	int answer = curr.m;
    	for (int i = 1; i < n + 1; i++) {
			if (curr.have[i] > 0) {
				for (int j = 0; j < curr.have[i]; j++) {
					supply(i);
				}
			}
		}
        return answer;
    }

    public int getStatus(int mID)
    {	
    	Order curr = orderInfo.get(mID);
    	if (curr.isFinished) return 0;
    	if (curr.isCancle) return -1;
        return curr.m;
    }

    Solution.RESULT hurry()
    {
        Solution.RESULT res = new Solution.RESULT();
        Node[] temp = new Node[5];
        int cnt = 0;
        while(!hurryPQ.isEmpty() && cnt < 5) {
        	Node curr = hurryPQ.poll();
        	Order currO = orderInfo.get(curr.id);
        	if(curr.ver != currO.ver || currO.isCancle || currO.isFinished) continue;
        	temp[cnt++] = curr;
        }
        for (int i = 0; i < cnt; i++) {
			res.IDs[i] = temp[i].id;
			hurryPQ.add(temp[i]);
		}
        res.cnt = cnt;
        
        return res;
    }
}
// order는 id가 최대 10억이니 해쉬맵으로 구현하여 최신상태를 관리함
// 오더는 가장 먼저 받은 순서대로이니 arraDeque를 종류별로 10개 만듬
// 주문이 1,4,5 음료로 이루어진게 온다고 하면 new Order만들고 1,4,5 category, orderInfo에 다 들어감
// order객체는 int[] need 10개 짜리, int[] have, oID, orderAt, isfinished, ver
// hurry는 pq 만듬 객체는 order, orderAt, ver
// ver는 항상 hashmaporder로 최신관리 ver가 바뀌는 상황은 주문취소, 주문 완료, 긴급주문(hurry)
// static으로 주문 받을때마다 갯수 카운팅 완료되면 -- 취소되면 --
// 여기까지 설계하고 일단 구현시작 설계 20분
// order는 기존에 없던 oID 보장함
// n은 음료의 종류 음료의 종류는 최대 3 ~ 10
// 먼저 들어온 주문은 oID가 아닌 함수 호출된 순서 먼저 호출이 먼저 들어옴
//supply 는 음료가 들어오는것 모든 order에 해당 음료가 비포함되어있으면 보관이 아닌 버림
//cancle oID주문 취소되기 전 남은 음료의 개수 반환 취소 시 가지고 있는 음료들 다은 Order에게 재배치
//cancle은 이미 받은 주문임을 보장함, orderInfo.get(oID).isFinished면 -1 하면 될듯(제조완료는 취소가 안됨)
// getStatus 주문 mID의 남은 음료 개수 반환 주문완료시 0 취소된건 -1
// hurry로 만들어진 5개의 목록은 다른 함수에 지장이 없음 그냥 반환만하는거지 우선으로 처리해야하는 주문이 된건 아님
// 남은 음료의 갯수가 가장 많은 주문이 우선 만약 여러개라면 가장 먼저 받은 주문


