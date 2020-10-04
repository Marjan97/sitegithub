from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from identity.models import UserEntity
from identity.forms import RegisterForm
from identity.helper_send_otp import *


# Create your views here.
def register_view(request):
    form = forms.RegisterForm

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = UserEntity.objects.get(mobile_phone_number=mobile)
                # send otp
                otp = helper.get_random_otp()
                helper.send_otp(mobile, otp)
                # save otp
                # print(otp)
                user.otp = otp
                user.save()
                #redirect to verify page
                return HttpResponseRedirect (reverse('verify.html'))

        except MyUser.DoesNotExist:
            #print error message
            pass

    return render(request, 'register.html', {'form': form})



def verify(request):
    return render (request,'verify.html')














# def mobile_login(request):
#     if request.method=="POST":
#         if "mobile" in request.POST:
#             mobile=request.POST.get('mobile')
#             user=UserEntity.objects.get(mobile_phone_number=mobile)
#             login(request,user)
#
#             # return HttpResponseRedirect (reverse('dashboard'),{'user':user})
#             return render(request, 'dashboard.html',{'user':user})
#
#     return render (request,'mobile_login.html')

def dashboard(request):
    return render (request , 'dashboard.html')


# class SendOTPToMobilePhone:
#     pass