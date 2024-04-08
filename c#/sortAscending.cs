        public static int[] SortNumsAscending(int[] arr)
        /*Create a function that takes an array of numbers and returns a new array, sorted in ascending order (smallest to biggest).

    Sort the numbers array in ascending order.
    If the function's argument is null, an empty array, or undefined; return an empty array.
    Return a new array of sorted numbers. */
        {

          if (arr == null || arr.Length == 0)
          {

            return new int[0];

          }


          Array.Sort(arr);

          return arr;
  
        }