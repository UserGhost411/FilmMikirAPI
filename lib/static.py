import os
import json
env = json.loads(str(os.environ.get("filmapi")))
KincirAPI = {
    'url': 'https://www.kincir.com/',
    'key': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aSI6MCwidXQiOiIiLCJhaSI6IjZiOTQwN2ZjLWU1ZWItNDFmNy05NjM4LWRlMWE2ODI5ZTRjYyIsImlhIjoiMjAyMi0wMS0xMlQxMDoxODo1Ni42OTQ0NTQ0MDNaIiwiYXUiOmZhbHNlLCJybSI6ZmFsc2UsInVkIjoiazF1aWNqOWpvOSIsImRkIjpudWxsLCJleHAiOjE2NDE5OTM1MzZ9.TuZ9kVSIOtrQb6eJ_oTZXyjzT-EpciBOiXaKbAMObOiR6yrZYl4fA-1IdVl6q9ZTiKr99ChMFpMahws8vcn79QumR2Z2HvEjf6MqjxKDEun5xscUM2kLFnNSAcOhpa4PPk8hSq2p0WjkefGN79brBYvKRe2sI5KL3gD3-yabuZQ',
    'cdn': 'https://cdn.kincir.com/',
    'expired': 0,
    'auth': {"clientId":str(env['a']),"type":"anonymous"}
}
IMDBAPI = {
    'url': 'https://imdb-api.com/',
    'key':str(env['b'])
}
urlBaseIMDB = ''
VersionScrap = '1.0 By UserGhost411'
DocumentationUrl = 'https://github.com/UserGhost411/repo'
errorMessage = {"status":0,"msg":"cant find spesific endpoint,Please Check our documentation","documentation":DocumentationUrl}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
