from django.shortcuts import render
from api.services import scrape_website, chat_with_ai
import json

def home(request):
    context = {
        'scrape_result': None,
        'chat_response': None,
        'previous_chat': None,
    }
    
    if request.method == 'POST':
        if 'scrape_submit' in request.POST:
            url = request.POST.get('url')
            result = scrape_website(url)
            context['scrape_result'] = json.dumps(result, indent=2)

        elif 'chat_submit' in request.POST:
            message = request.POST.get('message')
            context['previous_chat'] = message
            user_id = 1
            response = chat_with_ai(message, user_id)
            context['chat_response'] = response

    return render(request, "pages/index.html", context)
