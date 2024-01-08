private static void middleString(String str) {

    int len = str.length();

    if (len % 2 == 0) {
        System.out.println("There is no middle");

    } else {

        int mid = len / 2;
        System.out.println(str.charAt(mid));



    }


}