from django.test import  TestCase
from Polls.models import Question,Track,Choice
from django.utils import timezone
from django.utils import timezone
from django.urls import reverse,resolve
from tastypie.test import ResourceTestCase



class Testing_API(TestCase):

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

    def test_questionlist(self):
        url = reverse("Polls:list",kwargs={'pk':1})
        resp = self.client.get(url)
        print(resp.data)
        self.assertEqual(resp.status_code, 200)


    def test_crud(self):
        url = reverse("Polls:track",kwargs={'pk':1,'name':'get'})
        response = self.client.post(url, { "id": 3,
        "track_id": 1,
        "name": "River"})
        self.assertEquals(response.status_code,200)
        print("Response for post:",response)
        exp_data = {
            "id": 3,
            "track_id": 1,
            "name": "River"
        }
        self.assertEqual(response.json(), exp_data)







