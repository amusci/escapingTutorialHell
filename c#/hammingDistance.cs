    public static int HammingDistance(string str1, string str2)
    /* Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference. */
    {

      int count = 0;

      for (int i = 0; i < str1.Length; i++) {

        if (str1[i] != str2[i]) {

          count++;

        }
      }
      return count;
    }