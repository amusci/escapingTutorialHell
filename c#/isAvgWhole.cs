    public static bool IsAvgWhole(int[] arr)
    /*Create a function that takes an array as an argument and returns true or false depending
    on whether the average of all elements in the array is a whole number or not.*/
    {
      double sum = 0;
      double avg;
      foreach (int i in arr)
      {
        sum += i;

      }
      avg = sum / arr.Length;
      if (Math.Truncate((double)avg) == avg) 
      {
        return true;

      }
      return false;


    }