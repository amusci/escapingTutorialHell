        public static string Bomb(string txt)

        /* Create a function that finds the word "bomb" in the given string (not case sensitive).
        
        If found, return "Duck!!!", otherwise, return "There is no bomb, relax.".*/
        {

            string txtLower = txt.ToLower();
            string[] words = txtLower.Split(' ');
            Console.WriteLine(words[7]);

            foreach(string str in words)
            {

                string clean = str.Trim('.', ',', '!', '?');
                if (clean == "bomb") {

                    return "Duck!!!";
                }

            }

            return "There is no bomb, relax.";


            
        }