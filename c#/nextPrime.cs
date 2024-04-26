        public static int NextPrime(int num) 
        /* Given an integer, create a function that returns the next prime. If the number is prime, return the number itself. */
        {
            if (num <= 2)
            {
                return 2;
            }

            if (IsPrime(num))
            {
                return num;
            }

            while (true)
            {
                num++;
                if (IsPrime(num))
                {
                    return num;
                }
            }
        }


        public static bool IsPrime(int n)

        {

            if (n <= 1)
            {

                return false;

            }
            if (n <= 3)
            {

                return true;

            }

            if (n % 2 == 0 || n % 3 == 0)
            {

                return false;

            }

            for (int i = 5; i * i <= n; i += 6)
            {

                if (n % i == 0 || n % (i+2)==0)
                {

                    return false;

                }


            }

            return true;



        }