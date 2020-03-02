import paramiko
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip1 = '10.1.14.135'
        username1 = 'junchuan'
        passwd1='simulation'
        ssh.connect(ip1,22,username1,passwd1,timeout=5)
        command1 = "cd calib_demo1/third_party;python3 -c 'import param1_calculation;print(param1_calculation.get_param("+str(selected_choice.votes)+"))'"
        stdin, stdout, stderr = ssh.exec_command(command1)
        out1 = stdout.readlines() 
        selected_choice.param1 = float(out1[0])

        ip2 = '10.1.14.79'
        username2 = username1
        passwd2 = 'sineva2018simu'
        ssh.connect(ip2,22,username2,passwd2,timeout=5)
        command2 = "python3 -c 'import param2_calculation;print(param2_calculation.get_param("+str(selected_choice.param1)+"))'"
        stdin, stdout, stderr = ssh.exec_command(command2)
        out2 = stdout.readlines() 
        selected_choice.param2 = float(out2[0])

        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
