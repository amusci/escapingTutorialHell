        public static double[] CumulativeSum(double[] arr) 
        /*  Create a function that takes an array of numbers and returns an array where each number is the sum of itself + all previous numbers in the array. */
        {

            double[] result = new double[arr.Length];
            double ressyBOY = 0;

            for (int i = 0; i < arr.Length; i++) {


                ressyBOY += arr[i];
                result[i] = ressyBOY;


            }

            return result;

        }