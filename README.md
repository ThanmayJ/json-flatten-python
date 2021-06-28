# json-flatten-python
A utility to FLATTEN and UNFLATTEN .json files in python

All sample files have been taken from [here](https://filesamples.com/formats/json)

## JSON (JavaScript Object Notation)

A .json file might look like this
```
data = {'people': [{'age': 28,
         'firstName': 'Joe',
         'gender': 'male',
         'lastName': 'Jackson',
         'number': '7349282382'},
        {'age': 32,
         'firstName': 'James',
         'gender': 'male',
         'lastName': 'Smith',
         'number': '5678568567'},
        {'age': 24,
         'firstName': 'Emily',
         'gender': 'female',
         'lastName': 'Jones',
         'number': '456754675'}]}

```
## FLATTEN

Flattening it will give:
```
flattened = {'people.[0].age': 28,
             'people.[0].firstName': 'Joe',
             'people.[0].gender': 'male',
             'people.[0].lastName': 'Jackson',
             'people.[0].number': '7349282382',
             'people.[1].age': 32,
             'people.[1].firstName': 'James',
             'people.[1].gender': 'male',
             'people.[1].lastName': 'Smith',
             'people.[1].number': '5678568567',
             'people.[2].age': 24,
             'people.[2].firstName': 'Emily',
             'people.[2].gender': 'female',
             'people.[2].lastName': 'Jones',
             'people.[2].number': '456754675'}
 ```
## UNFLATTEN

 Unflattening a flattened .json file will bring back the original structure.
 ```
unflattened = {'people': [{'age': 28,
               'firstName': 'Joe',
               'gender': 'male',
               'lastName': 'Jackson',
               'number': '7349282382'},
              {'age': 32,
               'firstName': 'James',
               'gender': 'male',
               'lastName': 'Smith',
               'number': '5678568567'},
              {'age': 24,
               'firstName': 'Emily',
               'gender': 'female',
               'lastName': 'Jones',
               'number': '456754675'}]}
```
