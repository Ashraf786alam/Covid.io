from django.shortcuts import render
import requests
import json
# Create your views here.
def homepage(request):
    result=requests.get('https://api.covid19api.com/summary')
    Globalsummary=result.json()['Global']
    countries=result.json()['Countries']
    print(type(countries))
    #print(type(OneDayCase))
    for country in countries:
        OneDayCase=requests.get('https://api.covid19api.com/dayone/country/country/status/confirmed')
        #d=OneDayCase.json()[]['Cases']
        print(OneDayCase.json()['Cases'])
        print("---------------------------------------")
        return render(request,'Covid/home.html',{'result':result,'Global':Globalsummary,'countries':countries})
