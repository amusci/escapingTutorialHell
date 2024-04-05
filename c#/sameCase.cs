    public static bool SameCase(string str)
    {
        char[] ch = str.ToCharArray();
        int upperCount = 0;
        int lowerCount = 0;
        int s = str.Length;

        for (int i = 0; i < s; i++)
        {
            if (char.IsUpper(ch[i]))
            {
                upperCount ++;
            }
            else if (char.IsLower(ch[i]))
            {
                lowerCount++;
            }
        }
        if (upperCount != s && lowerCount != s)
        {
            return false;
        }
        else 
        {
            return true;
        }
    }