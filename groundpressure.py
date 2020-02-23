#calculate the ground pressure tracked vehicles with bogies


#user input for contact area calculation
width_of_track = int(input("width of track: "))
unloaded_wheel_radius = int(input("radius of the unloaded wheel: "))
length_between_axles = int(input("length between axles: "))

#contact area calculation
contact_area = width_of_track*(1.25*unloaded_wheel_radius+length_between_axles)

#user input for nominal ground pressure calculation
wheel_load = int(input("wheel load in kN: "))
track_weight = int(input("weight of track kN: "))

#nominal ground pressure calculation
nomGroundPressure = (2*wheel_load+track_weight)/(contact_area)
term = "kN"

print(nomGroundPressure,  term)