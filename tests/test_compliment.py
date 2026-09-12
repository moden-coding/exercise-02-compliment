#!/usr/bin/env python3

import contextlib
import io
import unittest
from unittest.mock import patch

from src.compliment import main


class Compliment(unittest.TestCase):

    def test_first(self):
        with patch('builtins.input', side_effect=['France']) as prompt:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                main()
            output = buf.getvalue().strip()
            self.assertEqual(
                output, "I have heard that France is a beautiful country.",
                msg="With input 'France', the program should print exactly "
                    "'I have heard that France is a beautiful country.'. Got %r."
                    % (output,))
            prompt.assert_called_once_with("What country are you from? ")

    def test_second(self):
        with patch('builtins.input', side_effect=['country-where-you-live']) as prompt:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                main()
            output = buf.getvalue().strip()
            self.assertEqual(
                output,
                "I have heard that country-where-you-live is a beautiful country.",
                msg="With input 'country-where-you-live', the program should "
                    "print 'I have heard that country-where-you-live is a "
                    "beautiful country.'. Got %r." % (output,))


if __name__ == '__main__':
    unittest.main()
