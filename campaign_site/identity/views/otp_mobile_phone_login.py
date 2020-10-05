from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from identity.models import UserEntity
from identity import forms,helper_send_otp



# Create your views here.
def mobile_phone_login(request):
    form = forms.RegisterForm

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = UserEntity.objects.get(mobile_phone_number=mobile)
                # send otp
                otp = helper_send_otp.get_random_otp() # create otp
                helper_send_otp.send_otp_soap(mobile, otp)  # send otp
                user.otp = otp
                user.save()
                request.session['user_mobile'] = user.mobile_phone_number
                print (otp) #check value of otp
                return HttpResponseRedirect(reverse('verify_otp_login'))


        except UserEntity.DoesNotExist:
            #print error message
            pass

    return render(request, 'mobile_phone_login.html', {'form': form})



def verify_otp_login(request):

    mobile = request.session.get('user_mobile')
    return render (request,'verify_otp_login.html',{'mobile':mobile})




def dashboard(request):
    return render (request , 'dashboard.html')


