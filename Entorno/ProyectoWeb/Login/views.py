from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# def Principal(request):
#     return render(request,'login.html',{})

    
# def Landing(request):
#     return render(request,'landing.html',{})

from django.contrib.auth import authenticate
from django.shortcuts import redirect

class LandingClass(View):
    template='Landing/landing.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template,{})
    

    def post(self,request,*args,**kwargs):
        return render(request,self.template,{})

class DashboardClass(View):
    templates='Dashboard/dashboard.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.templates,{})
    



class LoginClass(View):
    template='Login/login.html'
    template_Ok='Dashboard/dashboard.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template,{})
    
    def post(self,request,*args,**kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_sesion= authenticate(username= user_post , password=password_post)
        if user_sesion is None:
            self.message='Error Contraseña o Usuario Incorrecto'
            
            # return render(request,self.template_Ok,{})
        else:
            return redirect('Login:dashboard')
            
        
        return render(request,self.template,self.get_contex())

    def get_contex(self):
        return{
            'error':self.message
        }



        


     