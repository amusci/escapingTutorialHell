        public static int gcd(int n1, int n2)
        /* Write a function that returns the greatest common divisor (GCD) of two integers.*/
        {

            if (n1 == 0) {

                return n2;

            }  
            else if (n2 == 0) {

                return n1;

            }
            else if (n1 == n2) {

                return n1;

            }

            else if (n1 > n2) {

                return gcd(n1 - n2, n2);



            }
            return gcd(n1, n2 - n1);


            }