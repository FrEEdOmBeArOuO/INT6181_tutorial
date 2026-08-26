import unittest
from parking_fee import ParkingFeeCalculator


class TestParkingFeeCalculator(unittest.TestCase):

    def setUp(self):
        """Setup dataset fixtures for testing."""
        self.calculator = ParkingFeeCalculator()

        # Valid parking hours and expected fees: (hours, expected_fee)
        self.valid_fees = [
            (1, 0.0),       # First hour free
            (1.5, 10.0),    # Partial hour rounded up
            (2, 10.0),      # One billable hour
            (3, 20.0),      # Two billable hours
            (9, 80.0),      # Hits daily cap
            (10, 80.0),     # Capped at daily maximum
            (24, 80.0),     # Full day capped
        ]

        # Multi-day parking: (hours, expected_fee)
        self.multi_day_fees = [
            (25, 80.0),     # 1 day + 1 free hour
            (26, 90.0),     # 1 day + 2 hours (1 billable)
            (48, 160.0),    # 2 full days
            (49, 160.0),    # 2 days + 1 free hour
            (50, 170.0),    # 2 days + 2 hours (1 billable)
        ]

        # Invalid inputs (expected return None)
        self.invalid_inputs = [
            0,
            -1,
            -0.5,
            "2",
            None,
            True,
            [2],
        ]

    def test_valid_fee_calculation(self):
        """Test fee calculation for valid parking hours."""
        for hours, expected_fee in self.valid_fees:
            fee = self.calculator.calculate_fee(hours)
            self.assertIsNotNone(
                fee,
                msg=f"calculate_fee({hours}) should return a fee."
            )
            self.assertAlmostEqual(
                fee, expected_fee, places=2,
                msg=f"Fee for {hours} hour(s) should be {expected_fee}."
            )

    def test_first_hour_free(self):
        """Test that the first hour of parking is free."""
        self.assertAlmostEqual(self.calculator.calculate_fee(1), 0.0, places=2)
        self.assertAlmostEqual(self.calculator.calculate_fee(0.5), 0.0, places=2)

    def test_daily_cap(self):
        """Test that fee does not exceed the daily maximum."""
        for hours in [9, 10, 15, 24]:
            fee = self.calculator.calculate_fee(hours)
            self.assertLessEqual(
                fee, self.calculator.DAILY_MAX,
                msg=f"Fee for {hours} hour(s) should not exceed daily cap."
            )

    def test_invalid_inputs_return_none(self):
        """Test invalid inputs return None."""
        for hours in self.invalid_inputs:
            fee = self.calculator.calculate_fee(hours)
            self.assertIsNone(
                fee,
                msg=f"calculate_fee({hours}) should return None."
            )

    def test_multi_day_parking(self):
        """Test fee calculation for parking longer than 24 hours."""
        for hours, expected_fee in self.multi_day_fees:
            fee = self.calculator.calculate_fee(hours)
            self.assertIsNotNone(
                fee,
                msg=f"calculate_fee({hours}) should return a fee."
            )
            self.assertAlmostEqual(
                fee, expected_fee, places=2,
                msg=f"Fee for {hours} hour(s) should be {expected_fee}."
            )


if __name__ == '__main__':
    unittest.main()
