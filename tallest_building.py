tallest_buildings = {
    "Burj Khalifa": (1,"Dubai", "UAE", 828),
    "Merdeka 118": (2, "Kuala Lumpur", "Malaysia", 679),
    "Shanghai Tower": (3,"Shanghai", "China", 632)
}

for key, (rank, city, country, height) in tallest_buildings.items():
    print(f"{key} in {city} is {height} metres high")