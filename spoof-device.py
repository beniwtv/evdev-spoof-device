import evdev
import sys
from evdev import ecodes, AbsInfo

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

if not devices:
    print('No evdev devices found on your system.',
          'Check your evdev installation and device permissions.')
    sys.exit(1)

print("Available devices:")
for device in devices:
    print(device.path, device.name)


if len(sys.argv) == 1: 
    sys.exit(1)

for device in devices:
    if device.name == sys.argv[1]:
        break

print("Using:", device.name)

caps = {
    ecodes.EV_MSC : [ecodes.MSC_SCAN],
    ecodes.EV_KEY : [ecodes.BTN_JOYSTICK, ecodes.BTN_TRIGGER],
    ecodes.EV_ABS : device.capabilities()[3]
}

spoofdevice = evdev.uinput.UInput(events=caps,
                                 name=device.name + " PRO",
                                 vendor=device.info.vendor, 
                                 product=device.info.product,
                                 version=device.info.version)
                                 
print("Spoofing:", spoofdevice)
print("Mirroring events...")

for event in device.read_loop():
    #print(event)
    spoofdevice.write_event(event)
    spoofdevice.syn()
