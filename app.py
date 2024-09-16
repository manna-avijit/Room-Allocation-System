from flask import Flask, render_template, request, send_file, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allocate_rooms(group_df, hostel_df):
    allocations = []

    
    for idx, row in group_df.iterrows():
        group_id = row['Group ID']
        members = row['Members']
        gender = row['Gender']

        
        boys, girls = 0, 0
        if "Boys" in gender and "Girls" in gender:
            boys = int(gender.split('&')[0].strip().split()[0])
            girls = int(gender.split('&')[1].strip().split()[0])
        elif "Boys" in gender:
            boys = members
        else:
            girls = members
        
        
        if boys > 0:
            for i in range(len(hostel_df)):
                if hostel_df.loc[i, 'Gender'] == 'Boys' and hostel_df.loc[i, 'Capacity'] >= boys:
                    allocations.append([group_id, hostel_df.loc[i, 'Hostel Name'], hostel_df.loc[i, 'Room Number'], boys])
                    hostel_df.loc[i, 'Capacity'] -= boys
                    break

        
        if girls > 0:
            for i in range(len(hostel_df)):
                if hostel_df.loc[i, 'Gender'] == 'Girls' and hostel_df.loc[i, 'Capacity'] >= girls:
                    allocations.append([group_id, hostel_df.loc[i, 'Hostel Name'], hostel_df.loc[i, 'Room Number'], girls])
                    hostel_df.loc[i, 'Capacity'] -= girls
                    break

    allocation_df = pd.DataFrame(allocations, columns=['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])
    return allocation_df


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    if 'group_csv' not in request.files or 'hostel_csv' not in request.files:
        return redirect(request.url)

    group_csv = request.files['group_csv']
    hostel_csv = request.files['hostel_csv']

    if group_csv and hostel_csv:
        
        group_path = os.path.join(app.config['UPLOAD_FOLDER'], 'group_info.csv')
        hostel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'hostel_info.csv')
        group_csv.save(group_path)
        hostel_csv.save(hostel_path)

        
        group_df = pd.read_csv(group_path)
        hostel_df = pd.read_csv(hostel_path)

        
        allocation_df = allocate_rooms(group_df, hostel_df)

        
        allocation_path = os.path.join(app.config['UPLOAD_FOLDER'], 'allocations.csv')
        allocation_df.to_csv(allocation_path, index=False)

        
        return render_template('upload.html', tables=[allocation_df.to_html(classes='data', header="true")],
                               download_link=url_for('download_allocations'))

    return redirect(request.url)

@app.route('/download')
def download_allocations():
    allocation_path = os.path.join(app.config['UPLOAD_FOLDER'], 'allocations.csv')
    return send_file(allocation_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)