import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

# URI of the Crazyflie to connect to
URI = 'radio://0/80/2M/E7E7E7E7E7'

# Takeoff altitude (in meters)
TAKEOFF_ALTITUDE = 0.5

# Initialize the Crazyflie library
cflib.crtp.init_drivers()

def takeoff(scf, target_height):
    print("Taking off...")
    scf.cf.commander.send_hover_setpoint(0, 0, 0, target_height)
    time.sleep(5)  # Wait for 5 seconds for the takeoff to complete

def main():
    with SyncCrazyflie(URI) as scf:
        # Takeoff to the desired altitude
        takeoff(scf, TAKEOFF_ALTITUDE)

        # Perform other tasks or movements here

        # Close the connection
        scf.cf.commander.send_stop_setpoint()
        time.sleep(1)

if __name__ == '__main__':
    main()