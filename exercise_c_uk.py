united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

united_kingdom[1]["capital"] = "Cardiff"

print(united_kingdom)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).

norn_iron = {
  "name": "Northern Ireland",
  "population": 1811000,
  "capital": "Belfast"
}

united_kingdom.append(norn_iron)

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.

index = 0

for country in united_kingdom:
  print(united_kingdom[index]["name"])
  index += 1

# 4. Use a loop to find the total population of the UK.

pop_index = 0
total_pop = 0

for country in united_kingdom:
  total_pop = total_pop + united_kingdom[pop_index]["population"]
  pop_index += 1


print(total_pop)