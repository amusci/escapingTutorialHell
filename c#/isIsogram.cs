        public static bool IsIsogram(string str) 
        /* An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either true or false depending on whether or not it's an "isogram". */

        
        {

            HashSet<char> seen = new HashSet<char>();

            foreach(char c in str.ToLower()) {

                if (char.IsLetter(c)) {

                    if (seen.Contains(c)) {

                        return false;


                    }
                    
                    seen.Add(c);

                }

            }

            return true;


        }