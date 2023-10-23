import unittest,  os
from food_truck.food_truck import parse_arguments, search_by_food_items
test_file = 'test.csv'
rows = [
    'locationid,Applicant,FacilityType,cnn,LocationDescription,Address,blocklot,block,lot,permit,Status,FoodItems,X,Y,Latitude,Longitude,Schedule,dayshours,NOISent,Approved,Received,PriorPermit,ExpirationDate,Location,Fire Prevention Districts,Police Districts,Supervisor Districts,Zip Codes,Neighborhoods (old)\n',
    '1728067,Leo\'s Hot Dogs,Push Cart,9121000,MISSION ST: 19TH ST to 20TH ST (2300 - 2399),2301 MISSION ST,3595031,3595,031,23MFF-00008,APPROVED,Hot dogs and related toppings: non alcoholic beverages,6007018.02,2104913.057,37.76008693198698,-122.41880648110114,http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00008&ExportPDF=1&Filename=23MFF-00008_schedule.pdf,,,09/20/2023 12:00:00 AM,20230920,1,11/15/2024 12:00:00 AM,"(37.76008693198698, -122.41880648110114)",2,4,7,28859,19\n'
]

class TestFoodTruck(unittest.TestCase):
    def setUp(self):
        """
        Write the testing csv file  used in the test cases
        """
        with open(test_file, 'w', newline='') as csv_file:
            for row in rows:
                csv_file.write(row)
    def tearDown(self):
        """
        Remove the testing csv file at the end of the tests.
        """
        os.remove(test_file)

    def test_parse_arguments(self):
        """Check CLI arguments"""
        parser = parse_arguments()
        res = parser.parse_args(["--food", "drinks", "--csv", "check_csv.csv"])
        self.assertEqual(res.food, ["drinks"])
        self.assertEqual(res.csv, "check_csv.csv")

    def test_bad_parse_arguments(self):
        """Check that fails when we pass bad arguments"""
        parser = parse_arguments()
        self.assertRaises(SystemExit, parser.parse_args, ["--bad=arg", "ABC"] )
        self.assertRaises(SystemExit, parser.parse_args, ["--help"])
        self.assertRaises(SystemExit, parser.parse_args)

    def test_search_by_food_items_positive(self):
        """Return the match case thats the example."""
        res = search_by_food_items(test_file, ["beverages"])
        self.assertEqual(res, [{"address": "2301 MISSION ST", "applicant": "Leo's Hot Dogs"}])

    def test_search_by_food_items_negative(self):
        """Expect to return an empty list"""
        res = search_by_food_items(test_file, ["supercalifragilisticexpialidocious"])
        print(res)
        self.assertEqual(res, [])


if __name__ == '__main__':
    unittest.main()