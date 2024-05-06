        public static string OddishOrEvenish(int num)
        /*
        Create a function that determines whether a number is Oddish or Evenish.

        A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even.
        
        If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

        For example, OddishOrEvenish(121) should return "Evenish", since 1 + 2 + 1 = 4. OddishOrEvenish(41) should return "Oddish", since 4 + 1 = 5.
        */

        {
            int sum = 0;

            for (int i = num; i > 0; i /= 10)
            {

                int digit = i % 10;
                sum += digit;

            }

            if (sum % 2 == 0)
            {

                return "Evenish";

            }
            else 
            {

                return "Oddish";
            }

        }	