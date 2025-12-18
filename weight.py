

#name constant
Name = input("What is your name?: ")

earth_weight = float(input("How much do you weigh?: "))
#surface gravity factor 
Mercury_weight = 0.38 * earth_weight
Venus_weight = 0.91 * earth_weight
Moon_weight = 0.165 * earth_weight
Mars_weight = 0.38 * earth_weight
Jupiter_weight = 2.34 * earth_weight
Saturn_weight = 0.93 * earth_weight
Uranus_weight = 0.92 * earth_weight
Neptune_weight = 1.12 * earth_weight
Pluto_weight = 0.066 * earth_weight

#output 

print(f"{Name} here are your weights on our Solar system's planets")
# the earth weights multiply by the surface gravity
print(f" Weight on Mercury:      {Mercury_weight:,.2f}")
print(f" Weight on Venus:        {Venus_weight:,.2f}")
print(f" Weight on the Moon:     {Moon_weight:,.2f}")
print(f" Weight on Mars:         {Mars_weight:,.2f}")
print(f" Weight on Jupiter:      {Jupiter_weight:,.2f}")
print(f" Weight on Saturn:       {Saturn_weight:,.2f}")
print(f" Weight on Uranus:       {Uranus_weight:,.2f}")
print(f" Weight on Neptune:      {Neptune_weight:,.2f}")
print(f" Weight on Pluto:        {Pluto_weight:,.2f}")
