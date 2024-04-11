        public static bool LargestSwap(int num)
        /* Create a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.*/
        {

            string numString = num.ToString();
            string swapped = numString[1].ToString() + numString[0];
            int swappedInt = int.Parse(swapped);

            return num >= swappedInt;
                
        }