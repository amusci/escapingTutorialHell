	public static int[] MultiplyByLength(int[] arr)
  /*Create a function to multiply all of the values in an array by the amount of values in the given array.*/

	  {
      int[] result = new int[arr.Length];

      int n = arr.Length;

      for (int i = 0; i < n; i++) {

        result[i] = arr[i] * n;

      }

      return result;

	  }