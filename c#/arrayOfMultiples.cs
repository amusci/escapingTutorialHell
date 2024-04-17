        public static int[] ArrayOfMultiples(int num, int length)
         Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length. 
        
        {

            int[] ans = new int[length];



            for (int i = 0; i  length; i++)

            {

                ans[i] = num  (i + 1);

            }

            return ans;


            
        }