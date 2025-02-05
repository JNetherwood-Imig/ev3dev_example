from pybricks.iodevices import I2CDevice

class LaserSensor:
    def __init__(self, port):
        self.i2c = I2CDevice(port, 0x02 >> 1)

    def get_distance(self):
        results = self.i2c.read(0x42, 2)
        return results[0] + (results[1] << 8)
