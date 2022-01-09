from flask import Flask


app=Flask("Movieland")

@app.route('/')
def index():
    return "hello"
