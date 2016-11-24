# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response


def ignorcase_get(args, key):
    if not key:
        return ""
    if not args:
        return ""
    if key in args:
        return args[key]
    for old_key in args:
        if old_key.upper() == key.upper():
            return args[old_key]
    return ""


# Init and Query in batch.
@api_view(http_method_names=['POST', 'GET'])
def vnfs(request, *args, **kwargs):
    # if POST, then init VNF.
    if request._request.method == 'POST':
        resp_data = {
            "vnfinstanceid": "3",
            "jobid": "NF-CREATE-3-906322da-aa90-11e6-b216-fa163efb70d3"}
        ret = [0, resp_data, '200']
        return Response(data=resp_data, status=ret[2])

    # if GET, then Query in batch
    elif request._request.method == 'GET':
        resp_data = {
            "vnfinstanceid": "3",
            "VNFList": []}
        ret = [0, resp_data, '200']
        return Response(data=resp_data, status=ret[2])


# query and terminate
@api_view(http_method_names=['DELETE', 'GET'])
def vnf_detail(request, *args, **kwargs):
    # if GET, then Query.
    if request._request.method == 'GET':
        resp_data = {'unused': 'unused'}
        ret = [0, resp_data, '200']
        return Response(data=resp_data, status=ret[2])

    # if DELETE, then terminate VNF.
    elif request._request.method == 'DELETE':
        resp_data = {"jobid": "VNF-CANCEL-3-b511e590-ab25-11e6-a9f8-fa163efb70d3"}
        ret = [0, resp_data, '200']
        return Response(data=resp_data, status=ret[2])


@api_view(http_method_names=['GET'])
def job_status(request, *args, **kwargs):
    resp_data = {
        "jobid": "NF-CREATE-7-de65ee14-a279-11e6-819d-fa163e91c2f9",
        "responsedescriptor": {
            "errorcode": "",
            "progress": 100,
            "responsehistorylist": [
                {
                    "errorcode": "",
                    "progress": 90,
                    "responseid": 86,
                    "status": "processing",
                    "statusdescription": "LCM notify success"
                },
                {
                    "errorcode": "",
                    "progress": 82,
                    "responseid": 85,
                    "status": "processing",
                    "statusdescription": "execute plugin notify extend"
                },
                {
                    "errorcode": "",
                    "progress": 81,
                    "responseid": 84,
                    "status": "processing",
                    "statusdescription": "LCM notify to nfvo"
                }
            ],
            "responseid": 87,
            "status": "finished",
            "statusdescription": "Init VNF finished."
        }
    }
    ret = [0, resp_data, '200']
    return Response(data=resp_data, status=ret[2])


@api_view(http_method_names=['PUT'])
def vnf_grant_lcm(request, *args, **kwargs):
    # M -> O
    # grant_vnf_url = "openoapi/ztevmanagerdriver/v1/resource/grant"
    resp_data = {}
    ret = [0, '{"tenant": "admin"}', '201']
    resp_data["vim"] = [{"viminfoid": 1,
                         "vimid": 1,
                         "accessinfo": [{"tenant": "admin"}]}]
    return Response(data=resp_data, status=ret[2])


@api_view(http_method_names=['POST'])
def nf_notification(request, *args, **kwargs):
    # M -> O
    # notification_vnf_url = "openoapi/ztevmanagerdriver/v1/vnfs/lifecyclechangesnotification"
    return Response(status='201')
