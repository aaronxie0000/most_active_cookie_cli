import unittest
from most_active_cookie import readData, closestDate


class TestMostActiveCookie(unittest.TestCase):
    def test_read_data(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-09"],
            ["5UAVanZf6UtGyKVS", "2018-12-09"],
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-08"],
            ["fbcn5UAVanZf6UtG", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-07"],
        ]

        test_dates = readData("cookie_log.csv")
        self.assertCountEqual(test_dates, sample_dates)

    def test_oneClosestDate(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-09"],
            ["5UAVanZf6UtGyKVS", "2018-12-09"],
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-08"],
            ["fbcn5UAVanZf6UtG", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-07"],
        ]

        ans = closestDate(sample_dates, "2018-12-09")
        self.assertEqual(ans, ["AtY0laUfhglK3lC7"])

    def test_multiClosestDate(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-09"],
            ["5UAVanZf6UtGyKVS", "2018-12-09"],
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-08"],
            ["fbcn5UAVanZf6UtG", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-07"],
        ]

        ans = closestDate(sample_dates, "2018-12-08")
        self.assertCountEqual(
            ans, ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        )

    def test_nullClosetDate(self):
        sample_dates = [
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-09"],
            ["5UAVanZf6UtGyKVS", "2018-12-09"],
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-08"],
            ["fbcn5UAVanZf6UtG", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-07"],
        ]

        ans = closestDate(sample_dates, "2018-11-01")
        self.assertCountEqual(
            ans, ["N/A"]
        )


if __name__ == "__main__":
    unittest.main()
