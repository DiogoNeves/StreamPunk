from pynput import keyboard

def on_press(key: (keyboard.Key | keyboard.KeyCode | None)) -> None:
    try:
        print("Struct: ", key.__dict__)
        if key.vk == 76:
            print(f'{key} pressed')
    except AttributeError:
        return

def on_release(key: (keyboard.Key | keyboard.KeyCode | None)) -> bool:
    print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    return True


if __name__ == "__main__":
    print("Listening to StreamPunk device.")
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print("Bye!")

    # listener = keyboard.Listener(
    #     on_press=on_press,
    #     on_release=on_release)
    # listener.start()






""" Notes

Suppressing doesn't work yet, likely because the app is untrusted.

key.vk = 76 => enter

``uinput_device_paths``
            A list of device paths.

            If this is specified, *pynput* will limit the number of devices
            checked for the capabilities needed to those passed, otherwise all
            system devices will be used. Passing this might be required if an
            incorrect device is chosen.

"""
