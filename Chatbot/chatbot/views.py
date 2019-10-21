from django.shortcuts import render
from django.http import JsonResponse
from chatbot.models import FAQ

stopwords = ['a','an','the','who','what','why','?','is','in','for','because']
# Create your views here.
def chatbot(request):
  return render(request, 'chatbot.html')

def answer(request):
    response = ""
    filtered_query = []
    all_questions = FAQ.objects.all()
    query = request.GET.get('query', None)
    query = query.lower()
    query = query.split()
    for word in query:
      if word not in stopwords:
        filtered_query.append(word)

    answer_set = []
    for question in all_questions:
      print(question.__str__())
      for keyword in filtered_query:
        print(keyword)
        if keyword in question.__str__().lower() and question.answer not in answer_set:
          answer_set.append(question.answer)

    for answer in answer_set:
      response += answer

    if not response:
      response = "Sorry, I could not find anything relevent"


    data = {
        'response': response
    }
    return JsonResponse(data)