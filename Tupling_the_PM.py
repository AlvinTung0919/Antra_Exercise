prime_ministers = (
  "Tony Blair","Gordon Brown",
  "David Cameron","Theresa May",
  "Boris Johnson","Liz Truss",
  "Rushi Sunak","Alvin"
)

list_prime_ministers=list(prime_ministers)
list_prime_ministers.sort()
for item_number, name_item in enumerate(list_prime_ministers,start=1):
    
    print(f'{item_number} is {name_item}')