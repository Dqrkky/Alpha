import html_to_json
import shared

class Alpha:
    def __init__(self):
        with shared.requests.Session() as rss:
            self.rss = rss
    def live(self):
        data0 = shared.req(
            js0n={
                "method": "get",
                "url": "https://www.alphatv.gr/live",
                "aftermethod": "text"
            },
            r=self.rss
        )
        if data0 != None and isinstance(data0, str):
            data1 = html_to_json.convert(html_string=data0)
            data_out = {
                "program": [],
                "m3u8": None
            }
            if data1 != None and isinstance(data1, dict):
                if "html" in data1 and data1["html"] != None and isinstance(data1["html"], list) and len(data1["html"]) > 0:
                    for html0 in data1["html"]:
                        if html0 != None and isinstance(html0, dict):
                            if "body" in html0 and html0["body"] != None and isinstance(html0["body"], list) and len(html0["body"]) > 0:
                                for body0 in html0["body"]:
                                    if body0 != None and isinstance(body0, dict):
                                        for div0 in body0["div"]:
                                            if div0 != None and isinstance(div0, dict):
                                                if "main" in div0 and div0["main"] != None and isinstance(div0["main"], list) and len(div0["main"]) > 0:
                                                    for main0 in div0["main"]:
                                                        if main0 != None and isinstance(main0, dict):
                                                            if "div" in main0 and main0["div"] and isinstance(main0["div"], list) and len(main0["div"]) > 0:
                                                                for div1 in main0["div"]:
                                                                    if div1 != None and isinstance(div1, dict):
                                                                        if "div" in div1 and main0["div"] and isinstance(div1["div"], list) and len(div1["div"]) > 0:
                                                                            for div2 in div1["div"]:
                                                                                if div2 != None and isinstance(div2, dict):
                                                                                    if "div" in div2 and div2["div"] != None and isinstance(div2["div"], list) and len(div2["div"]) > 0:
                                                                                        for div3 in div2["div"]:
                                                                                            if div3 != None and isinstance(div3, dict):
                                                                                                if "div" in div3 and div3["div"] != None and isinstance(div3["div"], list) and len(div3["div"]) > 0:
                                                                                                    for div4 in div3["div"]:
                                                                                                        if div4 != None and isinstance(div4, dict):
                                                                                                            if "ul" in div4 and div4["ul"] != None and isinstance(div4["ul"], list) and len(div4["ul"]) > 0:
                                                                                                                for ul0 in div4["ul"]:
                                                                                                                    if ul0 != None and isinstance(ul0, dict):
                                                                                                                        if "li" in ul0 and ul0["li"] != None and isinstance(ul0["li"], list) and len(ul0["li"]) > 0:
                                                                                                                            for li0 in ul0["li"]:
                                                                                                                                if li0 != None and isinstance(li0, dict):
                                                                                                                                    if "div" in li0 and li0["div"] != None and isinstance(li0["div"], list) and len(li0["div"]) > 0:
                                                                                                                                        liveshowing = {
                                                                                                                                            "title": None,
                                                                                                                                            "image": None,
                                                                                                                                            "start_time": None
                                                                                                                                        }
                                                                                                                                        for div5 in li0["div"]:
                                                                                                                                            if div5 != None and isinstance(div5, dict):
                                                                                                                                                if "span" in div5 and div5["span"] != None and isinstance(div5["span"], list) and len(div5["span"]) > 0:
                                                                                                                                                    for span0 in div5["span"]:
                                                                                                                                                        if span0 != None and isinstance(span0, dict):
                                                                                                                                                            if "a" in span0 and span0["a"] != None and isinstance(span0["a"], list) and len(span0["a"]) > 0:
                                                                                                                                                                for a0 in span0["a"]:
                                                                                                                                                                    if a0 != None and isinstance(a0, dict):
                                                                                                                                                                        if "_value" in a0 and a0["_value"] != None and isinstance(a0["_value"], str):
                                                                                                                                                                            liveshowing["start_time"] = a0["_value"]
                                                                                                                                                if "h4" in div5 and div5["h4"] != None and isinstance(div5["h4"], list) and len(div5["h4"]) > 0:
                                                                                                                                                    for h40 in div5["h4"]:
                                                                                                                                                        if h40 != None and isinstance(h40, dict):
                                                                                                                                                            if "a" in h40 and h40["a"] != None and isinstance(h40["a"], list) and len(h40["a"]) > 0:
                                                                                                                                                                for a1 in h40["a"]:
                                                                                                                                                                    if a1 != None and isinstance(a1, dict):
                                                                                                                                                                        if "_value" in a1 and a1["_value"] != None and isinstance(a1["_value"], str):
                                                                                                                                                                            liveshowing["title"] = a1["_value"]
                                                                                                                                    if "_attributes" in li0 and li0["_attributes"] != None and isinstance(li0["_attributes"], dict):
                                                                                                                                        if "style" in li0["_attributes"] and li0["_attributes"]["style"] != None and isinstance(li0["_attributes"]["style"], str):
                                                                                                                                            liveshowing["image"] = li0["_attributes"]["style"].split("'")[1]
                                                                                                                                    if liveshowing["title"] != None and liveshowing["image"] != None and liveshowing["start_time"] != None:
                                                                                                                                        data_out["program"].append(liveshowing)
                                                                                                if "_attributes" in div3 and div3["_attributes"] != None and isinstance(div3["_attributes"], dict):
                                                                                                    if "data-liveurl" in div3["_attributes"] and div3["_attributes"]["data-liveurl"] != None and isinstance(div3["_attributes"]["data-liveurl"], str):
                                                                                                        data_out["m3u8"] = div3["_attributes"]["data-liveurl"]
            return data_out
    def program(self, date :str=None):
        if date != None and isinstance(date, str):
            data0 = shared.req(
                js0n={
                    "method": "get",
                    "url": "https://www.alphatv.gr/ajax/Isobar.AlphaTv.Components.Program.Program.GetCustomDateList",
                    "params": {
                        "date": date
                    },
                    "aftermethod": "text"
                },
                r=self.rss
            )
            if data0 != None and isinstance(data0, str):
                data1 = html_to_json.convert(html_string=data0)
                data_out = {
                    "program": []
                }
                if data1 != None and isinstance(data1, dict):
                    if "ul" in data1 and data1["ul"] != None and isinstance(data1["ul"], list) and len(data1["ul"]) > 0:
                        for ul0 in data1["ul"]:
                            if ul0 != None and isinstance(ul0, dict):
                                if "li" in ul0 and ul0["li"] != None and isinstance(ul0["li"], list) and len(ul0["li"]):
                                    for li0 in ul0["li"]:
                                        if li0 != None and isinstance(li0, dict):
                                            if "a" in li0 and li0["a"] != None and isinstance(li0["a"], list) and len(li0["a"]) > 0:
                                                for a0 in li0["a"]:
                                                    if a0 != None and isinstance(a0, dict):
                                                        if "span" in a0 and a0["span"] != None and isinstance(a0["span"], list) and len(a0["span"]) > 0:
                                                            program = {
                                                                "title": None,
                                                                "description": None,
                                                                "start_time": None
                                                            }
                                                            dummy = {
                                                                "tvShowTitle": "title",
                                                                "showType": "description",
                                                                "schTime": "start_time"
                                                            }
                                                            for span0 in a0["span"]:
                                                                if span0 != None and isinstance(span0, dict):
                                                                    if "_attributes" in span0 and span0["_attributes"] != None and isinstance(span0["_attributes"], dict) and "_value" in span0 and span0["_value"] != None and isinstance(span0["_value"], str):
                                                                        if "class" in span0["_attributes"] and span0["_attributes"]["class"] != None and isinstance(span0["_attributes"]["class"], list) and len(span0["_attributes"]["class"]) > 0:
                                                                            if span0["_attributes"]["class"][0] in dummy:
                                                                                program[dummy[span0["_attributes"]["class"][0]]] = span0["_value"]
                                                            if program["title"] != None and program["description"] != None and program["start_time"] != None:
                                                                data_out["program"].append(program)
                return data_out