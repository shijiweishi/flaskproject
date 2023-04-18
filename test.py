import pprint
from pprint import pprint
import urllib.request
import json
import time
data1 = {'words_result': [{'location': {'top': 178, 'left': 198, 'width': 1198, 'height': 205}, 'words': '12345789'}, {'location': {'top': 417, 'left': 184, 'width': 1205, 'height': 192}, 'words': '23457890'}, {'location': {'top': 609, 'left': 719, 'width': 82, 'height': 151}, 'words': '6'}], 'words_result_num': 3, 'log_id': 1646331549359870882}
data2 = {'words_result': [{'location': {'top': 0, 'left': 751, 'width': 2725, 'height': 264}, 'words': '2020字年河南省(部分地市)新高'}, {'location': {'top': 103, 'left': 3598, 'width': 986, 'height': 259}, 'words': '考联盟高一12月教'}, {'location': {'top': 331, 'left': 2838, 'width': 1250, 'height': 318}, 'words': '数学答题卡'}, {'location': {'top': 727, 'left': 347, 'width': 684, 'height': 225}, 'words': '姓名:'}, {'location': {'top': 706, 'left': 1472, 'width': 1216, 'height': 390}, 'words': '师小权'}, {'location': {'top': 1146, 'left': 4335, 'width': 284, 'height': 173}, 'words': '贴  条'}, {'location': {'top': 1354, 'left': 329, 'width': 675, 'height': 194}, 'words': '考生号:'}, {'location': {'top': 1327, 'left': 1149, 'width': 2316, 'height': 343}, 'words': '124689752'}, {'location': {'top': 1614, 'left': 1203, 'width': 1986, 'height': 368}, 'words': '1324689752'}, {'location': {'top': 1790, 'left': 3836, 'width': 781, 'height': 121}, 'words': '1.答题前,考生先将'}, {'location': {'top': 1968, 'left': 3957, 'width': 22, 'height': 45}, 'words': '0'}, {'location': {'top': 1932, 'left': 4301, 'width': 311, 'height': 92}, 'words': '置,并正'}, {'location': {'top': 2077, 'left': 4425, 'width': 137, 'height': 69}, 'words': '姓名'}, {'location': {'top': 2257, 'left': 3057, 'width': 115, 'height': 69}, 'words': '0'}, {'location': {'top': 2237, 'left': 3312, 'width': 144, 'height': 83}, 'words': '0'}, {'location': {'top': 2345, 'left': 413, 'width': 239, 'height': 1049}, 'words': 'BBBBE'}, {'location': {'top': 2334, 'left': 772, 'width': 243, 'height': 1040}, 'words': 'd BBBE'}, {'location': {'top': 2248, 'left': 2736, 'width': 212, 'height': 548}, 'words': '0田团'}, {'location': {'top': 2422, 'left': 3337, 'width': 137, 'height': 117}, 'words': '1'}, {'location': {'top': 2610, 'left': 3370, 'width': 124, 'height': 117}, 'words': '2'}, {'location': {'top': 2596, 'left': 3736, 'width': 149, 'height': 164}, 'words': '意'}, {'location': {'top': 2643, 'left': 3917, 'width': 270, 'height': 121}, 'words': '3.答非'}, {'location': {'top': 2621, 'left': 4463, 'width': 85, 'height': 83}, 'words': '时'}, {'location': {'top': 2817, 'left': 3388, 'width': 99, 'height': 97}, 'words': '3'}, {'location': {'top': 2826, 'left': 3766, 'width': 149, 'height': 187}, 'words': '事'}, {'location': {'top': 2774, 'left': 4025, 'width': 203, 'height': 137}, 'words': '笔书'}, {'location': {'top': 2750, 'left': 4459, 'width': 115, 'height': 103}, 'words': '求'}, {'location': {'top': 2896, 'left': 1158, 'width': 121, 'height': 200}, 'words': '0'}, {'location': {'top': 2946, 'left': 2214, 'width': 69, 'height': 67}, 'words': '0'}, {'location': {'top': 2919, 'left': 4041, 'width': 209, 'height': 139}, 'words': '指示'}, {'location': {'top': 2894, 'left': 4395, 'width': 209, 'height': 108}, 'words': '题区'}, {'location': {'top': 3029, 'left': 3434, 'width': 60, 'height': 92}, 'words': '4'}, {'location': {'top': 3086, 'left': 3795, 'width': 119, 'height': 149}, 'words': '项'}, {'location': {'top': 3097, 'left': 4070, 'width': 65, 'height': 92}, 'words': '效'}, {'location': {'top': 3027, 'left': 4305, 'width': 311, 'height': 144}, 'words': 'E试题卷'}, {'location': {'top': 3172, 'left': 3973, 'width': 645, 'height': 200}, 'words': '4.保持答题卡清'}, {'location': {'top': 3398, 'left': 4111, 'width': 38, 'height': 40}, 'words': '材'}, {'location': {'top': 3328, 'left': 4188, 'width': 381, 'height': 137}, 'words': '在答题卡'}], 'words_result_num': 38, 'log_id': 1646334962496543520}
data3 = {'words_result': [{'location': {'top': 178, 'left': 198, 'width': 1198, 'height': 205}, 'words': '12345789'}, {'location': {'top': 417, 'left': 184, 'width': 1205, 'height': 192}, 'words': '23457890'}, {'location': {'top': 609, 'left': 719, 'width': 82, 'height': 151}, 'words': '6'}], 'words_result_num': 3, 'log_id': 1646340221665581368}
data4 = {'words_result': [{'location': {'top': 361, 'left': 1239, 'width': 589, 'height': 2912}, 'words': '134516733'}, {'location': {'top': 392, 'left': 1923, 'width': 564, 'height': 3510}, 'words': '72468131'}, {'location': {'top': 3644, 'left': 1492, 'width': 239, 'height': 221}, 'words': '0'}], 'words_result_num': 3, 'log_id': 1646343354858389973}
# pprint(data4)
# print(time.time())

class Token():
    def __init__(self):
        self.born_time = time.time()
        self.token = self.calculate_token()

    def get_token(self):
        age = time.time() - self.born_time
        expire_time = 28 * 24 * 60 * 60  # 28天
        # expire_time=5#5秒
        if age > expire_time:
            self.token = self.calculate_token()
            self.born_time = time.time()
        return self.token

    def calculate_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=NC5SdNh5xZyIcqRGc25zwyBz&client_secret=5oGQAcPHwZuR3xDusU3u5sv86zCbMmBO'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        token = json.loads(bytes.decode(response.read()))
        return token['access_token']

token = Token()
for i in range(5):
    print(token.calculate_token())