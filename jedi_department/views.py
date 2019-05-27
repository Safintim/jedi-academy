from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CandidateForm, TestForm, JediForm
from .models import ListQuestions, Answer, Jedi, Candidate, Test, Padawan


def index(request):
    return render(request, 'jedi_department/index.html')


def candidate_form(request):
    if request.method == 'POST':
        form_candidate = CandidateForm(request.POST)
        if form_candidate.is_valid():
            request.session['email_candidate'] = form_candidate.cleaned_data['email']
            form_candidate.save()
            return HttpResponseRedirect('test_form')
    else:
        form_candidate = CandidateForm()

    return render(request, 'jedi_department/candidate_form.html', context={
        'candidate_form': form_candidate
    })


def jedi_form(request):
    if request.method == 'POST':
        form_jedi = JediForm(request.POST)
        if form_jedi.is_valid():
            request.session['name_jedi'] = form_jedi.cleaned_data['name'].name
            return HttpResponseRedirect('candidates')
    else:
        form_jedi = JediForm()

    return render(request, 'jedi_department/jedi_form.html', context={
        'jedi_form': form_jedi,
    })


def test_form(request):

    test = Test.objects.get(id=1)
    questions = ListQuestions.objects.filter(test=test)

    email_candidate = request.session['email_candidate']

    if request.method == 'POST':
        form_test = TestForm(request.POST)
        if form_test.is_valid():
            candidate = Candidate.objects.get(email=email_candidate)
            answers = request.POST.getlist('text_answer')
            candidate.pass_test = True
            candidate.save(update_fields=['pass_test'])
            for i in range(0, len(questions)):
                new_answer = Answer.objects.create(
                    test=test,
                    candidate=candidate,
                    question=questions[i],
                    text_answer=answers[i]
                )
            return HttpResponse('<h1>Answer accepted</h1>')
    else:
        form_test = TestForm()
    
    return render(request, 'jedi_department/test_form.html', context={
        'test_form': form_test,
        'questions': questions,
        'test': test
    })


def candidates(request):
    name_jedi = request.session['name_jedi']
    jedi = Jedi.objects.get(name=name_jedi)
    padawans = Padawan.objects.filter(jedi_id=jedi.pk)
    if request.method == 'POST':
        email_candidate = request.POST.get('candidate')
        candidate = Candidate.objects.get(email=email_candidate)
        if len(padawans) < 3:
            Padawan.objects.create(
                jedi_id=jedi,
                candidate_id=candidate
            )
            return HttpResponse('<h1>Candidate enrolled</h1>')
        return HttpResponse('<h1>You already have 3 candidates</h1>')
    else:
        candidates_id = [i.candidate_id.id for i in padawans]
        planet_jedi = jedi.planet
        candidates_planet_jedi = Candidate.objects.filter(planet=planet_jedi,
                                                          pass_test=True).exclude(id__in=candidates_id)

        candidates_answers = {}
        for candidate in candidates_planet_jedi:
            candidates_answers[candidate] = Answer.objects.filter(candidate=candidate)

    return render(request, 'jedi_department/candidates.html', context={
        'planet': planet_jedi,
        'candidates_answers': candidates_answers,
    })


def jedi_info(request):
    if request.method == 'GET':
        jedis = Jedi.objects.all()
        padawans = Padawan.objects.all()
        jedis_and_padawans = {}
        for jedi in jedis:
            jedis_and_padawans[jedi.name] = padawans.filter(jedi_id=jedi.id).count()

        return render(request, 'jedi_department/jedi_info.html', context={
            'jedis_and_padawans': jedis_and_padawans
        })
