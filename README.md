# StreamPunk
> Hack 🏴‍☠️ - Turn my numpad into a StreamDeck

StreamPunk was created as part of a live coding session on Twitch.  
The goal was to build the beginnings of a simple clone of 
[Stream Deck](https://www.elgato.com/uk/en/s/welcome-to-stream-deck), 
using a spare NumPad keyboard I have and see how far I could get in 
a couple of hours.  
_I have no intention to maintain this project._  

[Stream Deck](https://www.elgato.com/uk/en/s/welcome-to-stream-deck)
is a customisable control panel for streamers and live content creators.  
You can assign certain functions and workflows to special keys.  

### Future
In the future I might attempt to finish this project using a mix of 
NumPad, Karabiner and Alfred or macOS Shortcuts.  

## 🎥 Streams
Follow me on [YouTube](https://www.youtube.com/@DiogoNeves?sub_confirmation=1) or [Twitch](https://www.twitch.tv/diogosnows).  
New content coming soon...  

[🔧🏴‍☠️ Making of StreamPunk in Python + Numpad keyboard](https://youtu.be/-537XI17UrU)  
[![Making of StreamPunk in Python + Numpad keyboard](https://github.com/DiogoNeves/mochi-flashback/assets/178898/45373020-5f00-4ef6-a40c-fe8435995ec2)](https://youtu.be/-537XI17UrU)
  

## 🛠️ Installation
> There are no promises made this would run and I have only tested on macOS (Macbook Air M1) with python 3.11.8
> I did not freeze the requirements either.

Create the virtual environment:  
```bash
# Recommended
$ python -m venv .venv
```

Install the dependencies:  
```bash
$ pip install pynput
```

## 🏃 Running
Connect a NumPad or other keyboard.  
```bash
$ python stream_punk.py
```
Press the Enter key on the NumPad (you may need to change the 
key codes in the source, depending on your keyboard).  
> Timestamps will show as a new file in the `data/` folder.  


## License
[LICENSE](./LICENSE)