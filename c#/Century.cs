        public static string Century(int year)
        /* Create a function that takes in a year and returns the correct century. 
            All years will be between 1000 and 2010.
            The 11th century is between 1001 and 1100.
            The 18th century is between 1701-1800.
        */
        {

            int century = (year - 1) / 100 + 1;

            string suffix = "";

            switch (century) 
            {

                case 11:
                case 12:
                case 13:
                case 14:
                case 15:
                case 16:
                case 17:
                case 18:
                case 19:

                    suffix = "th";
                    break;
                default:
                    switch(century % 10)
                    {

                        case 1:
                            suffix = "st";
                            break;
                        case 2:
                            suffix = "nd";
                            break;
                        case 3:
                            suffix = "rd";
                            break;
                        default:
                            suffix = "th";
                            break;

                    }
                    break;


            }

            return century + suffix + " century";



        }