from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'tweet_sum_query/post_list.html', {})