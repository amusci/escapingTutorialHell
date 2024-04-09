	public static string Repetition(string txt, int n)
    /*Create a recursive function that takes two parameters and repeats the string n number of times.
    The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.*/
    {
    if (n == 1)
    {
    return txt;
    }
    return txt + Repetition(txt, n - 1);
    }