from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice, Track
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import questionSerializer,trackSerializer

class questionList(APIView):
    def get(self, request, pk, *args, **kwargs):
        track=Track.objects.get(pk=pk).question_set.all()
        tra=list(track.values())
        serial=questionSerializer(track,many=True)
        return Response(serial.data)


class crudTrack(APIView):
            def get(self,request,pk,name):
                track=Track.objects.all()
                serial=trackSerializer(track,many=True)
                return Response(serial.data)

            def post(self,request,pk,name):
                serial=trackSerializer(data=request.data)
                if(serial.is_valid()):
                    serial.save()
                    return Response(serial.data)


            def put(self,request,pk,name):
                serial=trackSerializer(Track,data=request.data)
                if (serial.is_valid()):
                    serial.save()
                    return Response(serial.data)

            def delete(self,request,pk,name):
                serial = Track.objects.get(pk=pk)
                serial.delete()
                return Response(status= 1)






def FirstPage(request):
    print("hello")
    return render(request,'Polls/FirstPage.html',{})


def GamePage(request):
    quest=Question.objects.all()
    track= Track.objects.all()
    track_list={
        "track_list":track
    }
    return render(request,'Polls/GamePage.html',track_list)

def QuestionView(request, pk):
    quest=Track.objects.get(pk=pk)
    que_list={
        "que_list":quest
    }
    return render(request,'Polls/QuestionPage.html',que_list)

def ResultView(request, pk):
    corr=0
    wrong=0
    resl = Question.objects.get(pk=pk)


    res=Question.objects.get(pk=pk).choice_set.all()
    ct=(res.values('choice_txt'))
    li=list(ct.values())
    vt=res.values('votes')
    li_v=list(vt.values())
    print("length",li_v[0]["votes"])

    correct_answer=res.values("corr_ans")
    corr_an=list(correct_answer.values())
    check=corr_an[0]["corr_ans"]
    print("correct answer: ",correct_answer)
    for r in range(len(li)):
        votes = li_v[r]["votes"]
        if(li[r]["choice_txt"]==check):
            print("r",r)

            corr=corr+votes
            print("correct:",corr)
        else:
            print(r)
            wrong=wrong+votes
            print("wrong : ",wrong)


    print(wrong)
    print("correct",corr)
    result_list = {
        "resul_list": resl,
        "wrong":wrong,
        "correct":corr,
    }

    return render(request, 'Polls/ResultPage.html', result_list)



