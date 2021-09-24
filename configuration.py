import configparser

import analogInputs

config = configparser.ConfigParser()


class ZeroConfigs:
    channel1_zero = 0
    channel2_zero = 0
    channel3_zero = 0
    channel4_zero = 0
    channel5_zero = 0


class SpanConfigs:
    channel1_span = 0
    channel2_span = 0
    channel3_span = 0
    channel4_span = 0
    channel5_span = 0


config['Zero_Config'] = {
    "Channel 1 Zero": str(ZeroConfigs.channel1_zero),
    "Channel 2 Zero": str(ZeroConfigs.channel2_zero),
    "Channel 3 Zero": str(ZeroConfigs.channel3_zero),
    "Channel 4 Zero": str(ZeroConfigs.channel4_zero),
    "Channel 5 Zero": str(ZeroConfigs.channel5_zero),
}

config['Span_Config'] = {
    "Channel 1 Span": str(SpanConfigs.channel1_span),
    "Channel 2 Span": str(SpanConfigs.channel2_span),
    "Channel 3 Span": str(SpanConfigs.channel3_span),
    "Channel 4 Span": str(SpanConfigs.channel4_span),
    "Channel 5 Span": str(SpanConfigs.channel5_span),
}


def WriteTheConfigFile():
    with open('analog_config.ini', 'w') as configfile:
        config['Zero_Config']['Channel 1 Zero'] = str(ZeroConfigs.channel1_zero)
        config['Zero_Config']['Channel 2 Zero'] = str(ZeroConfigs.channel2_zero)
        config['Zero_Config']['Channel 3 Zero'] = str(ZeroConfigs.channel3_zero)
        config['Zero_Config']['Channel 4 Zero'] = str(ZeroConfigs.channel4_zero)
        config['Zero_Config']['Channel 5 Zero'] = str(ZeroConfigs.channel5_zero)
        config['Span_Config']['Channel 1 Span'] = str(SpanConfigs.channel1_span)
        config['Span_Config']['Channel 2 Span'] = str(SpanConfigs.channel2_span)
        config['Span_Config']['Channel 3 Span'] = str(SpanConfigs.channel3_span)
        config['Span_Config']['Channel 4 Span'] = str(SpanConfigs.channel4_span)
        config['Span_Config']['Channel 5 Span'] = str(SpanConfigs.channel5_span)
        config.write(configfile)


def ReadTheConfigFile():
    config.read('analog_config.ini')
    ZeroConfigs.channel1_zero = int(config['Zero_Config']['Channel 1 Zero'])
    ZeroConfigs.channel2_zero = int(config['Zero_Config']['Channel 2 Zero'])
    ZeroConfigs.channel3_zero = int(config['Zero_Config']['Channel 3 Zero'])
    ZeroConfigs.channel4_zero = int(config['Zero_Config']['Channel 4 Zero'])
    ZeroConfigs.channel5_zero = int(config['Zero_Config']['Channel 5 Zero'])
    SpanConfigs.channel1_span = int(config['Span_Config']['Channel 1 Span'])
    SpanConfigs.channel2_span = int(config['Span_Config']['Channel 2 Span'])
    SpanConfigs.channel3_span = int(config['Span_Config']['Channel 3 Span'])
    SpanConfigs.channel4_span = int(config['Span_Config']['Channel 4 Span'])
    SpanConfigs.channel5_span = int(config['Span_Config']['Channel 5 Span'])
