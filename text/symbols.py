def get_valid_symbol_ids(valid_symbol_cases):
	#defaults
	pho = [
	'Į', # y
	'Ų', # ū
	'C', # ts
	'Č' # tš
	]
	_pad = '_'
	_special = '-'
	_punctuation = '!\'(),-.:;? '
	_accent = ''
	_letters = 'AĄBCČDEĘĖFGHIĮYJKLMNOPQRSŠTUŲŪVZŽaąbcčdeęėfghiįyjklmnoprsštuųūvzž'
	
	if "lowercase_only" in valid_symbol_cases:
		_letters = ''.join([x[0] for x in zip(_letters, _letters.upper()) if x[0] != x[1]])
	if "accent_chars" in valid_symbol_cases:
		_accent += '~^`'
	if "otimized_phonemes" in valid_symbol_cases:
		for ph in pho:
			_letters = _letters.replace(ph,"").replace(ph.lower(),"")

	return [_pad] + list(_special) + list(_punctuation) + list(_letters) + list(_accent)

def get_symbol_len(valid_symbol_cases):
	return len(get_valid_symbol_ids(valid_symbol_cases))
