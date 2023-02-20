import requests

def req(js0n :dict=None, r=None):
    if js0n != None and isinstance(js0n, dict):
        if "r" in js0n and js0n["r"] != None:
            r_ = js0n["r"]
        else:
            if r != None:
                r_ = r
            else:
                r_ = None
        if "method" in js0n and js0n["method"] != None:
            method_ = js0n["method"]
        else:
            method_ = None
        if "url" in js0n and js0n["url"] != None:
            url_ = js0n["url"]
        else:
            url_ = None
        if "params" in js0n and js0n["params"] != None:
            params_ = js0n["params"]
        else:
            params_ = None
        if "data" in js0n and js0n["data"] != None:
            data_ = js0n["data"]
        else:
            data_ = None
        if "headers" in js0n and js0n["headers"] != None:
            headers_ = js0n["headers"]
        else:
            headers_ = None
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            aftermethod_ = js0n["aftermethod"]
        else:
            aftermethod_ = None
        if r_ != None and method_ != None and url_ != None and aftermethod_ != None:
            try:
                re = r_.request(
                    method=method_,
                    url=url_,
                    params=params_,
                    data=data_,
                    headers=headers_
                )
            except Exception:
                re = None
            if re != None:
                out = None
                aftermethod_ = str(aftermethod_).lower()
                if aftermethod_ == "text":
                    out = re.text
                if aftermethod_ == "json":
                    out = re.json()
                if aftermethod_ == "content":
                    out = re.content
                if aftermethod_ == "r":
                    out = re
                return out