from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views
from wiki.serializers import TitleSerializer, DocumentSerializer
from wiki import models
from wiki.models import Title, Document
from collections import defaultdict
from wiki.helper import ResponseProcess
from wiki.config import document_data, title_data
from rest_framework.decorators import action
from datetime import datetime
import json
import requests

# Create your views here.
class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = TitleSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = TitleSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                response = ResponseProcess(data={"title_id": serializer.data["id"]}, message="Success", count=None)
                return response.successfull_response()
        except Exception as e:
            response = ResponseProcess([], str(e))
            return response.errord_response()


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        try:
            if 'title' in request.data:
                title_dict = {"title":request.data['title']}
                data = json.dumps(title_dict)
                response_title = requests.post(url=f"http://127.0.0.1:8000/api/v1/title/", data=data, headers=request.headers)

                response_title_parsed = json.loads(response_title.content)
                request.data['title_id'] = response_title_parsed['id']
            serializer = DocumentSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                response = ResponseProcess(data=serializer.data, message="Success", count=None)
                return response.successfull_response()
        except Exception as e:
            response = ResponseProcess([], str(e))
            return response.errord_response()

    def list(self, request, *args, **kwargs):
        try:
            timestamp_flag = False
            find_title = request.GET.get('title', None)
            timestamp = request.GET.get('timestamp', None)
            latest = request.GET.get('latest', None)
            final_data = []
            for data in (title_data):
                for element in document_data:
                    if element['title_id'] == data['id']:
                        element['title'] = data['title']
            final_data = document_data
            if find_title is not None:
                if timestamp is not None:
                    requested_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    timestamp_flag = True
                title_list = []
                for data in document_data:
                    titles = str(data['title'])
                    if timestamp_flag == True:
                        data_timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')
                        if data_timestamp < requested_timestamp and find_title in titles:
                            title_list.append(data)
                    elif find_title in titles:
                        title_list.append(data)
                final_data = title_list

            if latest is not None:
                final_data = sorted(final_data, key=lambda i: i['timestamp'], reverse=True)

            if len(final_data) <= 0:

                response = ResponseProcess(data=final_data, message="No Data Found", count=len(final_data))
                return response.successfull_response()
            response = ResponseProcess(data=final_data, message="Success", count=len(final_data))
            return response.successfull_response()
        except Exception as e:
            response = ResponseProcess([], str(e))
            return response.errord_response()

    @action(methods=['GET'], detail=False)
    def titles(self, request):
        try:
            find_title = request.GET.get('title', None)
            if find_title is not None:
                for data in title_data:
                    titles = str(data['title'])
                    if find_title not in titles:
                        data.clear()
            final_data = title_data
            if len(final_data) <= 0:
                response = ResponseProcess(data=final_data, message="No Data Found", count=len(final_data))
                return response.successfull_response()
            response = ResponseProcess(data=final_data, message="Success", count=len(final_data))
            return response.successfull_response()
        except Exception as e:
            response = ResponseProcess([], str(e))
            return response.errord_response()
