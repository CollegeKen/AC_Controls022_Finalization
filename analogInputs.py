import serial as sl
import ValveIndicator
import configuration
import outputs
import serialComms


class TestState:
    testState = True


def SerialComms():
    if TestState.testState is False:
        serialComms.SerialComms.SerialCommsCheck()
        serialComms.inputsFromArduino()
    if TestState.testState is True:
        pass


class PressureVariables:
    psv1 = 0
    psv2 = 0
    psv3 = 0
    psv4 = 0
    psv5 = 0


class AnalogZero:
    channel1_zero = 0
    channel2_zero = 0
    channel3_zero = 0
    channel4_zero = 0
    channel5_zero = 0


class AnalogSpan:
    channel1_span = 450
    channel2_span = 450
    channel3_span = 450
    channel4_span = 450
    channel5_span = 450


class ValveStates:

    # valve1_state = '0'

    def valve1_close(self):
        ValveIndicator.ValveIndicator.valve1_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            ValveStates.valve1_state = b'0'
            serialComms.SerialComms.ser.write(ValveStates.valve1_state)

    def valve1_open(self):
        ValveIndicator.ValveIndicator.valve1_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            ValveStates.valve1_state = b'1'
            serialComms.SerialComms.ser.write(ValveStates.valve1_state)

    def valve2_close(self):
        ValveIndicator.ValveIndicator.valve2_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'2')

    def valve2_open(self):
        ValveIndicator.ValveIndicator.valve2_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'3')

    def valve3_close(self):
        ValveIndicator.ValveIndicator.valve3_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'4')

    def valve3_open(self):
        ValveIndicator.ValveIndicator.valve3_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'5')

    def valve4_close(self):
        ValveIndicator.ValveIndicator.valve4_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'6')

    def valve4_open(self):
        ValveIndicator.ValveIndicator.valve4_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'7')

    def valve5_close(self):
        ValveIndicator.ValveIndicator.valve5_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'8')

    def valve5_open(self):
        ValveIndicator.ValveIndicator.valve5_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            pass
        if TestState.testState is False:
            serialComms.SerialComms.ser.write(b'y')


def DeclareAnalogInputs():
    if TestState.testState is True:
        PressureVariables.psv1 = 200
        PressureVariables.psv2 = 200
        PressureVariables.psv3 = 200
        PressureVariables.psv4 = 200
        PressureVariables.psv5 = 200

    if TestState.testState is False:
        serialComms.inputsFromArduino()


def ConvertRawInputToPSI():
    ch1_zero = int(AnalogZero.channel1_zero)
    ch2_zero = int(AnalogZero.channel2_zero)
    ch3_zero = int(AnalogZero.channel3_zero)
    ch4_zero = int(AnalogZero.channel4_zero)
    ch5_zero = int(AnalogZero.channel5_zero)
    ch1_span = int(AnalogSpan.channel1_span)
    ch2_span = int(AnalogSpan.channel2_span)
    ch3_span = int(AnalogSpan.channel3_span)
    ch4_span = int(AnalogSpan.channel4_span)
    ch5_span = int(AnalogSpan.channel5_span)
    PressureVariables.psv1 = int((int(PressureVariables.psv1) * (ch1_span - ch1_zero)) / 1024)
    PressureVariables.psv2 = int((int(PressureVariables.psv2) * (ch2_span - ch2_zero)) / 1024)
    PressureVariables.psv3 = int((int(PressureVariables.psv3) * (ch3_span - ch3_zero)) / 1024)
    PressureVariables.psv4 = int((int(PressureVariables.psv4) * (ch4_span - ch4_zero)) / 1024)
    PressureVariables.psv5 = int((int(PressureVariables.psv5) * (ch5_span - ch5_zero)) / 1024)
