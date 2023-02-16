import re

# constants
appendixes = [
  'appendix',
  'annex',
  'document',
  'addendum'
]
norms = [
  'ISO',
  'EN',
  'EN ISO',
  'ANSI',
  'AINSI',
  'ASTM',
  'NFPA',
  'CIBSE',
  'IBC',
  'BS',
  'DIN',
  'ASHRAE'
]
acronyms = r'\s[A-Z\/]{2,}\s'

def find_appendixes(str):
  result = set()
  for app in appendixes:
    exp = r'\s[a-zA-Z0-9]+\s{}\s[a-zA-Z0-9]+\s'.format(app)
    matches = re.findall(exp, str)
    for match in matches:
      result.add(match.strip())
  return result

def find_norms(str):
  result = set()
  for norm in norms:
    exp = r'{}\s*[0-9]+'.format(norm)
    matches = re.findall(exp, str)
    for match in matches:
      result.add(match.strip())
  return result

def find_acronyms(str):
  result = set()
  exp = acronyms
  matches = re.findall(exp, str)
  for match in matches:
    result.add(match.strip())
  return result