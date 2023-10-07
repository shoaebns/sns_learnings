def compute_gas_volume(pressure, temperature, moles):
    gas_constant = 8.3144621  # J / (mol*K)
    volume = (moles * gas_constant * temperature) / pressure
    return volume
