        public static bool CheckPerfect(int num) 

        /* 
        Create a function that tests whether or not an integer is a perfect number.
        
        A perfect number is a number that can be written as the sum of its factors, (equal to sum of its proper divisors) excluding the number itself.

        For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6.
        
        Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.


        */

        {

            int sum = 1;
            int i = 2;

            while (i * i <= num)
            {

                if (num % i == 0)
                {

                    sum += i + (num/i);

                }
                i += 1;

            }

        if (sum == num && num != 1) return true;
        else return false;
    

        }