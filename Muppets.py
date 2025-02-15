file_path= "/Users/alvintung/Downloads/qf-3376/Muppets.csv"


with open(file_path,'r') as file:
    muppet_read=file.read().splitlines()
    
for i in muppet_read:
    muppet_field=i.split(',')
    
    muppet, animal, colour = muppet_field
    
    print(f'{muppet} {animal} {colour}')
    