BASKETBALL_SNEAKERS = 0.40
BASKETBALL_SHOES = 0.20
BASKETBALL_BALL = 0.25
BASKETBALL_ACCESSORIES = 0.20

yearly_tax = float(input())

price_sneakers = yearly_tax * BASKETBALL_SNEAKERS
price_shoes = yearly_tax * BASKETBALL_SHOES
price_ball = yearly_tax * BASKETBALL_BALL
price_accessories = yearly_tax * BASKETBALL_ACCESSORIES

total_price = yearly_tax + price_sneakers + price_shoes + price_ball + price_accessories

print(total_price)