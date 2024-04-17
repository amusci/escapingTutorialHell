        public static int[] CountPosSumNeg(double[] arr) 
        /* Create a function that takes an array of positive and negative numbers.
        
        Return an array where the first element is the count of positive numbers and the second element is the sum of negative numbers.

        CountPosSumNeg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]
        
        */



        {
            int count = 0;
            int negSum = 0;


            
            

            foreach (int n in arr) {

                if (n < 0) {

                    negSum += n;


                }

                else {

                    count++;


                }


            }

            int[] result = {count, negSum};
            return result;
        
        }