import analogInputs


class AutoBools:
    valve1_auto = True
    valve2_auto = True
    valve3_auto = True
    valve4_auto = True
    valve5_auto = True
    valveAll_auto = True


class ManBools:
    valve1_manual = False
    valve2_manual = False
    valve3_manual = False
    valve4_manual = False
    valve5_manual = False
    valveAll_manual = False


class OffBools:
    valve1_off = False
    valve2_off = False
    valve3_off = False
    valve4_off = False
    valve5_off = False
    valveAll_off = False


class Valve1_HOA:
    def Valve1_Auto(self):
        AutoBools.valve1_auto = True
        ManBools.valve1_manual = False
        OffBools.valve1_off = False

    def Valve1_Man(self):
        analogInputs.ValveStates.valve1_open(self)
        ManBools.valve1_manual = True
        AutoBools.valve1_auto = False
        OffBools.valve1_off = False
        AutoBools.valveAll_auto = False

    def Valve1_Off(self):
        analogInputs.ValveStates.valve1_close(self)
        OffBools.valve1_off = True
        AutoBools.valve1_auto = False
        ManBools.valve1_manual = False
        AutoBools.valveAll_auto = False


class Valve2_HOA:
    def Valve2_Auto(self):
        AutoBools.valve2_auto = True
        ManBools.valve2_manual = False
        OffBools.valve2_off = False

    def Valve2_Man(self):
        analogInputs.ValveStates.valve2_open(self)
        ManBools.valve2_manual = True
        AutoBools.valve2_auto = False
        OffBools.valve2_off = False
        AutoBools.valveAll_auto = False

    def Valve2_Off(self):
        analogInputs.ValveStates.valve2_close(self)
        OffBools.valve2_off = True
        AutoBools.valve2_auto = False
        ManBools.valve2_manual = False
        AutoBools.valveAll_auto = False


class Valve3_HOA:
    def Valve3_Auto(self):
        AutoBools.valve3_auto = True
        ManBools.valve3_manual = False
        OffBools.valve3_off = False

    def Valve3_Man(self):
        analogInputs.ValveStates.valve3_open(self)
        ManBools.valve3_manual = True
        AutoBools.valve3_auto = False
        OffBools.valve3_off = False
        AutoBools.valveAll_auto = False

    def Valve3_Off(self):
        analogInputs.ValveStates.valve3_close(self)
        OffBools.valve3_off = True
        AutoBools.valve3_auto = False
        ManBools.valve3_manual = False
        AutoBools.valveAll_auto = False


class Valve4_HOA:
    def Valve4_Auto(self):
        AutoBools.valve4_auto = True
        ManBools.valve4_manual = False
        OffBools.valve4_off = False

    def Valve4_Man(self):
        analogInputs.ValveStates.valve4_open(self)
        ManBools.valve4_manual = True
        AutoBools.valve4_auto = False
        OffBools.valve4_off = False
        AutoBools.valveAll_auto = False

    def Valve4_Off(self):
        analogInputs.ValveStates.valve4_close(self)
        OffBools.valve4_off = True
        AutoBools.valve4_auto = False
        ManBools.valve4_manual = False
        AutoBools.valveAll_auto = False


class Valve5_HOA:
    def Valve5_Auto(self):
        AutoBools.valve5_auto = True
        ManBools.valve5_manual = False
        OffBools.valve5_off = False

    def Valve5_Man(self):
        analogInputs.ValveStates.valve5_open(self)
        ManBools.valve5_manual = True
        AutoBools.valve5_auto = False
        OffBools.valve5_off = False
        AutoBools.valveAll_auto = False

    def Valve5_Off(self):
        analogInputs.ValveStates.valve5_close(self)
        OffBools.valve5_off = True
        AutoBools.valve5_auto = False
        ManBools.valve5_manual = False
        AutoBools.valveAll_auto = False


class Valve_All_Auto_Check:
    def checkAllAuto(self):
        print("hello")
        if AutoBools.valve1_auto and AutoBools.valve2_auto and AutoBools.valve3_auto and AutoBools.valve4_auto and \
                AutoBools.valve5_auto and AutoBools.valve6_auto:
            AutoBools.valveAll_auto = True
