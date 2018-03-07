def string_has_keyword(string, keyword_list):
	for keyword in keyword_list:
		if keyword in string:
			return keyword

	return None
