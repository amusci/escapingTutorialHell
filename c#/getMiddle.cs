        public static string GetMiddle(string str) 
        /* Create a function that takes a string and returns the middle character(s).
        
        If the word's length is odd, return the middle character. If the word's length is even, return the middle two characters. */
        {


            if (str.Length % 2  != 0)
            {

                return str.Substring(str.Length / 2, 1);

            }

            return str.Substring((str.Length / 2) - 1, 2);
            
        }