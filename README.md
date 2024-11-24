# Next Gen Surveillance 

## Overview
Next Gen Surveillance is a smart surveillance system designed to enhance security. The system integrates advanced GPS tracking technology, allowing real-time monitoring and tracking of culprits. It provides a solution for tracking suspects using their unique identifiers, enabling law enforcement to respond quickly to incidents.

### Features
- **Real-time tracking**: Track culprits' locations instantly after activation.
- **Interactive map**: Displays the location of tracked suspects on an interactive map.
- **Backend API**: Simple REST API for integration with other systems to manage and retrieve tracking data.
- **Modular architecture**: Easily extendable and adaptable to various surveillance needs.

### Project Setup
To run this project locally:

### Method 1 

1. **Clone the repository or download zip file**
   ```bash
   git clone https://github.com/sahalhes/Next-Gen-Surveillance.git

2. **Run the following command in terminal**
    ```bash
    scripts/setup.bat

### Method 2

1. **Clone the repository: or download zip file**
   ```bash
   git clone https://github.com/sahalhes/Next-Gen-Surveillance.git

2. **Install dependencies: Navigate to the backend directory and install required Python dependencies:**

   ```bash
    pip install -r backend/requirements.txt

3. **Run the Flask backend app: In the backend directory, run the Flask application:**

    ```bash
    python backend/app.py

4. **View the frontend :**

    The frontend can be viewed by simply opening frontend/templates/tracker.html in a web browser. It shows a map that tracks suspects based on mock data.

### Project Structure
- **backend/**: Contains Flask API and tracking logic.
- **gps_tracker/**: The module responsible for simulating the GPS tracking process.
- **frontend/**: Contains HTML, CSS, and JavaScript for the interactive map interface.
- **tests/**: Unit tests for API and tracking functions.
- **docs/**: Documentation including flowcharts and diagrams.

### Future Enhancements
- **Machine learning integration**: Add predictive algorithms for detecting potential threats.
- **Higher precision tracking**: Use advanced GPS sensors for more accurate real-time tracking.
- **Mobile App**: Develop a mobile app for real-time tracking and alerts.
- **Improved authentication and authorization**: Add security features to protect data and access.

### Contributors
E S SAHAL HUSSAIN (@sahalhes)

### License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).