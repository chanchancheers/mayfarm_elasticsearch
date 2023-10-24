import json
f = open("/home/sineuncha/elasticsearches/crawl_yhn.json", "rt")

data = json.load(f)

ndjsonList = [] 

for i, n in enumerate(data):
    command = { "create" : {"_id" : n.pop("_id"), "_index" : "yhn"}}
    n.pop("html_contents")
    n.pop("table_nm")
    n.pop("collector")
    n.pop("server")
    n.pop("log_id")
    n.pop("spider")
    ndjsonList.append(json.dumps(command, ensure_ascii=False))        
    ndjsonList.append(json.dumps(n, ensure_ascii=False))        
f.close()

lines = "\n".join(ndjsonList).encode('utf-8')
lines = lines + "\n"
f = open("ndjson.json", "w")
f.write(lines)
f.close()