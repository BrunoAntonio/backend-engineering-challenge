import argparse
import sys

sys.path.append('./packages')

from calculator import MovingAverageCalculator
from data_processor import DataProcessor

class Application:
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--input_file', required=True, help='Path to the input JSON file containing events')
        parser.add_argument('--window_size', type=int, required=True, help='Window size in minutes for moving average calculation')
        args = parser.parse_args()

        # Initialize DataProcessor to handle loading and preprocessing of events
        processor = DataProcessor(args.input_file)
        try:
            loaded_events = processor.load_events()
            pre_processed_events = processor.pre_process_events(loaded_events)
            print(  pre_processed_events)
            # Initialize MovingAverageCalculator with preprocessed events and specified window size
            calculator = MovingAverageCalculator(pre_processed_events , args.window_size)
            moving_averages = calculator.calculate_moving_average()

            # Use DataProcessor to save the calculated moving averages
            processor.save_results(moving_averages)
        except (FileNotFoundError, ValueError) as e:
            print(e)

if __name__ == '__main__':
    app = Application()
    app.run()