from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json

@method_decorator(csrf_exempt, name='dispatch')
class AirtimeRequestView(View):
    def post(self, request):
        data = json.loads(request.body)

        print(data)
        ret = {"fulfillmentText":"Data Saved"}
        return HttpResponse(json.dumps(ret))