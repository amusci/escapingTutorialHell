        public static int LargestGap(int[] arr)
        /*
        Given an array of integers, return the largest gap between elements of the sorted version of that array.

        Here's an illustrative example. Consider the array:

        [9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]

        ... which, after sorting, becomes the array:

        [0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]

        ... so that we now see that the largest gap in the array is the gap of 11 between 9 and 20.
        */

        {
            int currentSum = 0;
            int previousSum = 0;

            Array.Sort(arr);

            

            for (int i = 0; i < arr.Length - 1; i++)
            {

                currentSum = arr[i + 1] - arr[i];
                Console.WriteLine(currentSum + " current");
                Console.WriteLine(previousSum + " previous");
                if (currentSum > previousSum)
                {

                    previousSum = currentSum;

                }

            }

            return previousSum;
            
            
        }	