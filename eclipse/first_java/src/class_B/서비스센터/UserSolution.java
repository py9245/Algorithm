package class_B.서비스센터;

import java.util.*;

class UserSolution {

    static final int INF = Integer.MAX_VALUE;
    static int N, M;
    static int[] currentResult;

    // 로봇 클래스
    static class Robot implements Comparable<Robot> {
        int rId, power;

        public Robot(int rId, int power) {
            this.rId = rId;
            this.power = power;
        }

        @Override
        public int compareTo(Robot o) {
            // 1. 처리량 높은 순, 2. ID 작은 순
            if (this.power != o.power) return o.power - this.power;
            return this.rId - o.rId;
        }
    }

    // 작업 클래스
    static class Task {
        int id, arrivalTime, workload, grade;
        int startTime, endTime;
        boolean isDelayed;
        Robot assignedRobot;

        public Task(int time, int id, int workload, int grade) {
            this.arrivalTime = time;
            this.id = id;
            this.workload = workload;
            this.grade = grade;
            this.isDelayed = false;
        }
    }

    // --- Comparators ---
    static Comparator<Task> normalComp = (o1, o2) -> {
        if (o1.grade != o2.grade) return o2.grade - o1.grade; // 등급 내림차순
        return o1.arrivalTime - o2.arrivalTime; // 시간 오름차순
    };

    static Comparator<Task> delayComp = (o1, o2) -> {
        return o1.arrivalTime - o2.arrivalTime; // 시간 오름차순
    };

    static Comparator<Task> workingComp = (o1, o2) -> {
        return o1.endTime - o2.endTime; // 종료시간 오름차순
    };

    // --- 전역 자료구조 ---
    static PriorityQueue<Robot> idleRobots;
    static PriorityQueue<Task> normalPQ;
    static PriorityQueue<Task> delayPQ;
    static PriorityQueue<Task> workingPQ;
    static ArrayDeque<Task> waitingDeque; // 지연 감시용

    static Robot[] robotInfo; // ID로 로봇 찾기
    static Task[] robotTask;  // ID로 작업 찾기

    public void init(int N, int M) {
        this.N = N;
        this.M = M;
        currentResult = new int[M + 1];

        idleRobots = new PriorityQueue<>();
        normalPQ = new PriorityQueue<>(normalComp);
        delayPQ = new PriorityQueue<>(delayComp);
        workingPQ = new PriorityQueue<>(workingComp);
        waitingDeque = new ArrayDeque<>();

        robotInfo = new Robot[1001];
        robotTask = new Task[1001];
    }

    // [핵심 1] 시간을 mTime까지 완전히 흐르게 함 (순서: 완료 -> 지연 -> 할당)
    void update(int mTime) {
        // mTime 이전에 끝나는 작업 + mTime 정각에 끝나는 작업 모두 처리
        while (!workingPQ.isEmpty() && workingPQ.peek().endTime <= mTime) {
            int now = workingPQ.peek().endTime;
            
            // 1. 작업 완료 처리
            processFinishedTasks(now);
            
            // 2. 지연 처리
            processDelays(now);
            
            // 3. 빈 로봇 재할당 (배치 처리)
            assignAllIdleRobots(now);
        }
        
        // Loop가 끝난 후, mTime 시점의 잔여 처리
        processDelays(mTime);
        // 여기서 assignAllIdleRobots(mTime)을 호출해도 되지만, 
        // API 함수들(receive 등)에서 어차피 호출하므로 생략 가능.
        // 하지만 안전하게 호출해두는 것이 좋음.
        assignAllIdleRobots(mTime);
    }

    // 완료된 작업 처리
    void processFinishedTasks(int time) {
        while(!workingPQ.isEmpty() && workingPQ.peek().endTime == time) {
            Task finished = workingPQ.poll();
            currentResult[finished.grade] += (finished.endTime - finished.arrivalTime);
            
            Robot r = finished.assignedRobot;
            robotTask[r.rId] = null;
            
            // 로봇이 삭제되지 않았다면 대기열 복귀
            if (robotInfo[r.rId] != null) {
                idleRobots.add(r);
            }
        }
    }

    // 지연 상태 전이 (Waiting -> DelayPQ)
    void processDelays(int time) {
        while (!waitingDeque.isEmpty()) {
            Task t = waitingDeque.peek();
            // 이미 할당된 건 덱에서 제거
            if (t.assignedRobot != null) {
                waitingDeque.poll();
                continue;
            }
            // 지연 기준: 접수시간 + N <= 현재시간
            if (t.arrivalTime + N <= time) {
                waitingDeque.poll();
                if (!t.isDelayed) {
                    t.isDelayed = true;
                    delayPQ.add(t);
                }
            } else {
                break; // 시간순이므로 탈출
            }
        }
    }

