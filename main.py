#!/usr/bin/env python3

"""This version works on the RaspPi to serially communicate with the Arduino.
   The manual controls work to activate the relays on the relay board.
   The relay works opposite of the Arduino signal, meaning that a "HIGH" signal
   from the Arduino turns OFF the relay, and vice verso for the the "LOW" signal.
   This version needs work on the conversion of raw data from the Arduino analog signals,
   and a reduction in time for updates to the HMI.
   Also need to clean up the HMI graphics to get rid of the 6th valve."""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from time import sleep
import serial as sl

import configuration
import outputs
import slider2
import ValveIndicator
import analogInputs


# The widget looks for the kv file of the same name, so if you call your app PlotterApp, make sure the kv file is named
# plotter


class PressureValues:
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0


class SettingsWindow(Widget):
    def __init__(self, **kwargs):
        super(SettingsWindow, self).__init__(**kwargs)


class MainView(Widget):
    scale = ListProperty([100, 100])

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.slider.bind(value1=self.on_slider_changed, value2=self.on_slider_changed)

    def on_slider_changed(self, obj, value):
        self.scale[0] = self.slider.value1
        self.scale[1] = self.slider.value2


class SettingsWindow(Screen):
    pass


class OutputsWindow(Screen):
    pass


class MainView(Screen):
    pass


