        public static string NameShuffle(string str)
        /* Create a function that accepts a string (of a person's first and last name) and returns a string with the first and last name swapped.*/
        {
            string[] result = str.Split(' ');

            return $"{result[1]} {result[0]}";

            
        }