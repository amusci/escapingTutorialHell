        public static double[] FindLargest(double[][] values) 

        /* Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.*/
        {

            List<double> list = new List<double>();

            foreach (double[] valueArray in values)
            {
                double largest = valueArray.Max();
                list.Add(largest);


            }

            return list.ToArray();

        }