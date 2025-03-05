# Parallelepiped Statistics Application - Deployment Guide

## Overview
This application processes data about parallelepipeds, calculates their geometric properties, and generates statistical reports in JSON format.

### Manual Setup Steps
1. Clone the repository
   ```bash
   git clone (https://github.com/AzizaMoldosheva/my_project/edit/main/README.md)
   cd my_project

   ```

2. Create the outputs directory
   ```bash
   mkdir outputs
   ```

3. Run the application
   ```bash
   python main.py
   ```

## Project Structure
```
parallelepiped_project/
├── main.py                 # Main script
├── parallelepipeds.json    # Input data with parallelepiped dimensions
├── utils/
│   ├── __init__.py         # Utils package initialization
│   ├── functions.py        # Mathematical functions
│   ├── statistics.py       # Statistical analysis
└── outputs/                # Output files directory
    ├── characteristics.json
    ├── statistics.json
```

## What the Application Does
- Reads parallelepiped dimensions from a JSON file
- Calculates properties like diagonal, volume, surface area, angles, and sphere parameters
- Computes averages across all parallelepipeds
- Outputs data to JSON files for further analysis

## Requirements
- Python 3.6+
- No external dependencies (uses only standard library)

## Output Files
- `characteristics.json`: Detailed data for each parallelepiped
- `statistics.json`: Statistical summary across all figures

## Customization
- Edit `parallelepipeds.json` to analyze different figures
- Modify calculations in `utils/functions.py`

## Troubleshooting
- Ensure the `outputs` directory exists before running
- Verify that your Python version is 3.6 or newer
- Check `parallelepipeds.json` for valid JSON syntax if errors occur


