from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from zeep import Client

from commons.views.basic_view import BasicView
from reserve.models import CampaignEntity

MERCHANT = '78d6c458-77e8-4570-a814-90452f0a5406'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')


class RequestZarinpal(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        camp_id = request.query_params.get('camp_id')
        campaign_entity = CampaignEntity.objects.get(id=camp_id)
        callback_url = 'http://95.156.252.188:8000/campaignDetail/{}/'.format(camp_id)
        cost = campaign_entity.cost
        description = campaign_entity.description
        email = request.user.email
        mobile = request.user.mobile_phone_number

        result = client.service.PaymentRequest(MERCHANT, cost, description, email, mobile, callback_url)

        if result.Status == 100:
            # TODO reserve temporary here.
            return Response(data='https://www.zarinpal.com/pg/StartPay/' + str(result.Authority),
                            status=status.HTTP_200_OK)
        else:
            return Response(data='Error code: ' + str(result.Status),
                            status=status.HTTP_400_BAD_REQUEST)


class VerifyZarinpal(BasicView, APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        camp_id = request.query_params.get('camp_id')
        campaign_entity = CampaignEntity.objects.get(id=camp_id)
        cost = campaign_entity.cost
        if request.GET.get('Status') == 'OK':
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], cost)
            if result.Status == 100:
                # TODO add student here to registered_users
                return Response(data='Transaction success.\nRefID: ' + str(result.RefID),
                                status=status.HTTP_200_OK)
            elif result.Status == 101:
                return Response(data='Transaction submitted : ' + str(result.Status),
                                status=status.HTTP_200_OK)
            else:
                return Response(data='Transaction failed.\nStatus: ' + str(result.Status),
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data='Transaction failed or canceled by user',
                            status=status.HTTP_400_BAD_REQUEST)
