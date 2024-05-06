        public static string Reverse(string str) 
        /*

        Write a function that takes a string of one or more words as an argument and returns the same string, but with all five or more letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

        */
        {
            string result = "";
            string[] words = str.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            
            for (int i = 0; i < words.Length; i++)
            {

                if (words[i].Length >= 5)
                {
                    char[] letters = words[i].ToCharArray();
                    Array.Reverse(letters);
                    result += new string(letters);
                }
                else
                {

                    result += words[i];

                }

                if (i < words.Length - 1)
                {

                    result += " ";

                }

                
            }

            return result;

        
        }