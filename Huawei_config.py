from netmiko  import ConnectHandler
import time
import logging


logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

date = time.strftime('%Y%m%d', time.localtime())

host = {
    '1.1.1.1',
    '2.2.2.2',
    '3.3.3.3',

};

for ip in host:

    huawei = {
        'device_type': "huawei",
        'ip': ip,
        'port': '22',
        'username': 'user',
        'password': 'senha',
        "global_delay_factor": 4,
    }
    try:
        huawei_connect = ConnectHandler(**huawei)
        print("Sucessfully Login to", ip)
        input = huawei_connect.send_config_set(open('display.txt').readlines())
        print(input)
        print(ip, 'Was finished!\n', "-" * 100)
        save_config = open("backup-{}".format(ip.strip()) + ".txt", "+w")
        save_config.write(input)
        save_config.close()
    except:
        e3 = open(f'{date}.txt', 'a')
        print(date, ip, '[Error 3] Unknown error.\n', file=e3)
        e3.close



