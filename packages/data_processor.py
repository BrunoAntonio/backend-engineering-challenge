import json
from datetime import datetime, timedelta

class DataProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.events = []

    # Load events from input JSON file and handle exceptions
    def load_events(self):
        try:
            with open(self.input_file, 'r') as f:
                self.events = json.load(f)
            return self.events
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file {self.input_file} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {self.input_file} is not a valid JSON file.")

    def pre_process_events(self, loaded_events  ):
        pre_processed_events = []
        for event in loaded_events:
            event_time = datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0)
            pre_processed_events.append({'time': event_time, 'duration': event['duration']})

        # Check if the last event's seconds component is greater than 0
        if loaded_events:
            last_event_time = datetime.strptime(loaded_events[-1]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            if last_event_time.second > 0:
                # Calculate the start of the next minute
                next_minute_start = (last_event_time + timedelta(minutes=1)).replace(second=0, microsecond=0)
                # Add a new event at the start of the next minute
                pre_processed_events.append({'time': next_minute_start, 'duration': 0})
        
        return pre_processed_events

    # Save moving averages to output JSON file
    def save_results(self, moving_averages):
        with open('output.json', 'w') as f:
            json.dump(moving_averages, f, indent=4)