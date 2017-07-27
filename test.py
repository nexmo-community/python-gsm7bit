#! /usr/bin/env python3

import unittest
import gsm7bit

class TestStringMethods(unittest.TestCase):
    def __init__(self):
        self.c = gsm7bit.Converter()
        self.chars = """@£$¥èéùìòÇØøÅåΔ_ΦΓΛΩΠΨΣΘΞ1^{}\[~]|€ÆæßÉ !"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà""" 
        self.codes = '000102030405060708090B0C0E0F101112131415161718191AB0A1B141B281B291B2F1B3C1B3D1B3E1B401B651C1D1E1F202122232425262728292A2B2C2D2E2F303132333435363738393A3B3C3D3E3F404142434445464748494A4B4C4D4E4F505152535455565758595A5B5C5D5E5F606162636465666768696A6B6C6D6E6F707172737475767778797A7B7C7D7E7F'

    def test_encode(self):
        self.assertEqual(c.encode(self.chars), self.codes)

    def test_encode_fail(self):
        with self.assertRaises(CharError):
            c.encode('This string should fail •')
    
    def test_decode(self):
        self.assertEqual(c.decode(self.codes), self.chars)
        


if __name__ == '__main__':
    unittest.main()

