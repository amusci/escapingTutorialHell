        public static bool KToK(string n, int k) 
        /*

        Write a function that returns true if k^k == n for input (n, k) and return false otherwise.

        */
        {

            BigInteger stringToLong = BigInteger.Parse(n);

            return BigInteger.Pow(k,k) == stringToLong;
            
        }