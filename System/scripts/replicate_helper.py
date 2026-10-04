import os,sys,json,time,base64,urllib.request
TOK=os.environ["REPLICATE_API_TOKEN"]
def call(url,data=None):
    r=urllib.request.Request(url,data=json.dumps(data).encode() if data else None,headers={"Authorization":f"Bearer {TOK}","Content-Type":"application/json","User-Agent":"curl/8.5"})
    return json.load(urllib.request.urlopen(r))
def datauri(p,mime):
    return f"data:{mime};base64,"+base64.b64encode(open(p,"rb").read()).decode()
def run(model,inp):
    try:
        p=call(f"https://api.replicate.com/v1/models/{model}/predictions",{"input":inp})
    except urllib.error.HTTPError as e:
        if e.code!=404: raise
        v=call(f"https://api.replicate.com/v1/models/{model}")["latest_version"]["id"]
        p=call("https://api.replicate.com/v1/predictions",{"version":v,"input":inp})
    while p["status"] in("starting","processing"):
        time.sleep(2);p=call(p["urls"]["get"])
    if p["status"]!="succeeded": raise SystemExit(f"{p['status']} {p.get('error')}")
    return p
def download(p,dest):
    o=p["output"];o=o[0] if isinstance(o,list) else o
    open(dest,"wb").write(urllib.request.urlopen(urllib.request.Request(o,headers={"User-Agent":"curl/8.5"})).read());return o
def log(p):
    print(p["id"],p["status"],p.get("metrics"),"https://replicate.com/p/"+p["id"])
