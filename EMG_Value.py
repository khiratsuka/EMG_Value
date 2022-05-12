#EMG Click
#読み取るデータはCH1のみでOK
#20220512test


import spidev
import time
import sys
import os

#SPI通信準備
spi = spidev.SpiDev()
bus = 1
device = 2
spi.open(bus, device)
spi.max_speed_hz = 1000000

num = 0
filename = "data/20211223_{number}.csv".format(number=num)
while True:
    filename = "data/20211223_{number}.csv".format(number=num)
    if not os.path.exists(filename):
        break
    num += 1


f = open(filename,'x')
csv_data = []
while True:
    try:
        raw_data = spi.xfer2([0x06, 0x00, 0x00])
        adc_data = ((raw_data[1] & 0x0F) << 8) | raw_data[2]
        csv_data.append(str(2.048*adc_data/4096) + '\n')
        print(2.048*adc_data/4096)
        #time.sleep(1)

    except KeyboardInterrupt:
        spi.close()
        f.writelines(csv_data)
        f.close()
        sys.exit()
