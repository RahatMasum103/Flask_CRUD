#............IMPORTANT..........#

# 1. Create a folder in the project directory 'uploads' to store the files
# 2. Run the program as localhost:5000/file
# 3. Uploaded file will take to automated new url for viewing

#......................................#

import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#from werkzeug import secure_filename


#-------- This is for the upload storage----------- #
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'py', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- --- This checks correct file or not ------------- #
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/file')
def file_home():
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            # ---------- This is the file object -------------- #
            file = request.files['file']

            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file', filename=filename))  # This reads the file and shows in the browser #
            else:
                print("Not an uploadable file")

        except Exception as e:
            print("Couldn't upload file")
            print(e)
            return redirect('/file')

    return redirect('/file')


@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename) # takes the file from storage and shows its content


if __name__ == '__main__':
    app.run(debug=True)