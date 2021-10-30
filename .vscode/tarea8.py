investment_in_bitcoin = 1.2
bitcoin_to_euros = 4000
def BitcoinToeuros (investment_in_bitcoin, bitcoin_to_euros):
    euro_value = investment_in_bitcoin * bitcoin_to_euros
    return euro_value

investment_in_euro = BitcoinToeuros (investment_in_bitcoin, bitcoin_to_euros)

if investment_in_euro <= 3000:
    print("Your investment is bellow 30,0000! SELL!") 
else:
    print("Your investment is above 30,0000!")


