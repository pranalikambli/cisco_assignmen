from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from django.http import JsonResponse


import json
from ipaddress import ip_address

from .serializers import RouterSerializer, RouterDetailsSerializer
from .models import RouterInfo
from .forms import RouterForm


class CreateRounterAPI(APIView):
    """
    Create a new router.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        router_obj = RouterInfo.objects.filter(is_active=True).all()
        serializer = RouterSerializer(router_obj, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        To create routers.
        :param request:
        :param format:
        :return: Status 200 on success else 404 for bad request
        """
        serializer = RouterSerializer(data=request.data)
        payload = request.data
        form = RouterForm(payload)
        if form.is_valid():
            if serializer.is_valid():
                data = RouterInfo.objects.create(
                    sapid=payload.get("sapid"),
                    hostname=payload.get("hostname"),
                    loopback=payload.get("loopback"),
                    mac_address=payload.get("mac_address"),
                )
                serializer = RouterSerializer(data)
                return Response({'data': serializer.data, 'msg': 'Record added successfully'},
                                status=status.HTTP_201_CREATED)
        return Response({'error': str(form.errors)}, status=status.HTTP_400_BAD_REQUEST)



class GetRoutersAPI(APIView):
    """
    List all routers.
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        obj = RouterInfo.objects.filter(is_active=True).all()
        serializer = RouterDetailsSerializer(obj, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class UpdateRouterAPI(APIView):
    """
    Update a new router.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, loopback, format=None):
        router_obj = RouterInfo.objects.filter(loopback=loopback, is_active=True).all()
        router_list = []
        for each in router_obj:
            router_list.append({"id": each.id,"sapid": each.sapid, "hostname": each.hostname, "loopback": each.loopback,
                                "mac_address": each.mac_address})
        return Response(router_list, status=status.HTTP_200_OK)

    def post(self, request, loopback, format=None):
        serializer = RouterSerializer(data=request.data)
        payload = request.data
        payload['loopback'] = loopback
        form = RouterForm(payload)
        if form.is_valid():
            import pdb
            pdb.set_trace()
            if serializer.is_valid():
                obj = RouterInfo.objects.filter(loopback=loopback, is_active=True).update(sapid=payload.get("sapid"),
                                                                                          hostname=payload.get(
                                                                                              "hostname"),
                                                                                          loopback=payload.get(
                                                                                              "loopback"),
                                                                                          mac_address=payload.get(
                                                                                              "mac_address"))

                serializer = RouterDetailsSerializer(payload)
                return Response({'data': serializer.data, 'msg': 'Record updated successfully'},
                                status=status.HTTP_200_OK)
        return Response({'error': str(form.errors)}, status=status.HTTP_400_BAD_REQUEST)

class DeleteRouterAPI(APIView):
    """
    Delete Router.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, loopback, format=None):
        router_obj = RouterInfo.objects.filter(loopback=loopback, is_active=True).all()
        router_list = []
        for each in router_obj:
            router_list.append({"id": each.id,"sapid": each.sapid, "hostname": each.hostname, "loopback": each.loopback,
                                "mac_address": each.mac_address})
        return Response(router_list, status=status.HTTP_200_OK)

    def delete(self, request, loopback, format=None):
        try:
            obj = RouterInfo.objects.filter(loopback=loopback, is_active=True).first()
            obj.is_active = False
            obj.save()
            return Response({'msg': 'Record Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete(request, loopback):
    user = request.user.id
    try:
        obj = RouterInfo.objects.filter(loopback=loopback, is_active=True).first()
        obj.is_active = False
        obj.save()
        return Response({'msg': 'Record Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetRoutersSapIdAPI(APIView):
    """
    List all routers by sapid.
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, sapid, format=None):
        obj = RouterInfo.objects.filter(sapid__icontains=sapid, is_active=True).all()
        serializer = RouterDetailsSerializer(obj, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)



class GetRoutersIpRangeAPI(APIView):
    """
    List all routers range between.
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, ip_range, format=None):
        start = ip_range.split("-")[0]
        end = ip_range.split("-")[1]
        start_int = int(ip_address(start).packed.hex(), 16)
        end_int = int(ip_address(end).packed.hex(), 16)
        ip_range = [ip_address(ip).exploded for ip in range(start_int, end_int + 1)]
        obj = RouterInfo.objects.filter(loopback__in=ip_range)
        serializer = RouterDetailsSerializer(obj, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
