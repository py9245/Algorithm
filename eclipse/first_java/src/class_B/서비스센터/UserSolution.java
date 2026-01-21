package class_B.서비스센터;

import java.util.*;

class UserSolution {

    static int N, M;
    static int[] currentResult;

    static class Robot implements Comparable<Robot> {
        int rId, power;

        public Robot(int rId, int power) {
            this.rId = rId;
            this.power = power;
        }

        @Override
        public int compareTo(Robot o) {
            if (this.power != o.power) return o.power - this.power;
            return this.rId - o.rId;
        }
    }

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

    static Comparator<Task> normalComp = (o1, o2) -> {
        if (o1.grade != o2.grade) return o2.grade - o1.grade;
        return o1.arrivalTime - o2.arrivalTime;
    };

    static Comparator<Task> delayComp = (o1, o2) -> o1.arrivalTime - o2.arrivalTime;
    static Comparator<Task> workingComp = (o1, o2) -> o1.endTime - o2.endTime;

    static PriorityQueue<Robot> idleRobots;
    static PriorityQueue<Task> normalPQ;
    static PriorityQueue<Task> delayPQ;
    static PriorityQueue<Task> workingPQ;
    static PriorityQueue<Task> waitingPQ;

    static Robot[] robotInfo;
    static Task[] robotTask;

    public void init(int N, int M) {
        UserSolution.N = N;
        UserSolution.M = M;
        currentResult = new int[M + 1];

        idleRobots = new PriorityQueue<>();
        normalPQ = new PriorityQueue<>(normalComp);
        delayPQ = new PriorityQueue<>(delayComp);
        workingPQ = new PriorityQueue<>(workingComp);
        waitingPQ = new PriorityQueue<>(Comparator.comparingInt(t -> t.arrivalTime));

        robotInfo = new Robot[1001];
        robotTask = new Task[1001];
    }

    void update(int mTime) {
        while (!workingPQ.isEmpty() && workingPQ.peek().endTime <= mTime) {
            int now = workingPQ.peek().endTime;
            processFinishedTasks(now);
            processDelays(now);
            assignAllIdleRobots(now);
        }
        processDelays(mTime);
        assignAllIdleRobots(mTime);
    }

    void processFinishedTasks(int time) {
        while (!workingPQ.isEmpty() && workingPQ.peek().endTime == time) {
            Task finished = workingPQ.poll();
            currentResult[finished.grade] += (finished.endTime - finished.arrivalTime);

            Robot r = finished.assignedRobot;
            robotTask[r.rId] = null;

            if (robotInfo[r.rId] != null) {
                idleRobots.add(r);
            }
        }
    }

    void processDelays(int time) {
        while (!waitingPQ.isEmpty()) {
            Task t = waitingPQ.peek();

            if (t.assignedRobot != null) {
                waitingPQ.poll();
                continue;
            }

            if (t.arrivalTime + N <= time) {
                waitingPQ.poll();
                if (!t.isDelayed) {
                    t.isDelayed = true;
                    delayPQ.add(t);
                }
            } else {
                break;
            }
        }
    }

    void assignAllIdleRobots(int time) {
        while (!idleRobots.isEmpty()) {
            Robot r = idleRobots.poll();
            Task job = findBestTask(time);

            if (job != null) {
                job.startTime = time;
                job.assignedRobot = r;

                int duration = (job.workload + r.power - 1) / r.power;
                job.endTime = time + duration;

                workingPQ.add(job);
                robotTask[r.rId] = job;
            } else {
                idleRobots.add(r);
                break;
            }
        }
    }

    Task findBestTask(int time) {
        while (!delayPQ.isEmpty()) {
            Task t = delayPQ.peek();
            if (t.assignedRobot != null) {
                delayPQ.poll();
                continue;
            }
            return delayPQ.poll();
        }

        while (!normalPQ.isEmpty()) {
            Task t = normalPQ.peek();

            if (t.assignedRobot != null || t.isDelayed) {
                normalPQ.poll();
                continue;
            }

            if (t.arrivalTime + N <= time) {
                normalPQ.poll();
                t.isDelayed = true;
                delayPQ.add(t);
                return findBestTask(time);
            }

            return normalPQ.poll();
        }
        return null;
    }

    public void receive(int mTime, int mId, int mWorkload, int mGrade) {
        update(mTime);

        Task newTask = new Task(mTime, mId, mWorkload, mGrade);
        normalPQ.add(newTask);
        waitingPQ.add(newTask);

        assignAllIdleRobots(mTime);
    }

    public void add(int mTime, int rId, int mThroughput) {
        update(mTime);

        Robot newRobot = new Robot(rId, mThroughput);
        robotInfo[rId] = newRobot;
        idleRobots.add(newRobot);

        assignAllIdleRobots(mTime);
    }

    public int remove(int mTime, int rId) {
        update(mTime);

        Robot r = robotInfo[rId];
        if (r == null) return -1;

        int retId = -1;

        if (robotTask[rId] != null) {
            Task oldJob = robotTask[rId];
            retId = oldJob.id;

            workingPQ.remove(oldJob);
            robotTask[rId] = null;

            Task resetTask = new Task(oldJob.arrivalTime, oldJob.id, oldJob.workload, oldJob.grade);

            if (resetTask.arrivalTime + N <= mTime) {
                resetTask.isDelayed = true;
                delayPQ.add(resetTask);
            } else {
                resetTask.isDelayed = false;
                normalPQ.add(resetTask);
                waitingPQ.add(resetTask);
            }
        } else {
            idleRobots.remove(r);
        }

        robotInfo[rId] = null;
        assignAllIdleRobots(mTime);

        return retId;
    }

    public int evaluate(int mTime, int mGrade) {
        update(mTime);
        return currentResult[mGrade];
    }
}
