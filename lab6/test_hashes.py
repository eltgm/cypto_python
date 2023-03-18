import unittest

from MD5 import MD5
from SHA1 import SHA1


class TestHashes(unittest.TestCase):
    def test_md5(self):
        expectations = {
            "": "d41d8cd98f00b204e9800998ecf8427e",
            "a": "0cc175b9c0f1b6a831c399e269772661",
            "abc": "900150983cd24fb0d6963f7d28e17f72",
            "message digest": "f96b697d7cb7938d525a2f31aaf161d0",
            "abcdefghijklmnopqrstuvwxyz": "c3fcd3d76192e4007dfb496cca67e13b",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": "d174ab98d277d9f5a5611c2c9f419d9f",
            "12345678901234567890123456789012345678901234567890123456789012345678901234567890": "57edf4a22be3c955ac49da2e2107b67a",
        }

        for string, md5_hash in expectations.items():
            with self.subTest(string=string, md5_hash=md5_hash):
                self.assertEqual(MD5.hash(string), md5_hash)

    def test_sha1(self):
        expectations = {
            "": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "a": "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8",
            "abc": "a9993e364706816aba3e25717850c26c9cd0d89d",
            "message digest": "c12252ceda8be8994d5fa0290a47231c1d16aae3",
            "abcdefghijklmnopqrstuvwxyz": "32d10c7b8cf96570ca04ce37f2a19d84240d3a89",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": "761c457bf73b14d27e9e9265c46f4b4dda11f940",
            "12345678901234567890123456789012345678901234567890123456789012345678901234567890": "50abf5706a150990a08b2c5ea40fa0e585554732",
        }

        for string, sha1_hash in expectations.items():
            with self.subTest(string=string, sha1_hash=sha1_hash):
                self.assertEqual(SHA1.hash(string), sha1_hash)
