import math

# Factor de 16
#voltage_received = 3.3 # Funciona 1° Parte
#voltage_received = 3.3 # Tiene de atenuación 11DB
voltage_received = 1.25 # El nuevo micro
bin_to_vol = lambda value: value * (voltage_received/ 65535)
# Factor de 10
#bin_to_vol = lambda value: value * (3.3/ 2**10)

def cal_vol_to_decibeles(signalMax:float = 0, signalMin:float = 0):    
    peakToPeak = signalMax - signalMin
    volts = ((peakToPeak * voltage_received) / 1024) * 0.707
    first = math.log(((volts/0.00631) * 20), 10)
    second = first + 94 - 44 - 25
    return second

    
def cal_decibeles(signalIn:int=1, signalOut:int=1):
    #! signalIn => Señal que ingresa a la raspberry y sale del dispositivo
    #! signalOut => Señal que sale de la raspberry e ingresa al dispositivo
    #return (20 * math.log(signalOut/signalIn))
    if signalOut > 0 and signalIn > 0:
        divided = signalOut/signalIn
        return round((20 * math.log(divided)),2)
    else:
        return 0
    