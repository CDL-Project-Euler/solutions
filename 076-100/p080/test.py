import decimal
decimal.getcontext().prec = 3
print(str(decimal.Decimal(2) ** decimal.Decimal(0.5)))