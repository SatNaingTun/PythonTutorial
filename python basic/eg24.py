
weather_c={"Monday":12,"Tuesday":14,"Wednesday":15,"Thursday":14,"Friday":21,"Saturday":22,"Sunday":24}

def TempC2F(temp_c):
    temp_f=(temp_c*(9/5))+32
    return temp_f

# weather_F=weather_c
weather_F={k:TempC2F(v) for k,v in weather_c.items()}
print(weather_F)
