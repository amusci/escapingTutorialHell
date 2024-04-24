        public static string Century(int year)
        /* Create a function that takes in a year and returns the correct century. 
            All years will be between 1000 and 2010.
            The 11th century is between 1001 and 1100.
            The 18th century is between 1701-1800.
        */
        {

            double century = year / 100;

            if (century <= 20)
            {

                return Math.Ceiling(century) + "th century";

            }
            else
            {

                return Math.Ceiling(century) + "st century";

            }

        }