import json

with open('constants.json') as constants:
    const = json.load(constants)

print(2*const['ARROW_HEIGHT'])