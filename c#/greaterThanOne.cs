        public static bool GreaterThanOne(string str)

        /* Given a fraction as a string, return whether or not it is greater than 1 when evaluated. */
        
        {
            string[] split = str.Split('/');
            int num1 = Int32.Parse(split[0]);
            int num2 = Int32.Parse(split[1]);

            if (num1 > num2) {

                return true;


            } else {

                return false;

            }
            
        }