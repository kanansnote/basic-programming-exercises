# Coupon Generator

base = "www.homeflix.com"
coupon = 'signup/coupon'
discount = 50
amount = 4

for num in range(amount):
    print(f'{base}/{coupon}/{discount}/{num}')

print(f"{amount} coupons created")

# Nov 14, 2022