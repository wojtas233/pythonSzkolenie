import random
ILOSC_LOSOWAN = 6
MINIMALNA = 1
MAKSYMALNA = 49

wylosowane = random.sample(range(MINIMALNA, MAKSYMALNA), ILOSC_LOSOWAN)
print(sorted(wylosowane))

