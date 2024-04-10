        public static double Mean(int[] arr) 
        /*Create a function that takes an array of numbers and returns the mean (average) of all those numbers.*/
        {
            double result = 0;

            for (int i = 0; i < arr.Length; i++) {

                result += arr[i];

            }

            return Math.Round(result / arr.Length,2);
        
        }