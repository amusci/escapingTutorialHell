        public static bool IsValid(string zip)
        /* Zip codes consist of 5 consecutive digits. Given a string, write a function to determine whether the input is a valid zip code. A valid zip code is as follows:

        Must only contain numbers (no non-digits allowed).
        Must not contain any spaces.
        Must not be greater than 5 digits in length.*/
        {

            if (zip.Length > 5)
            {

                return false;

            }
            for (int i = 0; i < zip.Length; i++) {

                if (!Char.IsDigit(zip[i])) {

                    return false;
            }

        }

        return true;

        }