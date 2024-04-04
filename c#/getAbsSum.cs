   using System;
   
   
    public static int GetAbsSum(int[] arr)

    /* Take an array of integers (positive or negative or both) and return the sum of the absolute value of each element. */
    {
        int ans = 0;
        for (int i = 0; i < arr.Length; i++)
        {

            ans += Math.Abs(arr[i]);

        }

        return ans;

    }
  }