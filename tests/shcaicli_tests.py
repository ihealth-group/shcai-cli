from shcaicli.api import SHCAi
import unittest
import os


class SHCAiTests(unittest.TestCase):
  def test_api_call(self):
    api_key = os.getenv('API_KEY')
    shc = SHCAi(api_key=api_key)
    cn = 'Paciente diagnosticado com has, nega dm. Em 20/09 iniciou QT para tratamento CA de mama'
    cn_inferred = shc.infer(cn=cn)
    pass
