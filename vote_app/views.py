from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vote
from .forms import VoteForm
from django.contrib import messages

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
        messages.success(request, 'Thanks for making your voice count')    
        return redirect('result',vote_id)
        
    else:
        return render(request,'vote_app/vote.html',{'vote':vote})

def result(request,vote_id):
    result_of = Vote.objects.get(pk=vote_id)    
    return render(request,'vote_app/result.html',{'result':result_of})


def create(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for adding a Question in poll')
            return redirect('index')
        else:
            return redirect('create')

    else:
         return render(request,'vote_app/create.html',{})
        
    
    
    
    