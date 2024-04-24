			{
                string result = "";
                char [] charArray = word.ToCharArray();
                Array.Reverse(charArray);

                for (int i = 0; i < charArray.Length; i++)
                {
                    switch(charArray[i])

                    {

                        case 'a':
                            result += '0';
                            break;
                        case 'e':
                            result += '1';
                            break;
                        case 'i':
                            result += '2';
                            break;
                        case 'o':
                            result += '2';
                            break;
                        case 'u':
                            result += '3';
                            break;

                        default:
                            result += charArray[i];
                            break;
                        
                    }

                    

                }

                return result + "aca";



			}