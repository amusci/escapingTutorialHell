        public static double[] FindLargest(double[][] values) 

        /* Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each. */

        {

            return values.Select(x => x.Max()).ToArray();
                
        }