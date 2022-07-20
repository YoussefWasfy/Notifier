from unittest import mock
from unittest import TestCase
import main


# Input dates and times needs to be changed depending on the time of testing
class AlarmTest(TestCase):

    @mock.patch('main.input', create=True)
    def test_one_data_entry(self, mocked_input):
        mocked_input.side_effect = ['1', '20.07.2022', '13:49']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 13:49')

    @mock.patch('main.input', create=True)
    def test_three_data_entries(self, mocked_input):
        mocked_input.side_effect = ['3', '20.07.2022', '13:52', '20.07.2022', '13:54', '20.07.2022', '13:53']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 13:52\nThe '
                                                             '2nd date has been reached! 20.07.2022 13:53\nThe '
                                                             '3rd date has been reached! 20.07.2022 13:54')

    # Testing entering the wrong type in the first input
    @mock.patch('main.input', create=True)
    def test_wrong_type_of_input(self, mocked_input):
        mocked_input.side_effect = ['ee', '3', '20.07.2022', '12:49', '20.07.2022', '12:47', '20.07.2022', '12:48']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 12:47\nThe '
                                                             '2nd date has been reached! 20.07.2022 12:48\nThe '
                                                             '3rd date has been reached! 20.07.2022 12:49')

    # Entering date instead of time and vice versa
    @mock.patch('main.input', create=True)
    def test_wrong_type_of_input(self, mocked_input):
        mocked_input.side_effect = ['3', '12:56', '20.07.2022', '20.07.2022', '12:56', '20.07.2022', '12:54',
                                    '20.07.2022', '12:55']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 12:54\nThe '
                                                             '2nd date has been reached! 20.07.2022 12:55\nThe '
                                                             '3rd date has been reached! 20.07.2022 12:56')

    # dates or times that have already passed
    @mock.patch('main.input', create=True)
    def test_already_passed_date_or_time(self, mocked_input):
        mocked_input.side_effect = ['3', '19.07.2022', '13:02', '20.07.2022', '13:03',
                                    '20.07.2022', '13:51']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 13:51')

    # All input dates are the same
    @mock.patch('main.input', create=True)
    def test_all_entries_are_same(self, mocked_input):
        mocked_input.side_effect = ['3', '20.07.2022', '14:34', '20.07.2022', '14:34',
                                    '20.07.2022', '14:34']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 14:34')

    # entering empty dates and time
    @mock.patch('main.input', create=True)
    def test_empty_data_entry(self, mocked_input):
        mocked_input.side_effect = ['1', '', '', '', '', '20.07.2022', '14:46']
        self.assertEqual(main.calculate_and_display_dates(), 'The 1st date has been reached! 20.07.2022 14:46')
