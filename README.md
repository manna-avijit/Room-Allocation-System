# Room Allocation System

This is a Flask-based web application designed to streamline and digitalize the process of allocating hostel rooms for group accommodations. The app ensures that groups are allocated rooms based on size, gender, and room capacity, ensuring efficient room assignments in hostels with gender-specific accommodations.

## Features

- Upload CSV files for **Group Information** and **Hostel Information**.
- Automatically allocates rooms based on group size, gender, and room capacity.
- Keeps group members with the same group ID together as much as possible.
- Boys and girls are allocated to their respective hostels.
- Downloadable CSV file with final room allocation details.
- Easy-to-use web interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hostel-room-allocation.git
   cd hostel-room-allocation
2. Create and activate a virtual environment (optional but recommended):
   
      ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required Python packages:
   
      ```bash
   pip install -r requirements.txt

4. Run the Flask app:

   ```bash
   python app.py

## Usage

1. **Upload CSV Files**:
   - **Group Information CSV**: Contains group ID, number of members, and gender details (e.g., "Boys", "Girls", "5 Boys & 3 Girls").
   - **Hostel Information CSV**: Contains hostel name, room number, room capacity, and gender restrictions for each room.

2. **Room Allocation**:
   - Once the CSV files are uploaded, the app processes and allocates rooms, ensuring that:
     - Group members with the same ID stay together as much as possible.
     - Boys and girls are placed in their respective hostels.
     - Room capacity limits are not exceeded.

3. **Download Results**:
   - After processing, the app displays the allocation results on the webpage and provides an option to download the final room assignments as a CSV file.

## File Structure

    
    project_directory/
    │
    ├── app.py                # Main Flask application
    ├── templates/            # HTML templates for web pages
    │   └── upload.html       # Upload form and results page
    ├── static/               # Static files (CSS, images, etc.)
    │   └── style.css         # Optional custom styling
    ├── uploads/              # Folder to store uploaded CSVs and results
    ├── requirements.txt      # Required Python packages
    └── README.md             # Project documentation

## Example Input

### Group Information CSV (`group_info.csv`)

    
    Group ID,Members,Gender
    101,3,Boys
    102,4,Girls
    103,2,Boys
    104,5,Girls
    105,8,5 Boys & 3 Girls

## Hostel Information CSV (hostel_info.csv)

    
    Hostel Name,Room Number,Capacity,Gender
    Boys Hostel A,101,3,Boys
    Boys Hostel A,102,4,Boys
    Girls Hostel B,201,2,Girls
    Girls Hostel B,202,5,Girls

## Example Output

### Allocated Rooms CSV (allocations.csv)

    
    Group ID,Hostel Name,Room Number,Members Allocated
    101,Boys Hostel A,101,3
    102,Girls Hostel B,202,4
    103,Boys Hostel A,102,2
    104,Girls Hostel B,201,5
    105,Boys Hostel A,102,5

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
