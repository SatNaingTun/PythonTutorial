import spidev
from time import sleep

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 9600  # Set SPI speed to 9600 Hz

def read_adc(channel):
    # Check if the channel is valid
    if channel > 1 or channel < 0:
        return -1
    # Perform SPI transaction and store returned bits in 'r'
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    # Construct ADC value from returned bits
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out

while True:
    raw_value = read_adc(0)
    print(f"Raw ADC Value: {raw_value}")
    sleep(0.7)
