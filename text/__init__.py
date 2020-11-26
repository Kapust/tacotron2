import re
from text import cleaners

from text.symbols import get_valid_symbol_ids

def text_to_sequence(text,cleaner_names):
  valid_symbols = get_valid_symbol_ids(cleaner_names)

  if 'accent_letters' not in cleaner_names and 'accent_chars' not in cleaner_names:
    cleaner_names.append('remove_accent_chars')

  _symbol_to_id = ({s: i for i, s in enumerate(valid_symbols)})
  
  sequence = _symbols_to_sequence(_clean_text(text, cleaner_names),_symbol_to_id,cleaner_names)

  return sequence

def sequence_to_text(sequence,cleaner_names):
  valid_symbols = get_valid_symbol_ids(cleaner_names)
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


def _symbols_to_sequence(symbols,vs,cleaner_names):
  arr = []
  skip_next = False
  for i in range(len(symbols)):
    if skip_next:
      skip_next = False
      continue
    s = symbols[i]
    if "accent_letters" in cleaner_names and i+1 < len(symbols) and symbols[i+1] in ['`','~','^']:
      s = symbols[i] + symbols[i+1]
      skip_next = True
    if "phonemes" in cleaner_names and i+1 < len(symbols) and symbols[i] == "c" and symbols[i+1] =="h":
      s = symbols[i] + symbols[i+1]
      skip_next = True
    if s in vs:
      arr.append(vs[s])
  return arr
