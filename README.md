# Adaptive Brightness

A small Python project that uses your webcam to detect room brightness and automatically adjust your screen brightness.

## What It Does

This script captures a frame from your webcam, converts it to grayscale, calculates the average brightness of the room, and maps that value to a screen brightness percentage.

It also smooths the brightness changes so the screen does not jump suddenly from one brightness level to another.

## Features

- Detects room brightness using the webcam
- Converts camera brightness values into screen brightness percentages
- Smoothly adjusts screen brightness over time
- Prevents the screen brightness from going too low
- Cleans up the camera properly when the program stops

## Requirements

- Python 3
- A working webcam
- A system supported by `screen_brightness_control`

The Python packages are listed in `requirements.txt`.

## Installation

Clone the repository:

```bash
git clone https://github.com/jaimzh/adaptive-brightness.git
cd adaptive-brightness
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

The program will start reading brightness from your webcam and adjusting your screen brightness every few seconds.

To stop it, press:

```bash
Ctrl+C
```

## How It Works

1. The webcam captures a frame.
2. The frame is converted to grayscale.
3. The average brightness of the grayscale image is calculated.
4. The brightness value is mapped to a screen brightness percentage.
5. The screen brightness is adjusted gradually using a smoothing factor.

## Privacy Note

The webcam is only used to measure brightness from the current frame. The script does not save images or record video.

## Notes

This is a simple project made for learning Python automation, OpenCV, and system brightness control.

Some systems may require extra permissions for webcam access or brightness control.
