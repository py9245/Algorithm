#####main.py
import sys
from solution import init, pickup, reset, getBest
import time



CMD_INIT = 100
CMD_PICKUP = 200
CMD_RESET = 300
CMD_GET_BEST = 400

MAX_M = 2000

mSeed = 0
def pseudo_rand():
	global mSeed
	mSeed = (mSeed * 1103515245 + 12345) % 2147483647
	return mSeed >> 16


mXs = [0 for _ in range(MAX_M)]
mYs = [0 for _ in range(MAX_M)]

def run1():
	global mSeed

	mNos = [0] * 5

	Q, mSeed = map(int, input().split())
	okay = False

	for q in range(Q):
		input_iter = iter(input().split())
		cmd = int(next(input_iter))
		if cmd == CMD_INIT:
			N = int(next(input_iter))
			M = int(next(input_iter))
			L = N // 10
			for i in range(M):
				mXs[i] = pseudo_rand() % N
				mYs[i] = pseudo_rand() % N
			init(N, M, L, mXs, mYs)
			okay = True
		elif cmd == CMD_PICKUP:
			while True:
				mSX = pseudo_rand() % N
				mSY = pseudo_rand() % N
				mEX = pseudo_rand() % N
				mEY = pseudo_rand() % N
				if mSX != mEX or mSY != mEY:
					break
			ret = pickup(mSX, mSY, mEX, mEY)
			ans = int(next(input_iter))
			if ret != ans:
				okay = False
		elif cmd == CMD_RESET:
			mNo = int(next(input_iter))
			res = reset(mNo)
			x = int(next(input_iter))
			y = int(next(input_iter))
			mdist = int(next(input_iter))
			rdist = int(next(input_iter))
			if res.mX != x or res.mY != y or res.mMoveDistance != mdist or res.mRideDistance != rdist:
				okay = False
		elif cmd == CMD_GET_BEST:
			getBest(mNos)
			for i in range(5):
				ans = int(next(input_iter))
				if mNos[i] != ans:
					okay = False
		else:
			okay = False
	return okay

st = time.time()
sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
	score = MARK if run1() else 0
	print("#%d %d" % (tc, score))
print(time.time() - st)