#!/usr/bin/env python3
import boto3
import cv2
from flask import Flask, render_template, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'static/uploads/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':

        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('index.html', msg='No file selected')
        
        file = request.files['file']

        # if no file is selected
        if file.filename == '':
            return render_template('index.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(UPLOAD_FOLDER + file.filename)

            imageBytes = transformToBytes(UPLOAD_FOLDER + file.filename)
            extracted_text = detect_text(imageBytes)

            # extract the text and display it
            return render_template('index.html',
                                    msg='Successfully processed',
                                    extracted_text=extracted_text,
                                    img_src=UPLOAD_FOLDER + file.filename)

        if file and not allowed_file(file.filename):
            return render_template('index.html', msg='File extension not supported')

        return render_template('index.html', msg='Error')

    elif request.method == 'GET':
        return render_template('index.html')


def transformToBytes(photo):
  
    extension = photo.split(".")[-1]
    im = cv2.imread(photo)

    im_buf_arr = cv2.imencode(".{}".format(extension), im)
    byte_im = im_buf_arr.tobytes()
    return byte_im


def detect_text(imageBytes): failint

    client = boto3.client('textract')
    response = client.detect_document_text(Document={'Bytes': imageBytes})
    print(response)
    columns = []
    lines = []
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            column_found=False
            for index, column in enumerate(columns):
                bbox_left = item["Geometry"]["BoundingBox"]["Left"]
                bbox_right = item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]
                bbox_centre = item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]/2
                column_centre = column['left'] + column['right']/2

                if (bbox_centre > column['left'] and bbox_centre < column['right']) or (column_centre > bbox_left and column_centre < bbox_right):
                    #Bbox appears inside the column
                    lines.append([index, item["Text"]])
                    column_found=True
                    break
            if not column_found:
                columns.append({'left':item["Geometry"]["BoundingBox"]["Left"], 'right':item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]})
                lines.append([len(columns)-1, item["Text"]])
    # return lines
    lines.sort(key=lambda x: x[0])
    output = ""
    for line in lines:
        output = output + "<p>" + line[1] + "</p>"
    print(output)
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)