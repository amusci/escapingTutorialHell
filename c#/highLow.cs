        public static string HighLow(string str) 
        /* Create a function that accepts a string of space separated numbers and returns the highest and lowest number (as a string). */
        {
            string[] stringArrayNum = str.Split(' ');

            List<int> numList = new List<int>();

            foreach (string stringomode in stringArrayNum) {
                numList.Add(int.Parse(stringomode));
                


            }

            int[] numArray = numList.ToArray();
            string max = numArray.Max().ToString();
            string min = numArray.Min().ToString();
            return max + " " + min;

        
        }