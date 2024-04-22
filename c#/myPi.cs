        public static decimal MyPi(int n)

        /* Given a number n, write a function that returns PI to n decimal places.

            n will not be above 15, to keep this challenge simple.
            Round up the last digit if the next digit in PI is greater or equal to 5 (see second example above).
            The return value must be a number (add suffix -m to returning number), not a string. */

        {
            const decimal myPi = 3.1415926535897931M;
            return Math.Round(myPi, n);
        }