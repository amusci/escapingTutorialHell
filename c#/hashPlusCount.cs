        public static int[] HashPlusCount(string s)
        /* Create a function that returns the number of hashes and pluses in a string. */
        {
            
            int hashCount = 0;
            int plusCount = 0;
            

            for (int i = 0; i < s.Length; i++)
             {

                if (s[i] == '+') {

                    plusCount += 1;


                }
                else if (s[i] == '#') {

                    hashCount += 1;    

            }

            
            
            }


            int[] result = { hashCount, plusCount };
            return result;
        }