    // 가용 로봇들에게 일감 분배
    void assignAllIdleRobots(int time) {
        while (!idleRobots.isEmpty()) {
            Robot r = idleRobots.poll();
            Task job = findBestTask(time);
            
            if (job != null) {
                job.startTime = time;
                job.assignedRobot = r;
                // 소요 시간 계산 (올림)
                int duration = (job.workload + r.power - 1) / r.power;
                job.endTime = time + duration;
                
                workingPQ.add(job);
                robotTask[r.rId] = job;
            } else {
                idleRobots.add(r);
                break; // 일감 없으면 종료
            }
        }
    }

    // 최우선 작업 찾기 (재귀 탐색)
    Task findBestTask(int time) {
        // 1. 지연 큐 확인
        while (!delayPQ.isEmpty()) {
            Task t = delayPQ.peek();
            if (t.assignedRobot != null) {
                delayPQ.poll();
                continue;
            }
            return delayPQ.poll();
        }
        
        // 2. 일반 큐 확인
        while (!normalPQ.isEmpty()) {
            Task t = normalPQ.peek();
            
            // 이미 처리된 놈 삭제
            if (t.assignedRobot != null || t.isDelayed) {
                normalPQ.poll();
                continue;
            }
            
            // [중요] JIT Check: 꺼내보니 지연되었으면 DelayPQ로 보내고 처음부터 다시
            if (t.arrivalTime + N <= time) {
                normalPQ.poll();
                t.isDelayed = true;
                delayPQ.add(t);
                return findBestTask(time); // 재귀 호출
            }
            
            return normalPQ.poll();
        }
        return null;
    }

    // --- API 구현 ---

    public void receive(int mTime, int mId, int mWorkload, int mGrade) {
        // 1. 내부 시뮬레이션 (1,2,3단계 수행)
        update(mTime);
        
        // 2. 요청 처리 (4단계)
        Task newTask = new Task(mTime, mId, mWorkload, mGrade);
        normalPQ.add(newTask);
        waitingDeque.add(newTask);
        
        // 3. 새 일감이 들어왔으니 즉시 할당 시도
        assignAllIdleRobots(mTime);
    }

    public void add(int mTime, int rId, int mThroughput) {
        update(mTime);
        
        Robot newRobot = new Robot(rId, mThroughput);
        robotInfo[rId] = newRobot;
        idleRobots.add(newRobot);
        
        // 새 로봇이 들어왔으니 할당 시도
        assignAllIdleRobots(mTime);
    }

    public int remove(int mTime, int rId) {
        update(mTime); // 중요: 먼저 mTime 작업들을 완료시켜서 로봇을 IDLE로 만들어야 함
        
        Robot r = robotInfo[rId];
        if (r == null) return -1;
        
        int retId = -1;
        
        // 로봇이 작업 중이라면 (update를 거쳤는데도 작업 중이라면 진짜 중간에 빼는 것)
        if (robotTask[rId] != null) {
            Task oldJob = robotTask[rId];
            retId = oldJob.id;
            
            workingPQ.remove(oldJob); // O(N) 삭제
            oldJob.assignedRobot = null;
            robotTask[rId] = null;
            
            // [핵심] 진행상황 초기화 = 새 객체 생성 (Deep Copy)
            // 기존 객체를 재사용하면 Ghost 상태 등과 꼬일 수 있음
            Task resetTask = new Task(oldJob.arrivalTime, oldJob.id, oldJob.workload, oldJob.grade);
            
            // 지연 여부 즉시 판단하여 적절한 큐에 삽입
            if (resetTask.arrivalTime + N <= mTime) {
                resetTask.isDelayed = true;
                delayPQ.add(resetTask);
            } else {
                resetTask.isDelayed = false;
                normalPQ.add(resetTask);
                // waitingDeque는 건드리지 않아도 findBestTask가 JIT로 처리해줌
            }
        } else {
            // 대기 중인 로봇 삭제
            idleRobots.remove(r);
        }
        
        robotInfo[rId] = null;
        
        // 작업이 뱉어졌거나 로봇이 사라졌으니 다시 정렬
        assignAllIdleRobots(mTime);
        
        return retId;
    }

    public int evaluate(int mTime, int mGrade) {
        update(mTime);
        return currentResult[mGrade];
    }
}