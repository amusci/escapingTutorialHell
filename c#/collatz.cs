        public static int collatz(int num)

        /*Consider the following operation on an arbitrary positive integer:

        If n is even -> n / 2
        If n is odd -> n * 3 + 1
        */
        {

            if (num % 2 == 0) {

                return num / 2;

            }

            else 

                return (num * 3) + 1;



        }