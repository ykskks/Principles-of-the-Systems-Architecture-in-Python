from __future__ import annotations


# p30: 値の範囲を制限してプログラムをわかりやすく安全にする
class Quantity:
    MIN = 1
    MAX = 100

    def __init__(self, value: int) -> None:
        if value < Quantity.MIN:
            raise ValueError(f"不正: {Quantity.MIN} 未満")
        if value > Quantity.MAX:
            raise ValueError(f"不正: {Quantity.MAX} 超")
        self.value = value

    def __eq__(self, other: Quantity) -> bool:
        return self.value == other.value

    def __add__(self, other: Quantity) -> Quantity:
        if not self.can_add(other):
            raise ValueError(f"不正: 合計が{Quantity.MAX} 超")
        added = self.add_value(other)
        return Quantity(added)

    def add_value(self, other: Quantity):
        return self.value + other.value

    def can_add(self, other: Quantity) -> bool:
        added = self.add_value(other)
        return added <= Quantity.MAX


# p34: 値オブジェクトは不変にする
class Quantity:
    MIN = 1
    MAX = 100

    def __init__(self, value: int) -> None:
        if value < Quantity.MIN:
            raise ValueError(f"不正: {Quantity.MIN} 未満")
        if value > Quantity.MAX:
            raise ValueError(f"不正: {Quantity.MAX} 超")
        self._value = value

    @property  # read only
    def value(self) -> int:
        return self._value

    def __eq__(self, other: Quantity) -> bool:
        return self.value == other.value

    def __add__(self, other: Quantity) -> Quantity:
        if not self.can_add(other):
            raise ValueError(f"不正: 合計が{Quantity.MAX} 超")
        added = self.add_value(other)
        return Quantity(added)

    def add_value(self, other: Quantity):
        return self.value + other.value

    def can_add(self, other: Quantity) -> bool:
        added = self.add_value(other)
        return added <= Quantity.MAX
