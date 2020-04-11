import requests

headers = {
    'authority': 'www.bigbasket.com',
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-dest': 'empty',
    'x-csrftoken': '3WCTjNB0lUeTrzbkNS67pyfTkMbm04nBtUDgOttWLKZzku9eHOvpstBUAvMyBILs',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'dnt': '1',
    'origin': 'https://www.bigbasket.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.bigbasket.com/basket/?ver=1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_bb_vid="MjM4NDM4NDAxMA=="; _bb_tc=0; _bb_rdt="MzE1Mjc5MjUyOA==.0"; _bb_rd=6; _ga=GA1.2.2080704515.1557381371; _vz=viz_5cd3c205e883e; _bb_source=pwa; _gcl_au=1.1.1106835971.1584554636; _fbp=fb.1.1584554636844.1029815039; adb=1; G_ENABLED_IDPS=google; _gcl_aw=GCL.1584953672.CjwKCAjwvOHzBRBoEiwA48i6Amoent09YkC7QIhvt03pluSvuDosxT-NjjYDHN7R_X-V2phQwiNCZBoCiyEQAvD_BwE; _gac_UA-27455376-1=1.1584953674.CjwKCAjwvOHzBRBoEiwA48i6Amoent09YkC7QIhvt03pluSvuDosxT-NjjYDHN7R_X-V2phQwiNCZBoCiyEQAvD_BwE; new_checkout=1; _bb_cid=1; _sp_van_encom_hid=1178; _bb_hid=1179; _sp_bike_hid=1176; G_AUTHUSER_H=0; BBAUTHTOKEN=MNCHhQsA6MWz5Tcp2CQaGYZ7ImNoYWZmIjogIkloc2tjejJXbzVCVFBnPT0iLCAidGltZSI6IDE1ODU5OTU5MzAuMjcyNzA5NiwgIm1pZCI6IDkzNTU1OTMsICJ2aWQiOiA5MDM3OTc5ODgsICJkZXZpY2VfaWQiOiAiV0VCIiwgInNvdXJjZV9pZCI6IDF9; _bb_aid="MzAxNzQ3OTgyNQ=="; _bb_mid="MzE0MjUwMzg0Nw=="; sessionid=1ahwfayyfma1g4z1js8bqauao90k2m6i; _client_version=2264; _gid=GA1.2.1117389379.1586527478; AKA_A2=A; csrftoken=3WCTjNB0lUeTrzbkNS67pyfTkMbm04nBtUDgOttWLKZzku9eHOvpstBUAvMyBILs; RT="z=1&dm=bigbasket.com&si=ca2ccaea-cef7-4882-b785-ec552009ebc8&ss=k8vdep2g&sl=5&tt=od5&obo=1&rl=1"; _gat_gtag_UA_27455376_1=1; bigbasket.com=1a8b7080-ee89-4f82-bf88-5a3cfc0eee34; ts="2020-04-11 14:29:22.981"',
}

response = requests.post('https://www.bigbasket.com/co/qc/stock/', headers=headers)
print(response.json())


def checkout():
    response = requests.post('https://www.bigbasket.com/co/update-po/', headers=headers, data=data).json()
    return response
