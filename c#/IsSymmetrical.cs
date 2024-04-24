        public static bool IsSymmetrical(int num) 

        /* 
        Create a function that takes a number as an argument and returns true or false depending on whether the number is symmetrical or not.
        
        A number is symmetrical when it is the same as its reverse.
        */

        {

            string numToString = num.ToString();

            return numToString.SequenceEqual(numToString.Reverse());

        }