        /*
       Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

        Given a censored string and a string of the censored vowels, return the original uncensored string.
        */
        {

            string result = "";
            int count = 0;

            for (int i = 0; i < txt.Length; i++)
            {

                if (txt[i] == '*')
                {

                    result += vowels[count];
                    Console.WriteLine(result);
                    count ++;
                }
                else
                {

                    result += txt[i];
                    Console.WriteLine(result);

                }

            }

            return result;



        }