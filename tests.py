# To run the tests, comment or remove lines 36 to 78 (included) from caesarCipher.py

import unittest
import caesarCipher

class TestcaesarCipher(unittest.TestCase):
    decoded_message = "hey there! this is an example of a caesar cipher."
    coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh."
    offset = 10
    def test_decoder(self):
        self.assertEqual(caesarCipher.decoder(self.coded_message, self.offset), self.decoded_message)
    
    def test_coder(self):
        self.assertEqual(caesarCipher.coder(self.decoded_message, self.offset), self.coded_message)

    # Actually, this test is a test to test caesarCipher.decoder because caesarCipher.decoderWithoutOffset works by calling caesarCipher.decoder method
    def test_decoderWithoutOffset(self):
        printed_messages = []
        for message in range(1,26):
            printed_messages.append(caesarCipher.decoder(self.coded_message, message))
        self.assertIn(self.decoded_message, printed_messages)
        

# Run the tests
unittest.main()