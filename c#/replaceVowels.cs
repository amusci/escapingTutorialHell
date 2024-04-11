        public static string ReplaceVowels(string str, string ch)
        {
            char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
            StringBuilder result = new StringBuilder(str);

            for (int i = 0; i < str.Length; i++)
            {

                if (Array.IndexOf(vowels, char.ToLower(result[i])) != -1) 
                {

                    result[i] = ch[0];

                } 

            }
            
            return result.ToString();    
        }