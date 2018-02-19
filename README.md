# mms2text
A way to identiy what is in a picture sent by a text. This is a simple flask app that takes a picture from an MMS and then classifies what is in the image. We use Twilio to understand what is in an MMS and to send the SMS response. Then we use Clarfai to understand what is in the image and we return the top three responses.

## Motivation

I created this project to see how to interface the twilio api and the clarfai api and do something concrete with them for fun. I learned a bunch about how twilio recieves and sends SMS and MMS responses. Also, how the Clarfai returns results and how to understand the resulting concepts. The final thing I learned was how to design text based interfaces.

## Installation

First clone this repository.

Then copy the env.example and paste in your clarfai credentials. You can signup at https://clarifai.com/developer/account/signup/


## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

This software is released under the Apache Licence 2.0
