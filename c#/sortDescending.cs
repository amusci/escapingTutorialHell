        public static int SortDescending(int num) 
        /* Create a function that takes any non-negative number as an argument and return it with its digits in descending order. Descending order is when you sort from highest to lowest.*/

        {
            int result = 0;
            char[] charArrayNum = num.ToString().ToCharArray();

            int[] intArray = charArrayNum.Select(c => (int) Char.GetNumericValue(c)).ToArray();

            Array.Sort(intArray);
            Array.Reverse(intArray);
            
            for (int i = 0; i < intArray.Length; i++) {

                result += intArray[i] * Convert.ToInt32(Math.Pow(10, intArray.Length-i-1));

            }


            return result;

        
        }