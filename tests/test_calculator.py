import unittest
from datetime import datetime



from calculator import MovingAverageCalculator

class TestMovingAverageCalculator(unittest.TestCase):
    def test_multiple_events(self):
        processed_events = [
            {'time': datetime(2018, 12, 26, 18, 11), 'duration': 20}, 
            {'time': datetime(2018, 12, 26, 18, 15), 'duration': 31}, 
            {'time': datetime(2018, 12, 26, 18, 23), 'duration': 54}, 
            {'time': datetime(2018, 12, 26, 18, 24), 'duration': 0}]
        
        calculator = MovingAverageCalculator(processed_events, 10)
        expected = [
            {"date": "2018-12-26 18:11:00","average_delivery_time": 0},
            {"date": "2018-12-26 18:12:00","average_delivery_time": 20},
            {"date": "2018-12-26 18:13:00","average_delivery_time": 20},
            {"date": "2018-12-26 18:14:00","average_delivery_time": 20},
            {"date": "2018-12-26 18:15:00","average_delivery_time": 20},
            {"date": "2018-12-26 18:16:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:17:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:18:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:19:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:20:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:21:00","average_delivery_time": 25.5},
            {"date": "2018-12-26 18:22:00","average_delivery_time": 31},
            {"date": "2018-12-26 18:23:00","average_delivery_time": 31},
            {"date": "2018-12-26 18:24:00","average_delivery_time": 42.5}]
        
        self.assertEqual(calculator.calculate_moving_average(), expected)

if __name__ == '__main__':
    unittest.main()