total_time = 75 #ms
one_way_distance = 2500.0 #km
optic_speed = 200000 #per second
ms_per_second = 1000

#calcs

time_on_wires = 2*one_way_distance / optic_speed * ms_per_second
print time_on_wires
time_at_routers = total_time - time_on_wires
print time_at_routers
