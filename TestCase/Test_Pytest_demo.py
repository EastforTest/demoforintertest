import requests
from xToolkit import xfile
import pytest

list_data = xfile.read('demo_data.xls').excel_to_dict(sheet=0)

cookies = {}
@pytest.mark.parametrize('datas',list_data)
def test_Case(datas):

    #如果需要cookie, 请求中就携带cookie
    #发起接口请求
    if datas['cookie'] == 'need' and datas['data'] =='':
        res = requests.request(datas['method'],datas['url'], cookies = cookies)
    elif datas['cookie'] == 'need':
        res = requests.request(datas['method'], datas['url'], cookies=cookies, data=eval(datas['data']))
    else:
        res = requests.request(datas['method'], datas['url'], data=eval(datas['data']))
        #print('---2---',datas['interface_name'])

    # 如果需要存cookie，就获取cookie信息
    if datas['cookie'] == 'save':
        cookies['session'] = res.cookies.get('session')


    assert res.json()['code'] == 200

if __name__ == '__main__':
    pytest.main(['-vs', '--capture=sys'])

