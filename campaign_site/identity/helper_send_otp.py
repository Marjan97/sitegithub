from campaign_site.settings import Kavenegar_API
from kavenegar import *
from random import randint



def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API,timeout=20)
        params = {
            'sender': '1000596446',  # optional
            'receptor': mobile,   # multiple mobile number, split by comma
            'message': 'Your OTP is {}'.format(otp),
        }
        response = api.sms_send(params)
        print('OTP: ', otp)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return  randint(1000, 9999)