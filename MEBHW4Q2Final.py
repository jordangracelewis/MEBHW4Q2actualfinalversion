# Prompt the user to input a value for 'R_f'
y = float(input(f"Enter a value for R_f: "))

# Solve for 'x' using the equation R_f = 0.005x
x_fuel_flow_rate = y / 0.005

# Display the result
print(f"For R_f = {y}, Fuel Flow Rate = {x_fuel_flow_rate}")

# Prompt the user to input a value for 'R_T'
y = float(input(f"Enter a value for R_T: "))

# Solve for 'x' using the equation R_T = 1.3x - 18.5
x_temperature = (y + 18.5) / 1.3

# Display the result
print(f"For R_T = {y}, Fuel Temperature = {x_temperature}")

# Prompt the user to input a value for 'R_P'
y = float(input(f"Enter a value for R_P: "))

# Solve for 'x' using the equation R_P = 0.3x
x_pressure = y / 0.3

# Display the result
print(f"For R_P = {y}, Fuel Pressure = {x_pressure}")

# Solve for 'N1' using the equation PV = NRT
x_Molar_Flow_rate_1 = ((x_pressure *1000) * x_fuel_flow_rate)/ (8.314 * (x_temperature+ 273))

# Display the result
print(f" The molar flow rate of stream 1 in mol/h is = {x_Molar_Flow_rate_1}")

# Prompt the user to input a value for 'X_A'
A = float(input("Enter the mole fraction for methane: "))
# Solve for 'm' using the equation Oxygen needed by RXN A = X_A * 2
m = x_Molar_Flow_rate_1 * A * 2

# Prompt the user to input a value for 'X_B'
B = float(input("Enter the mole fraction for ethane: "))
# Solve for 'n' using the equation Oxygen needed by RXN B = X_B * (7/2)
n = x_Molar_Flow_rate_1 * B * (7/2)

# Prompt the user to input a value for 'X_C'
C = float(input("Enter the mole fraction for propane: "))
# Solve for 'p' using the equation Oxygen needed by RXN C = X_C * 5
p = x_Molar_Flow_rate_1 * C * 5

# Prompt the user to input a value for 'X_D'
D = float(input("Enter the mole fraction for n-butane: "))
# Solve for 'q' using the equation Oxygen needed by RXN D = X_D * (13/2)
q = x_Molar_Flow_rate_1 * D * (13/2)

# Prompt the user to input a value for 'X_E'
E = float(input("Enter the mole fraction for isobutane: "))
# Solve for 'r' using the equation Oxygen needed by RXN E = X_E * (13/2)
r = x_Molar_Flow_rate_1 * E * (13/2)

# Calculate the sum of m, n, p, q, and r
total_oxygen_needed = m + n + p + q + r

# Prompt the user to input a value for 'PX'
S = float(input(f"Enter a value for percent excess air wanted: "))
excess_air = S
total_air_needed = total_oxygen_needed * (1/ 0.21)
Molar_flow_rate_air_fed = (excess_air / 100) * total_air_needed + total_air_needed

# Prompt temp to ideal gas law
T = float(input(f"Enter the temperature of air at your location in Celsius: "))
temp_air = T
Volumetric_flow_rate_air = (Molar_flow_rate_air_fed * 8.314 * (temp_air + 273)) / (101325)

# Display the result
print(f" The volumetric flow rate of the air stream, in m^3/hr, coming in excess is = {Volumetric_flow_rate_air}")

x_ra = Volumetric_flow_rate_air * 0.00025
print(f"Therefore, R_a = {x_ra}")