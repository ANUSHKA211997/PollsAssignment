from django.db import models

class Track(models.Model):
    track_id=models.IntegerField(default=0,null=True)
    name=models.CharField(max_length=20)

class Question(models.Model):
    track=models.ForeignKey(Track,on_delete=models.CASCADE,default=0)
    question_txt=models.CharField(max_length=100)

    def __str__(self):
        return self.question_txt

class Choice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_txt=models.CharField(max_length=100)
    corr_ans=models.CharField(max_length=50, null=True)
    votes=models.IntegerField(default=0)


    def __str__(self):
        return self.choice_txt
#
# class Correct(models.Model):
#     question=models.ForeignKey(Question,on_delete=models.CASCADE)
#     corr_ans=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.corr_ans


