from lib import *

# def calculate(n, ref='sun'):
def main(n, ref='sun'):
    offset_momentum(BODIES[ref])
    report_energy()
    advance(0.01, n)
    report_energy()
