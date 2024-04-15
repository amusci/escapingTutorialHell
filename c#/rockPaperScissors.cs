        public static bool rockPaperScissors(string user)
        /* Input a string, and have Computer choose randomly Rock, Scissors, Paper. Return true if user wins, false if computer wins or ties */
        {
            string[] computerChoices = ["Rock", "Scissors", "Paper"];
            
            Random rnd = new Random();

            int randomNumber = rnd.Next(0, computerChoices.Length);
            string compChoice = computerChoices[randomNumber];
            Console.WriteLine(randomNumber);

            Console.WriteLine(compChoice);
            
            if (user == compChoice) {

                return false;

            }

            else if (user == "Rock" && compChoice == "Paper") {

                return false;

            }

            else if (user == "Rock" && compChoice == "Scissors") {

                return true;
            }


            else if (user == "Paper" && compChoice == "Rock") {

                return true;

            }

            else if (user == "Paper" && compChoice == "Scissors") {

                return false;
            }
            else if (user == "Scissors" && compChoice == "Rock") {

                return false;

            }

            else if (user == "Scissors" &&  compChoice == "Paper") {

                return true;

            }

        
        return false;
            

        }