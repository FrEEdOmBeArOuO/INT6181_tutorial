import math


class ParkingFeeCalculator:
    HOURLY_RATE = 10.0
    DAILY_MAX = 80.0

    def calculate_fee(self, hours):
        """
        Calculates parking fee based on hours parked.
        - Hours must be a positive number (int or float, not bool).
        - The first hour is free.
        - Additional hours (including partial hours) are rounded up and charged at HOURLY_RATE.
        - Fee is capped at DAILY_MAX per 24-hour period.
        - Returns fee rounded to 2 decimal places, or None if invalid.
        """
        if not isinstance(hours, (int, float)) or isinstance(hours, bool):
            print("Hours must be a number.")
            return None

        if hours <= 0:
            print("Hours must be greater than zero.")
            return None

        full_days = int(hours // 24)
        remainder = hours - full_days * 24
        total = full_days * self.DAILY_MAX + self._fee_for_period(remainder)
        return round(total, 2)

    def _fee_for_period(self, hours):
        """Calculates fee for a single period up to 24 hours."""
        if hours <= 1:
            return 0.0

        billable_hours = math.ceil(hours - 1)
        return min(billable_hours * self.HOURLY_RATE, self.DAILY_MAX)


if __name__ == '__main__':
    calculator = ParkingFeeCalculator()

    try:
        hours = float(input("Enter parking hours: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    else:
        fee = calculator.calculate_fee(hours)
        if fee is not None:
            print(f"Parking fee for {hours} hour(s): ${fee:.2f}")
        else:
            print("Invalid parking hours.")
