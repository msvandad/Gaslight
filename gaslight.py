from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import math
from math import pi
table_columns = ["ID", "Gas", "Description", "Molecular mass (u)", "ISP (s)", "Density at 0 C° and 2.41e+7 Pa (g/cm^3)"]
table_column_kwargs = {"justify": "center", "vertical": "middle"}

gas_table = [["G-H2", "Hydrogen", "2.0", "272", "0.02"], 
    ["G-He", "Helium", "4.0", "165", "0.04"], 
    ["G-Ne", "Neon", "20.2", "75", "0.19"],
    ["G-Ar", "Argon", "39.9", "52", "0.44"],
    ["G-Kr", "Krypton", "83.8", "37", "1.08"],
    ["G-Xe", "Xenon", "131.3", "31", "1.89"],
    ["G-CO2", "Carbon Dioxide", "44.0", "61", "Liquid"],
    ["G-N2", "Nitrogen", "28.0", "73", "0.28"]]

gas_properties = {
    "G-H2": [4124, 1.41],
    "G-He": [2077, 1.66],
    "G-Ne": [411.9, 1.66],
    "G-Ar": [208.1, 1.67],
    "G-Kr": [125.0, 1.68],
    "G-Xe": [64.2, 1.66],
    "G-CO2": [188.9, 1.30],
    "G-N2": [296.8, 1.40] } # gas, specific gas constant J/kg·K, heat capacity ratio

class gaslight:
    def __init__(self):
        self.console = Console()
        self.table = Table(title="Thrust Gas")
        
        for column in table_columns:
            self.table.add_column(column, **table_column_kwargs)

        id = 0
        for row in gas_table:
            self.table.add_row(str(id), *row)
            id += 1

        self.console.print(self.table)
        self.selected_gas = Prompt.ask("Enter the Gas identifier you want to select (e.g., G-N2)")
    
    def calulate_nozzle_dimension(self, desired_thrust, chamber_pressure, chamber_temperature, environment_pressure):
        '''
        Calculates the nozzle dimensions for a given desired thrust, chamber pressure, chamber temperature, and environment pressure.
        
        Args:
            desired_thrust (float): The desired thrust of the nozzle in newtons.
            chamber_pressure (float): The chamber pressure in pascals.
            chamber_temperature (float): The chamber temperature in Kelvin.
            environment_pressure (float): The environment pressure in pascals.
        
        Returns:
            tuple: A tuple containing throat radius in meters and exit radius in meters.
        '''
        
        gas = gas_properties[self.selected_gas]
        R = gas[0]
        gamma = gas[1]

        t1 = 2 * gamma/(gamma - 1)
        t2 = R * chamber_temperature
        exp = (gamma - 1)/gamma
        t3 =  1 - ((environment_pressure/chamber_pressure)**exp)

        v_e = math.sqrt(t1 * t2 * t3)

        m_dot = desired_thrust/v_e

        t1 = m_dot * math.sqrt(chamber_temperature) / chamber_pressure
        t2 = math.sqrt(R) / gamma  
        exp = (gamma + 1) / (2 * gamma - 2)
        t3 = ((gamma + 1) / 2)**exp

        throat_area = t1 * t2 * t3
        throat_radius = math.sqrt(throat_area / pi)

        t2 = (1/(environment_pressure/chamber_pressure))**(1/gamma)
        t3 = (2/(gamma + 1))**(1/(gamma - 1))
        exit_area = throat_area * t2 * t3
        exit_radius = math.sqrt(exit_area / pi)

        nozzle_dimensions = (throat_radius, exit_radius)
    
        self.console.print(f"Throat radius: {nozzle_dimensions[0]} m")
        self.console.print(f"Exit radius: {nozzle_dimensions[1]} m")
        return nozzle_dimensions
    

if __name__ == "__main__":
    g = gaslight()

    prompt = Prompt.ask("Enter the desired thrust in newtons")
    desired_thrust = float(prompt)
    print("desired_thrust:", desired_thrust)

    prompt = Prompt.ask("Enter the chamber pressure in pascals")
    chamber_pressure = float(prompt)
    print("chamber_pressure:", chamber_pressure)

    prompt = Prompt.ask("Enter the chamber temperature in Kelvin")
    chamber_temperature = float(prompt)
    print("chamber_temperature:", chamber_temperature)

    prompt = Prompt.ask("Enter the environment pressure in pascals")
    environment_pressure = float(prompt)
    print("environment_pressure:", environment_pressure)

    nozzle_dimensions = g.calulate_nozzle_dimension(desired_thrust, chamber_pressure, chamber_temperature, environment_pressure)