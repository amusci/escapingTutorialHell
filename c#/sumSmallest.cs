        public static int SumSmallest(int[] values) 
        /* Create a function that takes an array of numbers and returns the sum of the two lowest positive numbers. */
        {

            return values.Where(x => x > 0).OrderBy(x => x).Take(2).Sum();

        }