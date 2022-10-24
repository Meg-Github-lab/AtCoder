from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())
S = str(B/A)

print(Decimal(S).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))