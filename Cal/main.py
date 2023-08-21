
commission = 0.0005


margin = int(input("투입금액(USDT)>> "))
leverage = int(input("배율>> "))

# filled_size 구매 수수료 1번.
# filled_size = (margin * leverage) - ((margin * leverage) * (commission * leverage))
filled_size = (margin * leverage) - ((margin * commission) * (leverage**2))

open_price = int(input("구매가(USDT)>> "))
last_price = int(input("판매가(USDT)>> "))

PnL = (last_price - open_price)  # 손익실현
PnL_ratio = (PnL / open_price) * 100

x = 0  # 팔 가격
property_filledSize_ratio = ( (x - filled_size) / filled_size ) * 100

print(PnL_ratio, "%")
liquidation_price = ""  # 청산가