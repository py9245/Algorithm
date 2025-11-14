#####main.py
import sys

from solution import init, add, remove, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_REMOVE = 300
CMD_CALC = 400

def run1():
	q = int(input())
	okay = False

	mIdArr = []
	sIdArr = []
	eIdArr = []
	mIntervalArr = []

	for i in range(q):
		inputarray = input().split()
		cmd = int(inputarray[0])

		if cmd == CMD_INIT:
			inputarray = input().split()
			n = int(inputarray[1])
			k = int(inputarray[3])
			for _ in range(k):
				tinfo = input().split()
				mIdArr.append(int(tinfo[1]))
				sIdArr.append(int(tinfo[3]))
				eIdArr.append(int(tinfo[5]))
				mIntervalArr.append(int(tinfo[7]))

			init(n, k, mIdArr, sIdArr, eIdArr, mIntervalArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = input().split()
			mId = int(inputarray[1])
			sId = int(inputarray[3])
			eId = int(inputarray[5])
			mInterval = int(inputarray[7])
			add(mId, sId, eId, mInterval)
		elif cmd == CMD_REMOVE:
			inputarray = input().split()
			mId = int(inputarray[1])
			remove(mId)
		elif cmd == CMD_CALC:
			inputarray = input().split()
			sId = int(inputarray[1])
			eId = int(inputarray[3])
			ans = int(input().split()[1])
			ret = calculate(sId, eId)
			# print(f"ret : {ret}")
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run1() else 0
		print("#%d %d" % (testcase, score), flush = True)
