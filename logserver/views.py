import logging
import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from logserver import services
from django import views

logger = logging.getLogger(settings.LOGGER)


class BrowserView(views.View):
    @staticmethod
    def get(request):
        dir_list = services.get_id_dirs()
        return render(
                request=request,
                template_name='logserver/browser.html',
                context={
                    'items': dir_list,
                }
            )


class BrowserIdView(views.View):
    @staticmethod
    def get(request, id):
        dir_list = services.get_list_of_logs(id=id)
        return render(
                request=request,
                template_name='logserver/browser_id.html',
                context={
                    'id': id,
                    'items': dir_list,
                }
            )


class BrowserDownloadFile(views.View):
    @staticmethod
    def get(request, id, file):
        return services.download_file_response(id, file)


class APILog(APIView):
    @staticmethod
    def get(request, id, start):
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def post(request, id, start):
        # start: 0 - new, 1 - continue, 2 - finalize
        logger.info(f"[URL]: {request.get_full_path()} | POST request data: {request.data}")
        if 'file' not in request.FILES and start != 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if start == 2:
            services.finalize_log(id=id)
            return Response(status=status.HTTP_200_OK)

        if start == 0:
            services.create_logs_dir(id=id)
            services.create_log_file(id=id)
        result = services.append_log(id=id, file_obj=request.FILES['file'])

        return Response(status=status.HTTP_200_OK) if result else Response(status=status.HTTP_406_NOT_ACCEPTABLE)
