        public static int Potatoes(string potato)
        /* Create a function to return the amount of potatoes there are in a string. */
        {

            return Regex.Matches(potato, "potato").Count;

            
        }