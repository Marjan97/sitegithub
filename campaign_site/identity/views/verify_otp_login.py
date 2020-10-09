from identity.models import UserEntity
from django.contrib.auth import login
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import render
from identity import helper_send_otp



def verify(request):
    try:
        mobile = request.session.get('user_mobile')
        user = UserEntity.objects.get(mobile_phone_number = mobile)

        if request.method == "POST":

            # check otp expiration
            if not helper_send_otp.check_otp_expiration(user.mobile_phone_number):
                return HttpResponseRedirect(reverse('mobile_phone_login'))

            if user.otp != int(request.POST.get('otp')):
                return HttpResponseRedirect(reverse('verify_otp_login'))

            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, 'verify_otp_login.html', {'mobile': mobile})

    except UserEntity.DoesNotExist:
        return HttpResponseRedirect(reverse('mobile_phone_login'))