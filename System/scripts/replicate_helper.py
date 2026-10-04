import os,sys,json,time,base64,urllib.request,urllib.error
TOK=os.environ["REPLICATE_API_TOKEN"]
def call(url,data=None):
    """One API call; a 429 (rate limit, nothing was created or charged) waits for Retry-After and retries up to 6 times."""
    for a in range(6):
        r=urllib.request.Request(url,data=json.dumps(data).encode() if data else None,headers={"Authorization":f"Bearer {TOK}","Content-Type":"application/json","User-Agent":"curl/8.5"})
        try:
            return json.load(urllib.request.urlopen(r,timeout=60))
        except urllib.error.HTTPError as e:
            if e.code!=429 or a==5: raise
            w=int(e.headers.get("Retry-After") or 12)+2;print("429, waiting",w,"s",flush=True);time.sleep(w)
def datauri(p,mime):
    return f"data:{mime};base64,"+base64.b64encode(open(p,"rb").read()).decode()
def run(model,inp):
    try:
        p=call(f"https://api.replicate.com/v1/models/{model}/predictions",{"input":inp})
    except urllib.error.HTTPError as e:
        if e.code!=404: raise
        v=call(f"https://api.replicate.com/v1/models/{model}")["latest_version"]["id"]
        p=call("https://api.replicate.com/v1/predictions",{"version":v,"input":inp})
    print("created",p["id"],flush=True)   # printed at once, so a prediction can be recovered if a later step hangs
    while p["status"] in("starting","processing"):
        time.sleep(2)
        try: p=call(p["urls"]["get"])
        except Exception as e: print("poll retry",str(e)[:50],flush=True);time.sleep(4)   # a network hiccup must not lose a paid prediction
    if p["status"]!="succeeded": raise SystemExit(f"{p['status']} {p.get('error')}")
    return p
def download(p,dest):
    """Downloads the output with a timeout and retries; the file is only written once fully read (no empty files)."""
    o=p["output"];o=o[0] if isinstance(o,list) else o
    for a in range(4):
        try:
            data=urllib.request.urlopen(urllib.request.Request(o,headers={"User-Agent":"curl/8.5"}),timeout=60).read()
            open(dest,"wb").write(data);return o
        except Exception as e:
            print("download retry",a+1,str(e)[:60],flush=True);time.sleep(3)
    raise SystemExit("download failed: "+o)
def log(p):
    print(p["id"],p["status"],p.get("metrics"),"https://replicate.com/p/"+p["id"])
def recover(pid,dest):
    """Fetches a finished prediction by id and saves its output (no new spend)."""
    p=call("https://api.replicate.com/v1/predictions/"+pid);download(p,dest);return p
