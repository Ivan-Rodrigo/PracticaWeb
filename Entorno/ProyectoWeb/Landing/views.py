from django.shortcuts import render

from django.views.generic import View
from django.contrib.auth import authenticate
from django.shortcuts import redirect

class LandingClass(View):
    template='Landing/landing.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template,{})
    

    def post(self,request,*args,**kwargs):
        return render(request,self.template,{})

