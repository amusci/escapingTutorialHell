        public static bool isFactorial(int n) 
        /*
        Create a function that checks if a given integer is exactly the factorial of an integer or not. true if it is, false otherwise.
        */
        {

            int sum = 1;
            int i = 1;

            while (sum < n)
            {

                i++;
                sum *= i;

            }
            return sum == n;

        }