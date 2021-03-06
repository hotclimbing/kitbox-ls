from django.urls import path

from logserver.views import LogsView, LogsIdView, LogsDownload, PingView, MainView, LogParseAndDownload, PingStatView, \
    PosTestView, MQTTView, MQTTDeviceView

from logserver.APIviews import APILog, APIPing, APIServer, APITestSmall, APITestBig, APIPosTest

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('logs/', LogsView.as_view(), name='logs'),
    path('logs/<int:id>/', LogsIdView.as_view(), name='logs_id'),
    path('logs/<int:id>/<str:file>', LogsDownload.as_view(), name='logs_download'),
    path('logs/<int:id>/parse/<str:file>', LogParseAndDownload.as_view(), name='logs_parse'),
    path('ping/', PingView.as_view(), name='ping'),
    path('ping/stat/', PingStatView.as_view(), name='ping_stat'),
    path('pos_test/', PosTestView.as_view(), name='pos_test'),
    path('mqtt/', MQTTView.as_view(), name='mqtt'),
    path('mqtt/<int:modem_id>', MQTTDeviceView.as_view(), name='mqtt_device'),

    path('api/v0/<int:id>/<int:start>/', APILog.as_view(), name='api_log'),
    path('api/v0/<int:id>/ping/', APIPing.as_view(), name='api_ping'),
    path('api/v0/server/', APIServer.as_view(), name='api_server'),

    path('api/v1/test_small', APITestSmall.as_view(), name='api_test_small'),
    path('api/v1/test_big', APITestBig.as_view(), name='api_test_big'),

    path('api/v2/pos_test', APIPosTest.as_view(), name='api_pos_test'),

]
