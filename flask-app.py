from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import logging
# The client takes the `API_KEY` you created in your Clarifai
# account. You can set these variables in your environment as:

clarifai_app = ClarifaiApp()

app = Flask(__name__)


@app.route('/web')
def hello_world():
    return 'Hello from Flask!'


def get_concept(result_json, index):
    """ Returns a given concept given an index"""
    return  result_json['outputs'][0]["data"]['concepts'][index]['name']


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    # get the general model
    model = clarifai_app.models.get("general-v1.3")
    mediaurl = request.values.get('MediaUrl0', None)
    print(mediaurl)
    # predict with the model
    model = clarifai_app.models.get('general-v1.3')
    image = ClImage(url=mediaurl)
    #image = ClImage(url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Phat_Thai_kung_Chang_Khien_street_stall.jpg/240px-Phat_Thai_kung_Chang_Khien_street_stall.jpg')
    responsejson = model.predict([image])

    print(responsejson)
    print("3rd Concept" +get_concept(responsejson, 2))
    print("4rd Concept" +get_concept(responsejson, 3))
    print("5th Concept" +get_concept(responsejson, 4))
    resp = MessagingResponse()
    resp.message("I think it might be one of the following:  " +
                 get_concept(responsejson, 0) + " or " +
                 get_concept(responsejson, 1) + " or " +
                 get_concept(responsejson, 2) + " or " +
                 get_concept(responsejson, 3))
    print(resp.message)
    return str(resp)


if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(debug=True, port=8080)

