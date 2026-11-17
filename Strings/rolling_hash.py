# Source: https://github.com/kazari4/atcoder-library/blob/main/Strings/rolling_hash.py


class RollingHash:
    """半開区間 [left, right) の部分文字列を扱うローリングハッシュ。"""

    MOD = (1 << 61) - 1
    DEFAULT_BASE = 911382323

    def __init__(self, text: str, base: int = DEFAULT_BASE) -> None:
        if not 1 < base < self.MOD:
            raise ValueError("base は 2 以上 MOD - 1 以下で指定してください")

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
        """元の文字列の長さを返す。"""
        return self._length

    def get(self, left: int, right: int) -> int:
        """区間 [left, right) のハッシュを返す。不正な区間は IndexError。"""
        if not 0 <= left <= right <= self._length:
            raise IndexError("区間は 0 <= left <= right <= 文字列長 を満たす必要があります")
        return (
            self._prefix[right]
            - self._prefix[left] * self._powers[right - left]
        ) % self.MOD

    def same(self, left1: int, right1: int, left2: int, right2: int) -> bool:
        """2区間の長さとハッシュが一致するかを判定する。"""
        first = self.get(left1, right1)
        second = self.get(left2, right2)
        return right1 - left1 == right2 - left2 and first == second
