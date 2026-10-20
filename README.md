# MouseClick

MouseClick plays a `.wav` sound every time a mouse button is pressed. The application runs in the background and does not open a visible window.

## Requirements

- Windows
- Python 3.8 or newer
- `pynput`

Install the dependency with:

```bash
pip install pynput
```

## Add your sound file

1. Put your audio file in the **same folder as `mouseclick.py`**.
2. Rename it to exactly `salahor.wav`.
3. Run the application:

```bash
python mouseclick.py
```

If you use the packaged executable built with the command below, `salahor.wav` is included automatically.

The audio file must be in WAV format because the application uses Windows `winsound`. To use a different filename, update this line in `mouseclick.py`:

```python
SOUND_FILE = resource_path("salahor.wav")
```

## Stop the application

Press **Ctrl+Shift+L+A**. At startup, the application prints the complete path where it expects the audio file.

## Build an executable (optional)

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable and include the WAV file:

```bash
pyinstaller --onefile --add-data "salahor.wav;." mouseclick.py
```

The executable will be created in the `dist` folder and will contain `salahor.wav`.

## Notes

- The application listens for mouse clicks globally while it is running.
- Windows may ask for permission for the Python or executable process.
- Only WAV files supported by Windows `winsound` can be played.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
