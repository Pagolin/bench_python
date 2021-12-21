from collections import namedtuple
from enum import Enum
from math import log, sqrt, exp
from scipy.stats import norm


class OptionType(Enum):
    PUT = "P"
    CALL = "C"


Option = namedtuple("Option",
                    ["spot", "strike", "risk_free_rate", "dividende_rate",
                     "volatility", "time", "ty", "dividende_false",
                     "ref_val"])


def d1(spot, strike, time, risk_free_rate, volatility):
    d = (log(spot / strike) + (risk_free_rate + volatility ** 2 / 2.) * time) \
        / (volatility * sqrt(time))
    return d


def d2(spot, strike, time, risk_free_rate, volatility):
    return d1(spot, strike, time, risk_free_rate, volatility) \
           - volatility * sqrt(time)


def calls_algo(spot, strike, time, risk_free_rate, volatility):
    d_1 = d1(spot, strike, time, risk_free_rate, volatility)
    d_2 = d_1 - volatility * sqrt(time)
    fprice = spot * norm.cdf(d_1) \
             - strike * exp(-risk_free_rate * time) * norm.cdf(d_2)
    return fprice


def puts_algo(spot, strike, time, risk_free_rate, volatility):
    fprice = strike * exp(-risk_free_rate * time) \
             + calls_algo(spot, strike, time, risk_free_rate, volatility)
    return fprice


def calulateForOption(option: Option):
    args = option.spot, option.strike, option.time, \
           option.risk_free_rate, option.volatility
    if option.ty == OptionType.PUT:
        return puts_algo(*args)
    else:
        return calls_algo(*args)

def refl(obj):
    return obj