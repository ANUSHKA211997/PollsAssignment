from django.test import  TestCase
from Polls.models import Question,Track
from django.utils import timezone
from django.utils import timezone
from django.urls import reverse,resolve


class Testing_Models(TestCase):

    def setUp(self):
        self.create_model()
    def create_model(self):
        Track.objects.create(track_id=1,name='Geography')
        track1=Track.objects.last()
        Track.objects.create(track_id=2,name='River')
        track2=Track.objects.last()

        Question.objects.create(track=track1,question_txt='Deepest trench')
        return(Question.objects.create(track=track2,question_txt='longest river'))

    def test_model(self):
        w = self.create_model()
        self.assertTrue(isinstance(w, Question))
        self.assertEqual(w.__str__(), w.question_txt)

