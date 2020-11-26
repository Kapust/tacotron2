_whitespace_re = re.compile(r'\s+')

pho_dict = {
'Į' : 'Y',
'Ų' : 'Ū',
'C' : 'Ts',
'Č' : 'Tš',
'TSH' :'ch',
'Ą~':'A~',
'Ą^':'A^',
'Ę~':'E~',
'Ę^':'E^',
'I^':'I`',
'U^':'U`',
}

def remove_accent_chars(text):
  return ''.join([c for c in text if c not in '`^~'])

def lowercase(text):
  return text.lower()

def phonemes(text):
  for pho in pho_dict:
    text = text.replace(pho,pho_dict[pho]).replace(lowercase(pho),lowercase(pho_dict[pho]))
  return text

def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)

def basic_cleaners(text):
  text = collapse_whitespace(text)
  return text