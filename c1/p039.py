from __future__ import annotations

from typing import List, Tuple


class Customer:
    pass


# p40: コレクション型を扱うロジックを専用クラスに閉じ込める
class Customers:
    def __init__(self, customers: List[Customer]) -> None:
        self.customers = customers

    def add(self, customer: Customer) -> None:
        pass

    def remove_if_exist(self, customer: Customer) -> None:
        pass

    def count(self) -> int:
        pass

    def important_customers(self) -> Customers:
        pass


# p42: コレクションオブジェクトを安定させる
class Customers:
    def __init__(self, customers: List[Customer]) -> None:
        self.customers = customers

    def get_list(self) -> List[Customer]:  # コレクションの参照をそのまま渡すメソッド
        return self.customers

    def as_list(self) -> Tuple[Customer]:  # コレクションの参照は変更不可にして渡す
        return tuple(self.customers)
