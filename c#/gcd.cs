        public static int gcd(int n1, int n2)
        /* Write a function that returns the greatest common divisor (GCD) of two integers.*/
        {

            while (n1 != 0 && n2 != 0) {


                if (n1 > n2) {

                    return gcd(n1, n1-n2);

                } else {

                    return gcd(n2, n2- n1);

                }
            }

            if (n1 == 0) {

                return n2;

            } else {


                return n1;

            }

        }