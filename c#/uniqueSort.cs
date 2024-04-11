        public static double[] UniqueSort(double[] arr)

        /* Given an array of numbers, write a function that returns an array that...

            Has all duplicate elements removed.
            Is sorted from least value to greatest value.

        */

        {

            double[] ans = arr.Distinct().ToArray();

            Array.Sort(ans);


            return ans;

        }