from flask import Flask, jsonify, request,send_file
import werkzeug
import photo_edit
import base64

app = Flask(__name__)

@app.route('/datas',methods= ['GET','POST'])
def data():
    global response
    if(request.method=='POST'):
        imagefile= request.files['image']
        filename= werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save("./uploaded_images/" + filename)
        photo_edit.photoGet(filename)
        
    else:
        return send_file("uploaded_images/grogu_a8w2.1280.jpg.webp")
            
        
if(__name__ == "__main__"):
    app.debug = True
    app.run()        
    
    
    
