	public static double ParallelResistance(double[] arr) 
  /*ParallelResistance({6, 3, 6}) ➞ 1.5

  // 1/RTotal = 1/6 + 1/3 + 1/6
  // 1/RTotal = 2/3
  // RTotal = 3/2 = 1.5*/
    {
      double result = 0;

      foreach (double d in arr) {

        result += 1 / d;

      }
      return Math.Round(1 / result,1);
	  }