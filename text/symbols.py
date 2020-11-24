_accent_letters = {
"a" :  ["a`","a~","a^"],
"ą" : ["ą~","ą^"],
"e" : ["e`","e~","e^"],
"ę" : ["ę~","ę^"],
"ė" : ["ė~","ė^"],
"i" : ["i`","i~","i^"],
"į" : ["į~","į^"],
"y" : ["y~","y^"],
"o" : ["o`","o~","o^"],
"u" : ["u`","u~","u^"],
"ų" : ["ų~","ų^"],
"ū" : ["ū~","ū^"],
"l" : ["l~"],
"m" : ["m~"],
"n" : ["n~"],
"r" : ["r~"]
}

def get_valid_symbol_ids(valid_symbol_cases):
	#defaults
	pho = ['Į', 'Ų', 'C', 'Č']
	_pad = '_'
	_special = '-'
	_punctuation = '!\'(),-.:;? '
	_accent = ''
	_letters = 'AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpQqRrSsŠšTtUuŲųŪūVvZzŽž'
	
	if "lowercase_only" in valid_symbol_cases:
		_letters = ''.join([x[0] for x in zip(_letters, _letters.upper()) if x[0] != x[1]])
	if "accent_chars" in valid_symbol_cases:
		_accent += '~^`'
	if "otimized_phonemes" in valid_symbol_cases:
		for ph in pho:
			_letters = _letters.replace(ph,"").replace(ph.lower(),"")

	_letters = list(_letters)
	if "accent_letters" in valid_symbol_cases:
		for letter in _letters:
			if letter in _accent_letters:
				insert_index = _letters.index(letter) +1
				_letters[insert_index:insert_index] = _accent_letters[letter]

	return [_pad] + list(_special) + list(_punctuation) + list(_accent) + _letters

def get_symbol_len(valid_symbol_cases):
	return len(get_valid_symbol_ids(valid_symbol_cases))
