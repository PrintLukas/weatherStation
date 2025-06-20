import smbus2
import bme280
import MySQLdb

## weather sensor
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
# print(data.id)
# print(data.timestamp)
# print(data.temperature)
# print(data.pressure)
# print(data.humidity)

bmpId = data.id
bmpTime = data.timestamp
bmpTemp = data.temperature
bmpPres = data.pressure
bmpHum = data.humidity

# there is a handy string representation too
# print(data)

## database access
user = 'weatherfrog'
pw = 'sunnyDay%%99'
db = 'climate'
try:
    connection = MySQLdb.connect(user=user, passwd=pw, db=db)
    c = connection.cursor()
    print("connected")
    # SQL-Query
    c.execute("""
        insert into BMP280
        (id, temperature, pressure, humidity)
        values(%s, %s, %s, %s)
        """, (bmpId, bmpTemp, bmpPres, bmpHum,))
    connection.commit()

    connection.close()
    print("closed")
except Exception as ex:
    print(ex)