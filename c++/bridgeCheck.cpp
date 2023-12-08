bool isSafeBridge(std::string s) {

	int len = s.size();
	for (int i = 0; i < len; i++) {
		if (s[i] == ' ') {
			return false;
		}

	} return true;


}