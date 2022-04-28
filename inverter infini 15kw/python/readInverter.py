import serial
import json

Infini15KWDescriptionField = {
    "description": {
        "solar_panel": [

            {"input_voltage_1": "Solar input voltage 1", "multiply": 0.1},
            {"input_voltage_2": "Solar input voltage 2", "multiply": 0.1},
            {"input_current_1": "Solar input current 1", "multiply": 0.01},
            {"input_current_2": "Solar input current 2", "multiply": 0.01}
        ],
        "battery": [
            {"voltage": "Battery Voltage", "multiply": 0.1},
            {"battery_capacity": "Battery Capacity", "unit": "%"},
            {"battery_current": "Battery Current", "multiply": 0.1,
                "note": {"charge": "+", "discharge": "-"}}
        ],

        "ac_input": [
            {"ac_r_voltage": "AC R Phase", "multiply": 0.1},
            {"ac_s_voltage": "AC S Phase", "multiply": 0.1},
            {"ac_t_voltage": "AC T Phase", "multiply": 0.1},
            {"ac_frequency": "AC Frequency", "multiply": 0.01},
        ]
    }

}

inverterDescriptionSolarPanel = Infini15KWDescriptionField['description']['solar_panel']
inverterDescriptionBattery = Infini15KWDescriptionField['description']['battery']

# for solar_panel in inverterDescriptionSolarPanel:

# print(solar_panel)  # mendapatkan key dari list
# print(i[str(*i)])  # mendapatkan value dari list
# print(i[str(*i)])

# print(Infini15KWDescriptionField['description']['solar_panel'])


# for battery in inverterDescriptionBattery:

#     key = "note"

#     if key in battery:
#         print("ada")

# print(battery.has_key('note'))


class InverterInfini15KW:
    __sundaya_message = "Sundaya Hybrid System Infini Solar 15KW"
    _dataInverter = []
    # _jsonResult;
    # current = 0

    def __init__(self, dataInverter):
        print('ini adalah consturtor')
        self._dataInverter = dataInverter.split(',')

    def get_inverter_message(self):

        try:

            jsonResult = {
                "response": "success",
                "solar_input_1": {"voltage": self._dataInverter[0], "current": self._dataInverter[2]},
                "solar_input_2": {"voltage": self._dataInverter[1], "current": self._dataInverter[2]},
                "battery": {"voltage": self._dataInverter[4], "capcity": self._dataInverter[5], "current": self._dataInverter[6]},
                "ac_voltage": {"phase_r": self._dataInverter[7], "phase_s": self._dataInverter[8], "phase_t": self._dataInverter[9]},

            }
            return jsonResult
        except NameError:
            return {"response": "fail","error":NameError}


ser = serial.Serial('COM8', 2400, timeout=1)  # open serial port
print(ser.name)         # check which port was really used
ser.write('^P003GS\r'.encode())     # get inverter data
line = ser.readline()

result = str(line)

data = str(line.decode('unicode_escape').encode('utf-8'))
# remove header response dari inverter
data1 = data.replace("b'^D11", "").split('\\')[0]  # remove character aneh
ser.close()


# trial model

p = InverterInfini15KW(data1)

done = p.get_inverter_message()
print(done)

# trial model
