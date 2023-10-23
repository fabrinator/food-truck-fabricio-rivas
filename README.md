# Engineering Assessment

This python scripts returns the different locations (Addresses and Applicant) that provides the food items that 
we have provided in the CLI as a filter.

For example: 

```shell script
$ python3 food_truck/food_truck.py --food pasta   
Address: 425 DIVISADERO ST, Applicant: The Chef Station
```

In the case that there is no food item registered in the csv, it will return:
```shell script
python3 food_truck/food_truck.py --food ABCDEF
There is not a location where they provide ['ABCDEF']
```


Also, this script has some unittest that we can execute:
```shell script
$ python3 -m unittest  -b -v
test_bad_parse_arguments (test.test_food_truck.TestFoodTruck)
Check that fails when we pass bad arguments ... ok
test_parse_arguments (test.test_food_truck.TestFoodTruck)
Check setup ... ok
test_search_by_food_items_negative (test.test_food_truck.TestFoodTruck)
Expect to return an empty list ... ok
test_search_by_food_items_positive (test.test_food_truck.TestFoodTruck)
Return the match case thats the example. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.008s

OK
```

We can also execute the coverage of the tests:

```shell script
coverage run -m unittest -b -v
test_bad_parse_arguments (test.test_food_truck.TestFoodTruck)
Check that fails when we pass bad arguments ... ok
test_parse_arguments (test.test_food_truck.TestFoodTruck)
Check setup ... ok
test_search_by_food_items_negative (test.test_food_truck.TestFoodTruck)
Expect to return an empty list ... ok
test_search_by_food_items_positive (test.test_food_truck.TestFoodTruck)
Return the match case thats the example. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK

coverage report               
Name                       Stmts   Miss  Cover
----------------------------------------------
food_truck/__init__.py         0      0   100%
food_truck/food_truck.py      15      0   100%
test/__init__.py               0      0   100%
test/test_food_truck.py       28      0   100%
----------------------------------------------
TOTAL                         43      0   100%
```

## CI on Github Actions
For passing the CI of the process, there is a workflow defined to run each time the code is pushed in github.

The definition of the workflows exists in the [repository](.github/workflows/run_test.yml)

