from __future__ import annotations

from abc import ABCMeta, abstractmethod

customer_type = "child"
base_fee = 100

# p49: 判断や処理のロジックをメソッドに独立させる

if customer_type == "child":
    fee = base_fee * 0.5


def is_child() -> bool:
    return customer_type == "child"


def child_fee() -> int:
    return base_fee * 0.5


if is_child():
    fee = child_fee()


# p53: 区分ごとのロジックを別のクラスに分けて記述する
class Yen:
    pass


class AdultFee:
    def yen(self) -> Yen:
        return Yen(100)

    def label(self) -> str:
        return "大人"


# p54: 区分ごとのクラスを同じ「型」として扱う
class Fee(metaclass=ABCMeta):
    @abstractmethod  # 子クラスでオーバーライドしないとインスタンス化できない
    def yen(self) -> Yen:
        pass

    @abstractmethod
    def label(self) -> str:
        pass


class AdultFee(Fee):
    def yen(self) -> Yen:
        return Yen(100)

    def label(self) -> str:
        return "大人"


class Charge:
    def __init__(self, fee: Fee):
        self.fee = fee

    def yen(self) -> Yen:
        return self.fee.yen()


class Reservation:
    def __init__(self):
        self.fees = []

    def add_fee(self, fee: Fee) -> None:
        self.fees.append(fee)

    def fee_total(self) -> Yen:
        total = Yen(0)
        for fee in self.fees:
            total.add(fee.yen())
        return total


# p58: 区分ごとのクラスのインスタンスを生成する
class FeeFactory:
    types = {}
    types["adult"] = AdultFee()
    types["child"] = ChildFee()

    def fee_by_name(self, name: str) -> Fee:
        return FeeFactory.types.get(name)


# p59: Javaの列挙型を使えばもっとかんたん
