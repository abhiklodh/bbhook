import requests

cookies = {
    #'_bb_vid': 'NDA3NDUyNjc1Mw==',
    #'_bb_tc': '0',
    #'_bb_rdt': 'MzE0OTAzMTg4Mg==.0',
    #'_bb_rd': '6',
    #'_gcl_au': '1.1.1733047202.1586102939',
    #'_ga': 'GA1.2.485530518.1586102939',
    #'_fbp': 'fb.1.1586102939745.1996533082',
    #'G_ENABLED_IDPS': 'google',
    #'adb': '0',
    #'BBAUTHTOKEN': 'MLVYC+fUSi449Z1xoIZHoC57ImNoYWZmIjogIjVnd1dkWkZNN0ZraWlRPT0iLCAidGltZSI6IDE1ODYxMDI5NjYuOTg2NDY3MSwgIm1pZCI6IDk5ODU2MTEsICJ2aWQiOiAxMjI2NTkzNDg3LCAiZGV2aWNlX2lkIjogIldFQiIsICJzb3VyY2VfaWQiOiAxfQ==',
    '_bb_mid': 'MzE0MzEyNzcxNw==',
    'sessionid': 'tvgo6fj8ony2arfbxfbjxnafg8kkiixc',
    #'_bb_hid': '898',
    #'_sp_bike_hid': '899',
    #'_bb_cid': '18',
    #'_bb_aid': 'MzAxODk4MTA4Mw==',
    #'_vz': 'viz_5e8a0301e8938',
    #'_client_version': '2263',
    #'AKA_A2': 'A',
    #'_gid': 'GA1.2.1450438360.1586353595',
    #'new_checkout': '1',
    'csrftoken': 'gEjvfAzMxZ3PFRfPbrHag2Gcc2EXdkrBwOke3tDZKmVaMKfdiooU4NhIFzO0PXyC',
    #'RT': 'z=1&dm=bigbasket.com&si=blrsv3ec02h&ss=k8rdyiyo&sl=4&tt=2n12&obo=1&rl=1',
    #'bigbasket.com': 'b632b01d-d9d4-401d-a9d9-4668582ef90e',
    #'ts': '2020-04-08 19:29:05.271',
}

headers = {
    # 'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    # 'DNT': '1',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRFToken': 'gEjvfAzMxZ3PFRfPbrHag2Gcc2EXdkrBwOke3tDZKmVaMKfdiooU4NhIFzO0PXyC',
    # 'Origin': 'https://www.bigbasket.com',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.bigbasket.com/basket/?ver=1',
    # 'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'addr_id': '137490997'
}

response = requests.post('https://www.bigbasket.com/co/update-po/', headers=headers, cookies=cookies, data=data)

print(response.json())