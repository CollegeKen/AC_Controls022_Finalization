from kivy.uix.widget import Widget
from kivy.properties import OptionProperty, StringProperty, ListProperty, BooleanProperty

import slider2


class ValveIndicator(Widget):
    valve_closed = StringProperty('/home/ken/PycharmProjects/AC_Controls013_WorkingSerialInputs_NotWorkingOutputs'
                                  '/Pictures/red_circle.png')
    valve_open = StringProperty('/home/ken/PycharmProjects/AC_Controls013_WorkingSerialInputs_NotWorkingOutputs'
                                '/Pictures/green_circle.png')
    border = ListProperty([16, 16, 16, 16])

    valve_state = StringProperty()
    valve1_state = StringProperty()
    valve2_state = StringProperty()
    valve3_state = StringProperty()
    valve4_state = StringProperty()
    valve5_state = StringProperty()
