from django.test import  TestCase
from Polls.models import Question,Track,Choice
from django.utils import timezone
from django.utils import timezone
from django.urls import reverse,resolve


class Testing_Views(TestCase):

    def setUp(self):
        Track.objects.create(track_id=1, name='Geography')
        track1 = Track.objects.last()
        Track.objects.create(track_id=2, name='River')
        track2 = Track.objects.last()
        Question.objects.create(track=track2, question_txt='longest river')
        que1 = Question.objects.last()
        Question.objects.create(track=track1, question_txt='Deepest trench')
        que2 = Question.objects.last()
        Choice.objects.create(question=que1,choice_txt='nile',corr_ans='nile',votes=2)
        Choice.objects.create(question=que2,choice_txt='mariana',corr_ans='mariana',votes=2)

    def test_firstPage(self):
        url = reverse("Polls:First")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_gamepage(self):
        url = reverse("Polls:Front")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_questionlist(self):
        url = reverse("Polls:list",kwargs={'pk':1})
        resp = self.client.get(url)
        print(resp.data)
        self.assertEqual(resp.status_code, 200)

    def test_result(self):
        url = reverse("Polls:result", kwargs={'pk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

