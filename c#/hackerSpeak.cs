
    public static string HackerSpeak(string str)
    {
        string ans = "";
        int n = str.Length;
        for(int i = 0; i < n; i++) {

            char ch = str[i];

            switch(ch)
            {
                case 'a':
                    ans += '4';
                    break;
                case 'e':
                    ans += '3';
                    break;
                case 'i':
                    ans += '1';
                    break;
                case 'o':
                    ans += '0';
                    break;
                case 's':
                    ans += '5';
                    break;
                default:
                    ans += ch;
                    break;


            }

    
        }

        return ans;
			
    }