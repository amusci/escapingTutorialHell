        public static bool ValidatePIN(string pin) 
        /* ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
        
        Your task is to create a function that takes a string and returns true if the PIN is valid and false if it's not.*/

        {

            if (pin.Length != 4 && pin.Length != 6) {

                return false;

            }
            char[] charArray = pin.ToCharArray();

            foreach (char ch in charArray) {

                if (!char.IsLetter(ch)) {


                    return false;

                }


            

            }

            return true;
        }