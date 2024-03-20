state_abb = {
  "NSW": "New South Wales",
  "ACT": "Australian Capital Territory",
  "NT": "Northern Territory",
  "QLD": "Queensland",
  "SA": "South Australia",
  "TAS": "Tasmania",
  "VIC": "Victoria",
  "WA": "Western Australia"
}

str_input = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
print(f"The state you entered is {state_abb.get(str_input)}")