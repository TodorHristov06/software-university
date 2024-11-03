deposit_amount = float(input())
deposit_deadline = int(input())
yearly_interest_rate = float(input()) / 100

sum = deposit_amount + deposit_deadline * ((deposit_amount * yearly_interest_rate)/12)

print(sum)