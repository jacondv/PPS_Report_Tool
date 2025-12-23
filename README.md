# PPS_Report_Tool - Setup Guide

This document describes **step-by-step instructions** to set up the development environment for **PPS Report Tool** on Windows, including Python, virtual environment, required libraries, and GUI setup.

---

## **1. Prerequisites**

- Windows 10 or 11
- Python 3.10.11 (download from [python.org](https://www.python.org/downloads/release/python-31011/))
  - **Do not use Microsoft Store Python** (may cause compatibility issues)
  - During installation, check **“Add Python 3.10 to PATH”**
- CMD or PowerShell for running commands
- Optional: Qt Designer 6 (Standalone) for GUI design ([download link](https://www.pythonguis.com/installation/install-qt-designer-standalone/))

---

## **2. Project Folder Structure**

Example:

## 2. Project Folder Structure

Example:

```text
PPS_Report_Tool/src
│
├─ gui/                  # Qt Designer .ui files
├─ venv/                # Virtual environment (created later)
├─ data/                # Sample point cloud data
├─ reports/             # Exported PDF reports
└─ requirements.txt     # Python dependencies
...
```
---


## **3. Create Virtual Environment**

1. Open CMD or PowerShell
2. Navigate to project folder:

```cmd
cd C:\Projects\PPS_Report_Tool
venv\Scripts\activate.bat
```
or
```cmd
Powershell
venv\Scripts\Activate.ps1
```

## 4. Update pip
python -m pip install --upgrade pip


## 5. Install Required Packages
Create requirements.txt:

# Core libraries
numpy
pandas

# 3D / Point Cloud
open3d==0.17.0

# GUI
PySide6==6.6.2

# Report export (HTML → PDF)
weasyprint==59.0
jinja2==3.1.2
pydyf==0.9.0

```cmd
pip install -r requirements.txt
```
## Check install
```cmd
python -c "import numpy, pandas, open3d, PySide6, weasyprint, jinja2, pydyf, reportlab; print('All packages installed successfully')"
```
# Start qtdesigner
```cmd
pyside6-designer
```