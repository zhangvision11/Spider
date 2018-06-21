import requests
k = requests.get('https://www.amazon.com/Girl-Wash-Your-Face-Believing/dp/1400201659?pd_rd_wg=nJ3FL&pd_rd_r=fe24e1e8-c60e-48b9-93d4-e5500a260724&pd_rd_w=RWT6t&ref_=pd_gw_ri&pf_rd_r=CWWDR9W3VGE7TTNR1X8P&pf_rd_p=a76d819d-d46f-5d89-be3e-dc07c7b5bb0c').text
print(k)