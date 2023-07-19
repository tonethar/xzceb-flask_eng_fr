import unittest

from translator import english_to_french, french_to_english


class TestEtoF(unittest.TestCase): 
  def test1(self): 
    self.assertEqual(english_to_french("Hello"), "Bonjour")
    self.assertNotEqual(english_to_french("Yes"), "Oui-Oui")

class TestFtoE(unittest.TestCase): 
  def test1(self): 
    self.assertEqual(french_to_english("Bonjour"), "Hello")
    self.assertEqual(french_to_english("Oui"), "Yes")


unittest.main()

# print(englishToFrench("Hello"))
# print(frenchToEnglish("Bonjour"))
