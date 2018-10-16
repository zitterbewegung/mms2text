# mms2text
[![Build Status](https://travis-ci.com/zitterbewegung/mms2text.svg?branch=master)](https://travis-ci.com/zitterbewegung/mms2text)

A way to identiy what is in a picture sent by a text. This is a simple flask app that takes a picture from an MMS and then classifies what is in the image. We use Twilio to understand what is in an MMS and to send the SMS response. Then we use Clarfai to understand what is in the image and we return the top three responses.

## Motivation

I created this project to see how to interface the twilio api and the clarfai api and do something concrete with them for fun. I learned a bunch about how twilio recieves and sends SMS and MMS responses. Also, how the Clarfai returns results and how to understand the resulting concepts. The final thing I learned was how to design text based interfaces.

## Installation

First clone this repository.

Then copy the env.example and paste in your clarfai credentials. You can signup at https://clarifai.com/developer/account/signup/

## License

This software is released under the Apache Licence 2.0
