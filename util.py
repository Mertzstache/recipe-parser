def string_has_keyword(string, keyword_list):
	for keyword in keyword_list:
		if keyword in string.lower():
			return keyword

	return None

def string_has_keywords_multiple(string, keyword_list):
	keywords_in_string = []
	copy_of_string = string[:].lower()
	for keyword in keyword_list:
		if keyword in copy_of_string:
			keywords_in_string.append(keyword)
			copy_of_string = copy_of_string.replace(keyword, '')
	return keywords_in_string

def string_has_keywords_any(string, keyword_list):
	keywords_in_string = []
	copy_of_string = string[:].lower()

	for keyword in keyword_list:
		for k in keyword.split(' '):
			if k in copy_of_string:
				keywords_in_string.append(k)
				copy_of_string = copy_of_string.replace(keyword, '')
	return keywords_in_string
