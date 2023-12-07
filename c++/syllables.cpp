int numberSyllables(std::string word) {


    int len = word.size();
    int counter = 0;

    for (int i = 0; i < len; i++) {
        if (word[i] ==  '-') {
            counter = counter+1;

        }

    }
	return counter + 1;


}