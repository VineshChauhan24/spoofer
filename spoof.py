import json
from mitmproxy.http import HTTPResponse
from mitmproxy import http



def jsonparser(response):
    jsondata = json.dumps(response)
    return jsondata


def requestmaker(jsondata):
    converToString = jsonparser(jsondata).encode('utf-8')

    jsonResponse = http.HTTPResponse.make(
        200,  # (optional) status code
        converToString,  # (optional) content
        {"Content-Type": "application/json"}  # (optional) headers
    )
    return jsonResponse



answers = ({"access_token": "admin", "status": "ok"},
           {"licenses": [{"id": 1, "expirary": 0, "type": "Admin", "activated": True,
                          "purchase_date": 1548114184.1072772, "hwid": "8a489e698bb2e7aee3ec0cd14e1fac0cf03b713f6118c0d8544cc291793d3287"}], "status": "ok"},
           {"success": True, "message": "", "status": "ok"})

requestResponse = list(map(requestmaker, answers))


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.startswith('https://grammultitool.com/api/v1/user/authenticate'):
        flow.response = requestResponse[0]

    elif flow.request.pretty_url.startswith('https://grammultitool.com/api/v1/user/licenses/?access_token='):
        flow.response = requestResponse[1]

    elif flow.request.pretty_url.startswith('https://grammultitool.com/api/v1/user/licenses/1/register?'):
        flow.response = requestResponse[2]
