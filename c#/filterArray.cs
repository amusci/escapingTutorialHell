        public static int[] FilterArray(object[] arr)
        /* Create a function that takes an array of non-negative integers and strings and return a new array without the strings.*/

        {

            List <int> result = new List<int>();

            for (int i = 0; i < arr.Length; i++)
            {

                if (arr[i].GetType() == typeof(int))
                {

                    result.Add((int)arr[i]);

                }
            }

            return result.ToArray();

            
        }