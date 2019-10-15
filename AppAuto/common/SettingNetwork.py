# coding:utf-8
__author__ = 'GRUNMI'


from appium.webdriver.connectiontype import ConnectionType

class NetworkType:
    def __init__(self, driver):
        self.driver = driver

    def get_network(self):
        info = {
            "0": "NO_CONNECTION",
            "1": "AIRPLANE_MODE",
            "2": "WIFI_ONLY",
            "4": "DATA_ONLY",
            "6": "ALL_NETWORK_ON"
        }
        network = info.get("{}".format(self.driver.network_connection))
        return network

    def set_network(self, num):
        network_type = {
            0: ConnectionType.NO_CONNECTION,
            1: ConnectionType.AIRPLANE_MODE,
            2: ConnectionType.WIFI_ONLY,
            4: ConnectionType.DATA_ONLY,
            6: ConnectionType.ALL_NETWORK_ON
        }
        return self.driver.set_network_connection(network_type[num])

if __name__ == '__main__':
    from AppAuto.common.MyDriver import my_driver
    NetworkType(my_driver()).set_network(6)
    print(NetworkType(my_driver()).get_network())