class SliderApp(App):
    # Variables for analog inputs. Must use Properties for kv file to update variables
    psv1 = NumericProperty(0)
    psv2 = NumericProperty(0)
    psv3 = NumericProperty(0)
    psv4 = NumericProperty(0)
    psv5 = NumericProperty(0)

    vlv1_state = StringProperty()
    vlv2_state = StringProperty()
    vlv3_state = StringProperty()
    vlv4_state = StringProperty()
    vlv5_state = StringProperty()
    vlv6_state = StringProperty()

    configuration.ReadTheConfigFile()

    channel1_zero = configuration.ZeroConfigs.channel1_zero
    channel2_zero = configuration.ZeroConfigs.channel2_zero
    channel3_zero = configuration.ZeroConfigs.channel3_zero
    channel4_zero = configuration.ZeroConfigs.channel4_zero
    channel5_zero = configuration.ZeroConfigs.channel5_zero

    channel1_span = configuration.SpanConfigs.channel1_span
    channel2_span = configuration.SpanConfigs.channel2_span
    channel3_span = configuration.SpanConfigs.channel3_span
    channel4_span = configuration.SpanConfigs.channel4_span
    channel5_span = configuration.SpanConfigs.channel5_span

    def build(self):
        Clock.schedule_interval(self.update_psv, 0.75)

        sm = ScreenManager()
        sm.add_widget(MainView(name='Main'))
        sm.add_widget(SettingsWindow(name='Settings'))
        sm.add_widget(OutputsWindow(name="Outputs"))

        configuration.ReadTheConfigFile()

        channel1_zero = configuration.ZeroConfigs.channel1_zero
        channel2_zero = configuration.ZeroConfigs.channel2_zero
        channel3_zero = configuration.ZeroConfigs.channel3_zero
        channel4_zero = configuration.ZeroConfigs.channel4_zero
        channel5_zero = configuration.ZeroConfigs.channel5_zero

        channel1_span = configuration.SpanConfigs.channel1_span
        channel2_span = configuration.SpanConfigs.channel2_span
        channel3_span = configuration.SpanConfigs.channel3_span
        channel4_span = configuration.SpanConfigs.channel4_span
        channel5_span = configuration.SpanConfigs.channel5_span

        analogInputs.AnalogZero.channel1_zero = int(configuration.ZeroConfigs.channel1_zero)
        analogInputs.AnalogZero.channel2_zero = int(configuration.ZeroConfigs.channel2_zero)
        analogInputs.AnalogZero.channel3_zero = int(configuration.ZeroConfigs.channel3_zero)
        analogInputs.AnalogZero.channel4_zero = int(configuration.ZeroConfigs.channel4_zero)
        analogInputs.AnalogZero.channel5_zero = int(configuration.ZeroConfigs.channel5_zero)
        analogInputs.AnalogSpan.channel1_span = int(configuration.SpanConfigs.channel1_span)
        analogInputs.AnalogSpan.channel2_span = int(configuration.SpanConfigs.channel2_span)
        analogInputs.AnalogSpan.channel3_span = int(configuration.SpanConfigs.channel3_span)
        analogInputs.AnalogSpan.channel4_span = int(configuration.SpanConfigs.channel4_span)
        analogInputs.AnalogSpan.channel5_span = int(configuration.SpanConfigs.channel5_span)

        return sm

    def process(self):
        channel1_zero = int(self.root.get_screen('Settings').ids.channel1_zero.text)
        channel2_zero = int(self.root.get_screen('Settings').ids.channel2_zero.text)
        channel3_zero = int(self.root.get_screen('Settings').ids.channel3_zero.text)
        channel4_zero = int(self.root.get_screen('Settings').ids.channel4_zero.text)
        channel5_zero = int(self.root.get_screen('Settings').ids.channel5_zero.text)
        channel1_span = int(self.root.get_screen('Settings').ids.channel1_span.text)
        channel2_span = int(self.root.get_screen('Settings').ids.channel2_span.text)
        channel3_span = int(self.root.get_screen('Settings').ids.channel3_span.text)
        channel4_span = int(self.root.get_screen('Settings').ids.channel4_span.text)
        channel5_span = int(self.root.get_screen('Settings').ids.channel5_span.text)

        configuration.ZeroConfigs.channel1_zero = channel1_zero
        configuration.ZeroConfigs.channel2_zero = channel2_zero
        configuration.ZeroConfigs.channel3_zero = channel3_zero
        configuration.ZeroConfigs.channel4_zero = channel4_zero
        configuration.ZeroConfigs.channel5_zero = channel5_zero
        configuration.SpanConfigs.channel1_span = channel1_span
        configuration.SpanConfigs.channel2_span = channel2_span
        configuration.SpanConfigs.channel3_span = channel3_span
        configuration.SpanConfigs.channel4_span = channel4_span
        configuration.SpanConfigs.channel5_span = channel5_span

        analogInputs.AnalogZero.channel1_zero = int(configuration.ZeroConfigs.channel1_zero)
        analogInputs.AnalogZero.channel2_zero = int(configuration.ZeroConfigs.channel2_zero)
        analogInputs.AnalogZero.channel3_zero = int(configuration.ZeroConfigs.channel3_zero)
        analogInputs.AnalogZero.channel4_zero = int(configuration.ZeroConfigs.channel4_zero)
        analogInputs.AnalogZero.channel5_zero = int(configuration.ZeroConfigs.channel5_zero)
        analogInputs.AnalogSpan.channel1_span = int(configuration.SpanConfigs.channel1_span)
        analogInputs.AnalogSpan.channel2_span = int(configuration.SpanConfigs.channel2_span)
        analogInputs.AnalogSpan.channel3_span = int(configuration.SpanConfigs.channel3_span)
        analogInputs.AnalogSpan.channel4_span = int(configuration.SpanConfigs.channel4_span)
        analogInputs.AnalogSpan.channel5_span = int(configuration.SpanConfigs.channel5_span)

        configuration.WriteTheConfigFile()
        configuration.ReadTheConfigFile()

        print(analogInputs.AnalogZero.channel1_zero, ' ', analogInputs.AnalogSpan.channel1_span)
        print(channel1_span, configuration.SpanConfigs.channel1_span)

    def Valve1_Auto(self, *kwargs):
        outputs.Valve1_HOA.Valve1_Auto(self)

    def Valve1_Man(self, *kwargs):
        outputs.Valve1_HOA.Valve1_Man(self)

    def Valve1_Off(self, *kwargs):
        outputs.Valve1_HOA.Valve1_Off(self)

    def Valve2_Auto(self, *kwargs):
        outputs.Valve2_HOA.Valve2_Auto(self)

    def Valve2_Man(self, *kwargs):
        outputs.Valve2_HOA.Valve2_Man(self)

    def Valve2_Off(self, *kwargs):
        outputs.Valve2_HOA.Valve2_Off(self)

    def Valve3_Auto(self, *kwargs):
        outputs.Valve3_HOA.Valve3_Auto(self)

    def Valve3_Man(self, *kwargs):
        outputs.Valve3_HOA.Valve3_Man(self)

    def Valve3_Off(self, *kwargs):
        outputs.Valve3_HOA.Valve3_Off(self)

    def Valve4_Auto(self, *kwargs):
        outputs.Valve4_HOA.Valve4_Auto(self)

    def Valve4_Man(self, *kwargs):
        outputs.Valve4_HOA.Valve4_Man(self)

    def Valve4_Off(self, *kwargs):
        outputs.Valve4_HOA.Valve4_Off(self)

    def Valve5_Auto(self, *kwargs):
        outputs.Valve5_HOA.Valve5_Auto(self)

    def Valve5_Man(self, *kwargs):
        outputs.Valve5_HOA.Valve5_Man(self)

    def Valve5_Off(self, *kwargs):
        outputs.Valve5_HOA.Valve5_Off(self)

    def Valve_All_Auto(self, *kwargs):
        outputs.Valve_All_Auto_Check.checkAllAuto(self)

    def update_psv(self, *kwargs):
        analogInputs.DeclareAnalogInputs()
        analogInputs.ConvertRawInputToPSI()

        self.psv1 = analogInputs.PressureVariables.psv1
        self.psv2 = analogInputs.PressureVariables.psv2
        self.psv3 = analogInputs.PressureVariables.psv3
        self.psv4 = analogInputs.PressureVariables.psv4
        self.psv5 = analogInputs.PressureVariables.psv5

        self.slider1_lower = int(self.root.get_screen('Main').ids.slider1.value1)
        self.slider1_upper = int(self.root.get_screen('Main').ids.slider1.value2)
        self.slider2_lower = int(self.root.get_screen('Main').ids.slider2.value1)
        self.slider2_upper = int(self.root.get_screen('Main').ids.slider2.value2)
        self.slider3_lower = int(self.root.get_screen('Main').ids.slider3.value1)
        self.slider3_upper = int(self.root.get_screen('Main').ids.slider3.value2)
        self.slider4_lower = int(self.root.get_screen('Main').ids.slider4.value1)
        self.slider4_upper = int(self.root.get_screen('Main').ids.slider4.value2)
        self.slider5_lower = int(self.root.get_screen('Main').ids.slider5.value1)
        self.slider5_upper = int(self.root.get_screen('Main').ids.slider5.value2)

        self.vlv1_state = self.root.get_screen('Main').ids.valve1.valve1_state
        self.vlv2_state = self.root.get_screen('Main').ids.valve2.valve2_state
        self.vlv3_state = self.root.get_screen('Main').ids.valve3.valve3_state
        self.vlv4_state = self.root.get_screen('Main').ids.valve4.valve4_state
        self.vlv5_state = self.root.get_screen('Main').ids.valve5.valve5_state

        if self.psv1 < self.slider1_upper:
            analogInputs.ValveStates.valve1_open(self)
        if self.psv1 > self.slider1_upper:
            analogInputs.ValveStates.valve1_close(self)

        if self.psv2 < self.slider2_upper:
            analogInputs.ValveStates.valve2_open(self)
        if self.psv2 > self.slider2_lower:
            analogInputs.ValveStates.valve2_close(self)

        if self.psv3 < self.slider3_upper:
            analogInputs.ValveStates.valve3_open(self)
        if self.psv3 > self.slider3_lower:
            analogInputs.ValveStates.valve3_close(self)

        if self.psv4 < self.slider4_upper:
            analogInputs.ValveStates.valve4_open(self)
        if self.psv4 > self.slider4_lower:
            analogInputs.ValveStates.valve4_close(self)

        if self.psv5 < self.slider5_upper:
            analogInputs.ValveStates.valve5_open(self)
        if self.psv5 > self.slider5_lower:
            analogInputs.ValveStates.valve5_close(self)



if __name__ == '__main__':
    SliderApp().run()
    sl.Serial.close
