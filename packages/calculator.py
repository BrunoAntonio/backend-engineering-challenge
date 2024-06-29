from datetime import timedelta
from collections import deque

class MovingAverageCalculator:
    # Initialize MovingAverageCalculator with preprocessed events and defined window size and validate window size
    def __init__(self, events, window_size):
        if window_size <= 0:
            raise ValueError("window_size must be greater than 0")
        self.events = events
        self.window_size = window_size

    # Calculate moving average delivery time for each event based on the window size
    def calculate_moving_average(self):
        results = []
        window = deque()
        current_time = self.events[0]['time']
        end_time = self.events[-1]['time']

        while current_time <= end_time:
            while window and window[0]['time'] < current_time - timedelta(minutes=self.window_size):
                window.popleft()

            average_delivery_time = sum(event['duration'] for event in window) / len(window) if window else 0
            results.append({'date': current_time.strftime('%Y-%m-%d %H:%M:%S'), 'average_delivery_time': average_delivery_time})

            for event in [e for e in self.events if e['time'] == current_time]:
                window.append(event)

            current_time += timedelta(minutes=1)

        return results