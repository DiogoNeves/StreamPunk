from pynput import keyboard
import datetime


def get_path(stream_name: str) -> str:
    return f"data/{stream_name}.txt"


def append_timestamp_to_file(file_path: str, event_name: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{event_name}: {timestamp}\n")


def start_stream(stream_name: str) -> None:
    file_path = get_path(stream_name)
    append_timestamp_to_file(file_path, "start")


def flag_moment(stream_name) -> None:
    file_path = get_path(stream_name)
    append_timestamp_to_file(file_path, "flag")


def listen(stream_name: str) -> None:
    def on_release(key: (keyboard.Key | keyboard.KeyCode | None)) -> None:
        try:
            if key.vk == 76:
                flag_moment(stream_name)
        except AttributeError:
            pass

    start_stream(stream_name)
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    print("Listening to StreamPunk device.")
    stream_name = "testing"
    listen(stream_name)
    print("Bye!")




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
