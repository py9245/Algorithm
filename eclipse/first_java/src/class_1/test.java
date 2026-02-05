package class_1;



public class test {
	static class TestClass {
		void exe(int[] arr) {
			System.out.println(func(func(5, 5), 5, func(arr)));
		}

		int func(int a, int b) {
			return a + b;
		}

		int func(int a, int b, int c) {
			return a - b;
		}

		int func(int[] c) {
			int s = 0;
			for (int i = 0; i < c.length; i++) {
				s += c[i];
			}
			return s;
		}
	}

	public static void main(String[]args) {
		int[] a = {1, 2, 3, 4, 5};
		TestClass t = new TestClass();
		t.exe(a);
	}
}