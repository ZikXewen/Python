jane2 = {
  "people1" : {
       "firstName": "Joe",
       "lastName": "Jackson",
       "gender": "male",
       "age": 28,
       "number": "7349282382"
    },
    'people2':
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    'people3':
    {
       "firstName": "Emily",
       "lastName": "Jones",
       "gender": "female",
       "age": 24,
       "number": "456754675"
    }
}
# test = dict(sorted(jane2.items(), key = lambda item: item[1]["number"]))

test = ["as", "asdfg", "asdf"]
test = sorted(test, key = lambda item: len(item))
print(test)