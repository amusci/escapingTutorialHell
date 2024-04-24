        public static bool IsSymmetrical(int num) 

        /* 
        Create a function that takes a number as an argument and returns true or false depending on whether the number is symmetrical or not.
        
        A number is symmetrical when it is the same as its reverse.
        */

        {

            string numToString = num.ToString();
            int half = numToString.Length / 2;
            string firstHalf = numToString.Substring(0, half);
            string secondHalf = numToString.Substring(numToString.Length - half);
            
            char[] secondHalfToCharArray = secondHalf.ToCharArray();
            Array.Reverse(secondHalfToCharArray);
            string reversedSecondHalf = new string(secondHalfToCharArray);


            return firstHalf.Equals(reversedSecondHalf);

        }