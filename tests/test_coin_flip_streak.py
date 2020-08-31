import unittest

from automateboringstuff.coin_flip_streak import as_heads_or_tails


class CoinFlipStreak(unittest.TestCase):
    def test_should_return_heads_given_one(self):
        result = as_heads_or_tails(1)
        self.assertTrue('H', result)


if __name__ == '__main__':
    unittest.main()
