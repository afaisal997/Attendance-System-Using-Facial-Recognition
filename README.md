# Face Recognition Based Attendance System

This project is a **Face Recognition Based Attendance System** built using **Python** and **PyQt5**. It uses computer vision techniques to detect and recognize faces via webcam and automatically records attendance into a CSV file.

---

## 🧠 Features

- 📸 Real-time face detection and recognition using OpenCV.
- 🧑‍💼 GUI built with PyQt5 for seamless user interaction.
- 🗂 Automatically logs attendance with name, time, and date into `Attendance.csv`.
- 📁 Supports multiple windows for input and output display.
- 📦 Resource management with `.qrc` and compiled `resource.py`.

---

## 📂 Project Structure

```plaintext
.
├── Attendance.csv           # Output file with attendance logs
├── mainwindow.py            # Main GUI window logic
├── out_window.py            # Secondary output window logic
├── mainwindow.ui            # UI layout for the main window (Qt Designer)
├── outputwindow.ui          # UI layout for the output window (Qt Designer)
├── resource.qrc             # Qt resource file (images, icons)
├── resource.py              # Compiled Python resource file
```

---

## 🚀 How to Run

### 1. Install Dependencies

Make sure Python is installed, then install the required packages:

```bash
pip install pyqt5 opencv-python
pip install opencv-python
pip install face-recognition
pip install numpy
pip install python-csv
pip install os-sys
```

### 2. Run the Application

```bash
python mainwindow.py
```

Ensure your webcam is connected and functional.

---

## 📝 How It Works

1. **GUI Initialization**: PyQt5 launches a user-friendly interface.
2. **Face Detection**: Webcam captures video frames; OpenCV detects faces.
3. **Face Recognition**: Matches are found against a trained model (assumed to be integrated).
4. **Attendance Logging**: Attendance is recorded in `Attendance.csv` with timestamp.
5. **Secondary Window**: Shows output/confirmation based on face detection.

---

## 🧰 Tools & Libraries Used

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- Qt Designer (for `.ui` files)

---

## 📌 Notes

- Modify UI using Qt Designer and regenerate the Python code with:

```bash
pyuic5 mainwindow.ui -o mainwindow.py
pyuic5 outputwindow.ui -o out_window.py
pyrcc5 resource.qrc -o resource.py
```

## 🙌 Acknowledgements

- OpenCV community and documentation
- PyQt and Qt Designer tools
