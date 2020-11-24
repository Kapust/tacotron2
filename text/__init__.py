import re
from text import cleaners

from text.symbols import get_valid_symbol_ids

_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')

def text_to_sequence(text, cleaner_names,valid_symbol_cases):
  valid_symbols = get_valid_symbol_ids(valid_symbol_cases)
  if 'lowercase_only' in valid_symbol_cases and 'lowercase' not in cleaner_names:
    cleaner_names.append('lowercase')
  if "otimized_phonemes" in valid_symbol_cases and 'phonemes' not in cleaner_names:
    cleaner_names.append('phonemes')
  if "accent_letters" in valid_symbol_cases and 'accent_chars' in cleaner_names:
    cleaner_names.remove('accent_chars')

  _symbol_to_id = ({s: i for i, s in enumerate(valid_symbols)})
  
  sequence = _symbols_to_sequence(_clean_text(text, cleaner_names),_symbol_to_id,valid_symbol_cases)

  return sequence

def sequence_to_text(sequence,valid_symbol_cases):
  valid_symbols = get_valid_symbol_ids(valid_symbol_cases)
  _id_to_symbol = {i: s for i, s in enumerate(valid_symbols)}

  result = ''
  for symbol_id in sequence:
    if symbol_id in _id_to_symbol:
      s = _id_to_symbol[symbol_id]
      result += s
  return result

def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text


def _symbols_to_sequence(symbols,vs,vsc):
  if "accent_letters" in vsc:
    arr = []
    for i in range(len(symbols)):
      if i+1 < len(symbols) and symbols[i+1] in ['`','~','^']:
        s = symbols[i] + symbols[i+1]
        i+=2
  else:
    s = symbols[i]
    if s in vs:
      arr.append(vs[s])
  return arr
  else:
    return [vs[s] for s in symbols if s in vs]
