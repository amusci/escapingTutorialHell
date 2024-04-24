        public static int Potatoes(string potato)
        /* Create a function to return the amount of potatoes there are in a string. */
        {
            int count = 0;
            int index = -1;
            string poetaytoe = "potato";

            while ((index = potato.IndexOf(poetaytoe, index + 1)) != -1)
            {

                count ++;

            }

            return count;
            
        }