BASKETBALL_SNEAKERS = 0.40
BASKETBALL_CLOTHES = 0.20
BASKETBALL_BALL = 0.25
BASKETBALL_ACCESSORIES = 0.20

yearly_tax = float(input())

price_sneakers = yearly_tax - (yearly_tax * BASKETBALL_SNEAKERS)
price_clothes = price_sneakers - (price_sneakers * BASKETBALL_CLOTHES)
price_ball = price_clothes * BASKETBALL_BALL
price_accessories = price_ball * BASKETBALL_ACCESSORIES

total_price = yearly_tax + price_sneakers + price_clothes + price_ball + price_accessories

print(total_price)