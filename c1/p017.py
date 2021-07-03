quantity = 100
unit_price = 50
tax_rate = 1.1
answer = 5500  # 例としてこれらの数字を使いテスト

# p18: 切れ目がはっきりしないコード
price = quantity * unit_price
if price < 3000:
    price += 500
price = price * tax_rate

assert price == answer


# p20: 目的ごとのローカル変数を使う
base_price = quantity * unit_price

shipping_cost = 0
if base_price < 3000:
    shipping_cost = 500

billing_price = (base_price + shipping_cost) * tax_rate  # item_priceだと品物自体の金額を想起させる

assert billing_price == answer


# p21: メソッドとして独立させる
def calculate_shipping_cost(base_price: int) -> int:
    if base_price < 3000:
        return 500
    return 0


base_price = quantity * unit_price

shipping_cost = calculate_shipping_cost(base_price)

billing_price = (base_price + shipping_cost) * tax_rate  # item_priceだと品物自体の金額を想起させる

assert billing_price == answer


# p23: 異なるクラスの重複したコードをなくす
class ShippingCost:
    minimum_for_free = 3000
    cost = 500

    def __init__(self, base_price: int) -> None:
        self.base_price = base_price

    def amount(self) -> int:
        if self.base_price < ShippingCost.minimum_for_free:
            return ShippingCost.cost
        return 0


class Order:
    def __init__(self, quantity: int, unit_price: int) -> None:
        self.quantity = quantity
        self.unit_price = unit_price

    @property  # read only
    def base_price(self) -> int:
        return self.quantity * self.unit_price

    def calculate_shipping_cost(self) -> int:
        cost = ShippingCost(self.base_price)
        return cost.amount()


class OrderChange:
    def __init__(self, quantity: int, unit_price: int) -> None:
        self.quantity = quantity
        self.unit_price = unit_price

    @property  # read only
    def base_price(self) -> int:
        return self.quantity * self.unit_price

    def calculate_shipping_cost(self) -> int:
        cost = ShippingCost(self.base_price)
        return cost.amount()


order = Order(quantity=quantity, unit_price=unit_price)
assert order.calculate_shipping_cost() == 0  # base_price=5000なので送料0

order_change = OrderChange(quantity=quantity, unit_price=unit_price)
assert order_change.calculate_shipping_cost() == 0
