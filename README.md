# Automated Product Registration Script

## Overview
This project automates the process of logging into a website and registering products using the PyAutoGUI library. The script interacts with a browser and utilizes a CSV file containing product information to fill out and submit a registration form.

---

## Features
- **Automated Browser Launch:** Opens Google Chrome and navigates to a specified URL.
- **Login Automation:** Inputs credentials to log into the website.
- **Product Registration:** Reads product data from a CSV file and populates form fields on the website.
- **Customizable Timing:** Includes pauses between actions to ensure compatibility with various system speeds.

---

## Prerequisites
1. **Python 3.7+**
2. **Required Libraries:**
   - `pyautogui`
   - `pandas`
3. **Chrome Browser Installed**
4. **CSV File Format:**
   The script expects a `products.csv` file with the following headers:
   - `id`
   - `brand`
   - `type`
   - `category`
   - `unit_price`
   - `cost`
   - `obs` (optional notes)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Create a `requirements.txt` with `pyautogui` and `pandas` if not already available.)*

3. Place your `products.csv` file in the root directory of the project.

---

## Usage
1. Run the script:
   ```bash
   python main.py
   ```

2. Observe the automation process as the script:
   - Opens Chrome
   - Logs into the website
   - Reads product details from `products.csv`
   - Registers each product on the website

3. Make sure to keep the browser in focus during execution.

---

## Configuration
### Adjusting Pauses
The script uses `pyautogui.PAUSE` to control the delay between actions. Modify these values as needed:
```python
pyautogui.PAUSE = 0.5  # Adjust global delay
```

### Customizing Login Credentials
Update the `pyautogui.write` commands with your login email and password:
```python
pyautogui.write("your-email@example.com")
pyautogui.write("your-password")
```

---

## Limitations
- **Resolution Dependence:** The script relies on specific screen resolutions and UI element positions.
- **Browser Focus:** The script requires the browser to remain in focus during execution.
- **Static URLs:** The URL and UI elements must remain consistent for the script to function correctly.

---

## Troubleshooting
1. **Elements Not Found:**
   - Ensure the screen resolution and UI layout match the script's expectations.
2. **Login Failures:**
   - Verify credentials and adjust delays if the login form is slow to load.
3. **CSV Errors:**
   - Check the format and ensure all required columns are present.

---

## Contributing
Feel free to submit issues or pull requests for improvements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

