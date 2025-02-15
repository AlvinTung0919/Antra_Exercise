file_path="/Users/alvintung/Downloads/qf-3383"

print(file_path)

# read first file into a list
with open("/Users/alvintung/Downloads/qf-3383/Grand Prix 2022.csv", 'r') as gp_2022:

    # read all lines into list, split this and return the second column entry (a list comprehension!)
    grand_prix_2022 = [line.split(",")[1] for line in gp_2022.read().splitlines()]

# read second file into a list
with open("/Users/alvintung/Downloads/qf-3383/Grand Prix 2023.csv", 'r') as gp_2023:

    # read all lines into list, split this and return the second column entry (a second list comprehension!)
    grand_prix_2023 = [line.split(",")[1] for line in gp_2023.read().splitlines()]

# get sets for each of the two lists
grand_prix_2022_set = set(grand_prix_2022)
grand_prix_2023_set = set(grand_prix_2023)

# get the ones in one, but not both
exceptions = grand_prix_2022_set ^ grand_prix_2023_set

# now convert this to a list
exceptions_list = list(exceptions)

print("\n")

# list these out
for ex in exceptions_list:

    # need to find out which element each member came from
    if ex in grand_prix_2022_set:
        print("{0} is in 2022 only".format(ex))
    else:
        print("{0} is in 2023 only".format(ex))

