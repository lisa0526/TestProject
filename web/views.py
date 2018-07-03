from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
import json
# Create your views here.
def login(request):
    if request.method=='POST':
        result={}
        username=request.POST.get('username')
        password=request.POST.get('password')
        result['user']=username
        result['pass']=password
        result=json.dumps(result,indent=2,sort_keys=True)
        return HttpResponse(result,content_type='application/json;charest=utf-8')
    else:
        return render_to_response('login.html')
