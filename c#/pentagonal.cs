        public static int pentagonal(int num)

        /*

        Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

        In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.

        Return the number of dots that exist in the whole pentagon on the Nth iteration.
        */



        {
            return (5 * num * num - 5 * num + 2) / 2;


            
        }