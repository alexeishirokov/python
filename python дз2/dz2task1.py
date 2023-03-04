from random import randint

coin = randint(3, 8)
eagle = 0
tails = 0
count = 0 
print(f"Число монет: {coin}")

for i in range(coin):
	coin_random = randint(0,1)
	print(coin_random)
	if coin_random == 0:
		tails += 1
	elif coin_random == 1:
		eagle += 1

if tails >= eagle:
	print(f"Чтобы везде был орёл, нужно повернуть: {eagle}")
else:
	print(f"Чтобы везде была решка, нужно повернуть: {tails}")