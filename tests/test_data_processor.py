import unittest
from datetime import datetime
from unittest.mock import MagicMock
from data_processor import DataProcessor
from unittest.mock import mock_open, patch

class TestDataProcessor(unittest.TestCase):

    def test_pre_process_events(self):
        loaded_events = [
            {"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 20},
            {"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "airliberty","event_name": "translation_delivered","nr_words": 30, "duration": 31},
            {"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb3","source_language": "en","target_language": "fr","client_name": "taxi-eats","event_name": "translation_delivered","nr_words": 100, "duration": 54}]

        mock_input_file = MagicMock()
        data_processor_instance = DataProcessor(mock_input_file)
        pre_processed_events = data_processor_instance.pre_process_events(loaded_events)
        self.assertEqual(len(pre_processed_events), 4)
        self.assertEqual(pre_processed_events[0]['time'],  datetime(2018, 12, 26, 18, 11))
        self.assertEqual(pre_processed_events[0]['duration'], 20)

if __name__ == '__main__':
    unittest.main()