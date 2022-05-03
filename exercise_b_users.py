users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# # 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# # 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# # 3. Get the list of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# # 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])

# # 5. Get the smallest of Erik's lottery numbers

numbers = users["Erik"]["lottery_numbers"]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(sorted_numbers[0])

# 6. Return an list of Avril's lottery numbers that are even

avril_numbers = users["Avril"]["lottery_numbers"]

evens = []

# FOR every number in avril_numbers:

for number in avril_numbers:
  if number % 2 == 0:
    evens.append(number)

  # IF modulo of number is 0
    # THEN append number to evens
  
# PRINT evens

print(evens)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users["Erik"]["lottery_numbers"].append(7)

print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = 'Edinburgh'

print(users["Erik"])

# 9. Add a pet dog to Erik called "fluffy"

# CREATE the fluffy dictionary and assign it to fluffy

fluffy = {
  "name": "fluffy",
  "species": "dog"
}

# APPEND fluffy to Erik's pets

users["Erik"]["pets"].append(fluffy)

print(users["Erik"])

# 10. Add another person to the users dictionary

jenny = {
  "twitter": "jennymac",
  "lottery_numbers": [7, 15, 19, 22, 30, 45],
  "home_town": "Cumbernauld",
  "pets": [
    {
      "name": "bobo",
      "species": "dog"
    },
    {
      "name": "liam",
      "species": "goldfish"
    },
    {
      "name": "noel",
      "species": "goldfish"
    }
  ]
  }

users["Jenny"] = jenny

print(users)