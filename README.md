This is a simple python script that mirrors pedals (joysticks) so they can be seen by games using Wine.
(Else for some reason they do not show up on some games, like Star Citizen or Microsoft Flight Simulator!)

Run the script once to see all devices, then pass your device name as first argument, example:

    python3 spoof-device.py "ATMEL/VIRPIL/191105 VPC Rudder Pedals"

It will add "PRO" to the spoofed device's name, so you can identify it in game.
