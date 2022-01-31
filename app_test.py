import unittest
from most_active_cookie import readData, closestDate
from datetime import datetime


class TestMostActiveCookie(unittest.TestCase):
    def test_read_data(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["5UAVanZf6UtGyKVS", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["fbcn5UAVanZf6UtG", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-07', "%Y-%m-%d")],
        ]

        test_dates = readData("cookie_log.csv")
        self.assertCountEqual(test_dates, sample_dates)

    def test_oneClosestDate(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["5UAVanZf6UtGyKVS", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["fbcn5UAVanZf6UtG", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-07', "%Y-%m-%d")],
        ]

        ans = closestDate(sample_dates, "2018-12-09")
        self.assertEqual(ans, ["AtY0laUfhglK3lC7"])

    def test_multiClosestDate(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["5UAVanZf6UtGyKVS", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["AtY0laUfhglK3lC7", datetime.strptime('2018-12-09', "%Y-%m-%d")],
            ["SAZuXPGUrfbcn5UA", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["fbcn5UAVanZf6UtG", datetime.strptime('2018-12-08', "%Y-%m-%d")],
            ["4sMM2LxV07bPJzwf", datetime.strptime('2018-12-07', "%Y-%m-%d")],
        ]

        ans = closestDate(sample_dates, "2018-12-08")
        self.assertCountEqual(
            ans, ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        )


if __name__ == "__main__":
    unittest.main()
