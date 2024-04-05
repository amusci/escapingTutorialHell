    public static bool SameCase(string str)
    {
    public static bool SameCase(string str)
    {

        char[] ch = str.ToCharArray();
        if (ch.All(char.IsLower) == true || ch.All(char.IsUpper) == true)
        {

            return true;

        }

        return false;

    }
    }