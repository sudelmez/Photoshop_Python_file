from flask import Flask, jsonify, request, make_response
import werkzeug
import photo_edit
from io import BytesIO
import numpy as np 
import cv2

app = Flask(__name__)


@app.route('/process',methods= ['POST'])
def process():
    global response
    if(request.method=='POST'):
        imagefile= request.files['image']
        image_data = imagefile.read()
        image_array = BytesIO(image_data)
        img = cv2.imdecode(np.frombuffer(image_array.read(), np.uint8), cv2.IMREAD_COLOR)
        print(type(img))
        print(img)
        img=photo_edit.getShop(img)
    
        # Convert the OpenCV image to a suitable format (e.g., JPEG or PNG)
        ret, buffer = cv2.imencode('.jpg', img)
        image_data = buffer.tobytes()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpeg'
        return response
    
    else:
        return

if(__name__ == "__main__"):    
    app.debug = True
    app.run()        
    


#--------------------------------------------------------------------


# @app.route('/save',methods= ['POST'])

# def save():
#     global response,nameFile
#     if(request.method=='POST'):
#         imagefile= request.files['image']
#         filename= werkzeug.utils.secure_filename(imagefile.filename)
#         imagefile.save("./uploaded_images/" + filename)
                 
#     else:
#         return      
    
    
    
