# CustomQR
Personalized Python-based QR Code Generator

## Overview
A Python-based GUI application that generates and customizes QR codes. Built with `ttkbootstrap` for a modern interface, it allows users to input a URL, specify a custom fill color for the QR code, and save the generated image to their desired location.



## Features
- **Custom URL Input**: Generate QR codes for any URL.
- **Custom Fill Color**: Specify the QR code color (default is black).
- **Save Functionality**: Save the generated QR code as a PNG file.
- **Modern GUI**: Designed using `ttkbootstrap` with rounded corners and a sleek theme.



## Prerequisites
To run this project, ensure the following dependencies are installed:

- **Python 3.x** (recommended version 3.7+)
- Required Python libraries:
  - `ttkbootstrap`
  - `qrcode`
  - `Pillow`



## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aditixrawat/CustomQR.git
cd CustomQR
```

### 2. Install Dependencies
Install the required libraries using pip:

```bash
pip install ttkbootstrap qrcode pillow
```
## Usage
### Run the Application
1. Navigate to the folder where the code is located.
2. Run the Python script:
```bash
python qrcode_generator.py
```
## Steps to Use:
 1. Enter the URL for which you want to generate the QR code.
 2. Optionally, specify a Fill Color (e.g., red, blue, #123456). If left empty, the default color is black.
 3. Click Generate QR Code to display the QR code within the app.
 4. Use the Save QR Code button to save the generated image to your preferred location.


## File Structure
```bash
CustomQR/
│
├── qrcode_generator.py   # Main Python script
├── README.md             # Project documentation
└── requirements.txt      # Optional file for dependencies
```
## Additional Notes
 - **Fill Color Validation**: Ensure to use valid color names (e.g., red, blue) or hex codes (e.g., #123456). Invalid color input will show an error.
 - **Temporary QR Code**: A temporary file qrcode.png is created in the working directory before saving. This is deleted once the file is saved elsewhere.
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

