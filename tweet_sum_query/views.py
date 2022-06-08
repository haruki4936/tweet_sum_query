from django.shortcuts import render

# Create your views here.
def tweet_sum_query_home(request):
    return render(request, 'tweet_sum_query/tweet_sum_query_home.html', {})