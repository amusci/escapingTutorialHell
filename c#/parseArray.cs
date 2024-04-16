        public static string[] ParseArray (object[] arr)
        /* Create a function that takes an array of integers and strings, converts integers to strings, and returns the array as a string array.*/
        {

            List<string> result = new List<string>();

            foreach (object obj in arr)
            {

                result.Add(obj.ToString());

            }


            return result.ToArray();

            
        }