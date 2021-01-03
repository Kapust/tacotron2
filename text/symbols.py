_kirciuotos_raides = {
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

_fonemos = {
'regular' :['į', 'ų', 'c', 'č'],
'accent' : ['ą~','ą^','ę~','ę^','i^','į','į~','į^','u^','ų','ų~','ų^','c','č'],
'add' : ['ch']
}

def get_valid_symbol_ids(cleaners):
	_simboliai = ' ?!.'
	_balsiai = 'AaĄąEeĘęĖėIiĮįYyOoUuŲųŪū'
	_priebalsiai_sprogstamieji = 'BbDdGgPpTtKk'
	_priebalsiai_snypsciantieji = 'CcČčSsŠšZzŽžFfHh'
	_priebalsiai_kiti = 'JjLlMmNnRrVv'
	_kirciai = '~^`'
	
	_raidynas = _balsiai + _priebalsiai_sprogstamieji + _priebalsiai_snypsciantieji + _priebalsiai_kiti

	if "lowercase" in cleaners:
		_raidynas = ''.join([x[0] for x in zip(_raidynas, _raidynas.upper()) if x[0] != x[1]])

	if "accent_chars" in cleaners:
		_raidynas += _kirciai

	_raidynas = list(_raidynas) + list(_simboliai)

	if "accent_letters" in cleaners:
		for raide in _raidynas:
			if raide in _kirciuotos_raides:
				insert_index = _raidynas.index(raide) + 1
				if "lowercase" not in cleaners:
					kirciuotos_su_didz = []
					for kirciuota_raide in _kirciuotos_raides[raide]:
						kirciuotos_su_didz.append(kirciuota_raide.upper())
						kirciuotos_su_didz.append(kirciuota_raide)
					_raidynas[insert_index:insert_index] = kirciuotos_su_didz
				else:
					_raidynas[insert_index:insert_index] = _kirciuotos_raides[raide]

	if "phonemes" in cleaners:
		if "accent_letters" in cleaners:
			_raidynas = [x for x in _raidynas if x.lower() not in _fonemos['accent']]
		else:
			_raidynas = [x for x in _raidynas if x.lower() not in _fonemos['regular']]
		insert_index = _raidynas.index('h') + 1
		_raidynas[insert_index:insert_index] = _fonemos['add']

	return _raidynas 

def get_symbol_len(cleaners):
	return len(get_valid_symbol_ids(cleaners))
