        public static int Major(int[] arr) 
        /*
        Create a function that takes an integer array and return the biggest between positive sum, negative sum, or 0s count. The major is understood as the greatest absolute.

        arr = {1,2,3,4,0,0,-3,-2}, the function has to return 10, because:

        Positive sum = 1+2+3+4 = 10
        Negative sum = (-3)+(-2) = -5
        0s count = 2 (there are two zeros in array)
        */
        {
            int positiveSum = 0;
            int negativeSum = 0;
            int zerosCount = 0;

            for (int i = 0; i < arr.Length; i++)
            {

                if (arr[i] > 0)
                {

                    positiveSum += arr[i];

                }

                else if (arr[i] < 0)
                {

                    negativeSum += arr[i];

                }

                else 
                {

                    zerosCount++;

                }


            }

            int absNegativeSum = Math.Abs(negativeSum);
            if (absNegativeSum > positiveSum)
            {

                string absNegativeSumToString = "-" + absNegativeSum.ToString();
                int negativeBackToInt = int.Parse(absNegativeSumToString);
                return negativeBackToInt;


            }
            else
            {

                int max = Math.Max(positiveSum, zerosCount);
                return max;

            }


        }