        public static string ToScottishScreaming(string str) 
        /* A strong Scottish accent makes every vowel similar to an "e", so you should replace every vowel with an "e". Additionally, it is being screamed, so it should be in block capitals.

            Create a function that takes a string and returns a string.*/


        {

            string[] vowels = {"A","E","I","O","U"};
            List<string> result = new List<string>();
            char[] characters = str.ToUpper().ToCharArray();

            foreach (char c in characters) {

                if (vowels.Contains(c.ToString())) {

                    result.Add("E");


                } else {


                    result.Add(c.ToString());


                }
                

            }

            return string.Join("", result);


        }