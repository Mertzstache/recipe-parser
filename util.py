def string_has_keyword(string, keyword_list):
	for keyword in keyword_list:
		if keyword in string.lower():
			return keyword

	return None

def string_has_keywords_multiple(string, keyword_list):
	keywords_in_string = []

	for keyword in keyword_list:
		if keyword in string.lower():
			keywords_in_string.append(keyword)
			string = string.replace(keyword, '')

	return keywords_in_string
