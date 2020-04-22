from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vote
# from .forms import VoteForm

def index(request):
    vote_qsn = Vote.objects.all()
    return render(request,'vote_app/index.html',{'vote':vote_qsn})

def vote(request,vote_id):
    vote = Vote.objects.get(pk=vote_id)
    if request.method == "POST":
        selected_vote = request.POST['vote']
        if selected_vote == "option_one_count":
            vote.option_one_count +=1
        elif selected_vote == "option_two_count":
            vote.option_two_count +=1
        elif selected_vote == "option_three_count":
            vote.option_three_count +=1
        else:
            return HttpResponse(400,'error in form')
        vote.save()    
        return redirect('result',vote_id)
        
    else:
        return render(request,'vote_app/vote.html',{'vote':vote})

def result(request,vote_id):
    result_of = Vote.objects.get(pk=vote_id)
    return render(request,'vote_app/result.html',{'result':result_of})
    
    
    
    