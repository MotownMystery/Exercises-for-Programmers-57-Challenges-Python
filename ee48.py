from pyowm import OWM

def convert(temp):
    return (9/5)*temp + 32

API_key = 'eef14d3e088d888cfddff3351d98e2f0'
owm = OWM(API_key)

obs = owm.weather_at_place('Denver,US')
w = obs.get_weather()
data = w.get_temperature()
Temp = round(data['temp']-273,2)
print("The weather in Denver is: ",convert(Temp))