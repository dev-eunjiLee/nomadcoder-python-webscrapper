import requests
import beautifulsoup

url = "https://www.jobkorea.co.kr/Search/?stext=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

payload = {}
headers = {
    'Cookie': 'GTMVars=63787639f127dd435acf409c37584ef6; GTMVarsFrom=NET:23:29:14; jobkorea=Site_Oem_Code=C1; sm=keyword=%ed%8c%8c%ec%9d%b4%ec%8d%ac; ASP.NET_SessionId=iciupylo343lpverctrfpjgm'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
