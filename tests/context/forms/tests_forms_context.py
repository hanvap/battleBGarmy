from django.test import TestCase

from histproject.context.forms import HistoricalEventForm


class TestHistoricalEventForm(TestCase):
    def setUp(self):
        self.valid_form = {
            'title': 'Test Title',
            'description': 'Test Description',
            'date': '2022-10-11',
            'image': 'https://',
            'video_id': 'UKuO5cgHd2k'
        }

        self.invalid_form = {
            'title': '',
            'description': 'Test Description',
            'date': '2022-10-11',
            'image': 'https://',
            'video_id': 'UKuO5cgHd2k'
        }
    def test_form_valid(self):
        form = HistoricalEventForm(data=self.valid_form)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = HistoricalEventForm(data=self.invalid_form)
        self.assertFalse(form.is_valid())

