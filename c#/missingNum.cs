        public static int MissingNum(int[] arr)
        /* Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number. */

        {

            Array.Sort(arr);
            for (int i = 0; i < arr.Length; i++) 
            {
                Console.WriteLine(arr[i]);
                Console.WriteLine(i + 1);

                if (arr[i] != i + 1) {

                    return i + 1;
                }

            }

            return arr.Length + 1;

        }