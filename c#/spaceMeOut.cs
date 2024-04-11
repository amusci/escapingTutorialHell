        public static string SpaceMeOut(string str)
        /* Create a function that takes a string and returns a string with spaces in between all of the characters.*/
        {

            string result = "";

            for (int i = 0; i < str.Length; i++) {
                if  (i > 0) {

                    result += " ";


                }

                result += str[i];

            }

            return result;

            
        }