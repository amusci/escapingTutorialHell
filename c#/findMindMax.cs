    public static double[] FindMinMax(double[] values) 
    /* Create a function that takes an array of numbers and return both the minimum and maximum numbers, in that order. */
    {

      double max = values.Max();
      double min = values.Min();
      
      return new double[] {min, max};
				
    }