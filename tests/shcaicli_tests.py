from shcaicli.api import SHCAi
import unittest
import os


class SHCAiTests(unittest.TestCase):
  def test_api_call(self):
    api_key = os.getenv('API_KEY')
    shc = SHCAi(api_key=api_key)
    cn = 'Paciente diagnosticado com has, nega dm.'
    cn_inferred = shc.infer(cn=cn)
    cn_inferred = next(cn_inferred)
    pass
