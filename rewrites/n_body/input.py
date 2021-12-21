from lib import *

def algo(nIterations):
    solarSystem = newSystem()
    energy_states = []
    for i in range(0,nIterations):
        energy = report_energy(solarSystem)
        energy_states.append(energy)
        solarSystem.advance()
    return energy_states