from shcaicli.api import SHCAi
import unittest
import os


class SHCAiTests(unittest.TestCase):
  def test_api_call(self):
    api_key = os.getenv('API_KEY')
    shc = SHCAi(api_key=api_key, tokens_mode=True)
    with open('/Users/rafaelmorais/Downloads/Amosta_Nota_clinica.txt', 'r') as amostra:
      next(amostra)
      cns = []
      for line in amostra:
        id_cn, cn_text = line.split('\t')
        cns.append(cn_text)

      cn_inferred = shc.infer(cns=cns[0:50])
      pass
