def celsius_to_farenheit(stopnie):
    return (stopnie * 1.8) + 32

def farenheit_to_celsius(stopnie):
    return (stopnie - 32) / 1.8

for x in range(-20, 40, 5):
    print('Temperatura {celcius}C to {farenheit}F'.format(celcius=x,
                                                          farenheit=celsius_to_farenheit(x)))
