import analogInputs
import serial as sl


class SerialComms:
    def SerialCommsCheck(self):
        if ArduinoIsReadyBool.arduinoIsReady:
            ser = sl.Serial('/dev/ttyACM0', 9600)


class ArduinoIsReadyBool:
    arduinoIsReady = True


def waitingForArduino():
    cookedserial = SerialComms.ser.readline().decode('utf-8').strip('\r\n')
    print(cookedserial)
    if cookedserial == '<Arduino is Ready>':
        ArduinoIsReadyBool.arduinoIsReady = True
        print(ArduinoIsReadyBool.arduinoIsReady)


def inputsFromArduino():
    cookedserial = SerialComms.ser.readline().decode('utf-8').strip('\r\n')
    datasplit = cookedserial.split(',')
    analogInputs.PressureVariables.psv1 = datasplit[0].strip('<')
    analogInputs.PressureVariables.psv2 = datasplit[1]
    analogInputs.PressureVariables.psv3 = datasplit[2]
    analogInputs.PressureVariables.psv4 = datasplit[3]
    analogInputs.PressureVariables.psv5 = datasplit[4].strip('>')
