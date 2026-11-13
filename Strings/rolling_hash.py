# Source: https://github.com/kazari4/atcoder-library/blob/main/Strings/rolling_hash.py
"""Substring hashes for a string, usable as a standalone AtCoder submission snippet."""


class RollingHash:
    """Polynomial rolling hash with half-open substring ranges [left, right)."""

    MOD = (1 << 61) - 1
    DEFAULT_BASE = 911382323

    def __init__(self, text: str, base: int = DEFAULT_BASE) -> None:
        if not 1 < base < self.MOD:
            raise ValueError("base must be between 2 and MOD - 1")

        self._length = len(text)
        self.base = base
        self._powers = [1] * (self._length + 1)
        self._prefix = [0] * (self._length + 1)

        for i, char in enumerate(text):
            self._powers[i + 1] = self._powers[i] * base % self.MOD
            self._prefix[i + 1] = (
                self._prefix[i] * base + ord(char) + 1
            ) % self.MOD

    def __len__(self) -> int:
        """Return the length of the original string."""
        return self._length

    def get(self, left: int, right: int) -> int:
        """Return the hash of [left, right); raise IndexError for an invalid range."""
        if not 0 <= left <= right <= self._length:
            raise IndexError("substring range is out of bounds")
        return (
            self._prefix[right]
            - self._prefix[left] * self._powers[right - left]
        ) % self.MOD

    def same(self, left1: int, right1: int, left2: int, right2: int) -> bool:
        """Test whether two ranges have equal lengths and hashes."""
        first = self.get(left1, right1)
        second = self.get(left2, right2)
        return right1 - left1 == right2 - left2 and first == second
