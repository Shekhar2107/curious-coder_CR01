import io
from flask import Flask, render_template, send_file
import subprocess
import os
from gtts import gTTS
import pyttsx3
from flask import Flask, render_template, request, redirect, url_for
import subprocess
import time

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/luna_adventure')
def luna_adventure():
    return render_template('luna_adv_read_more.html')

@app.route('/create_one')
def create():
    return render_template('create.html')



@app.route('/read_paragraph')
def read_paragraph():
    # Retrieve the paragraph content from your HTML file or database
    paragraph_content = "In the mystical land of Etherealis, where ancient forests whispered tales of forgotten magic, a celestial event known as the Harmony Eclipse occurs once every thousand years. Legend has it that during this rare celestial alignment, a gateway to the realm of eternity opens, revealing a powerful artifact that can shape the destiny of the world.Enter Luna, a young and talented enchantress with a mysterious past. As the Harmony Eclipse approaches, Luna discovers a hidden prophecy that foretells the artifact's ability to either bring unparalleled prosperity or plunge Etherealis into eternal darkness. Determined to unravel the secrets of the prophecy, Luna sets out on a journey with her loyal companions, a mischievous forest sprite named Zephyr and a wise old sage named Orion.As Luna navigates through enchanted landscapes and encounters magical creatures, she must forge alliances and make decisions that will impact the fate of Etherealis. Along the way, she meets enigmatic individuals, each holding a piece of the puzzle. Among them is Seraphiel, a brooding guardian with a tragic past, and Astra, a spirited astronomer with a connection to the stars.In this visual novel, players guide Luna through a captivating narrative, balancing the delicate harmony between magic and nature. The choices made by players will not only influence Luna's personal journey but also determine the outcome of the Harmony Eclipse and the destiny of Etherealis.As Luna delves deeper into the mystery, she discovers hidden truths about herself and the world around her. The lines between ally and adversary blur, and Luna must confront the shadows of her past to unlock the true potential of the artifact.Will Luna embrace the light within her and lead Etherealis to a new era of prosperity, or will the darkness consume her, shrouding the land in eternal night? The answers lie within the choices you make as Luna's destiny unfolds during the extraordinary Harmony Eclipse."  # Update with your actual content

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 120)  # Speed of speech

    # Read the text directly without saving to a file
    engine.say(paragraph_content)
    engine.runAndWait()

    return render_template('luna_adv_read_more.html')

@app.route('/download_sample')
def download_sample():
    # Create a sample text file
    sample_text = "This is a sample text file."
    file_content = io.StringIO(sample_text)
    
    # Send the file as a response with appropriate headers
    return send_file(file_content, as_attachment=True, download_name='sample.txt', mimetype='text/plain')


VIDEO_TITLES = ["parallel worlds", "The celestial heist","The last letter"]
VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), "videos")
@app.route('/generate', methods=['POST'])
def generate():
    writer_prompt = request.form['writer_prompt']

    # Check if the user input matches any video title
    matching_video = next((title for title in VIDEO_TITLES if writer_prompt.lower() in title.lower()), None)

    return render_template('create.html', writer_prompt=writer_prompt, matching_video=matching_video)

@app.route('/play')
def play():
    matching_video = request.args.get('matching_video')

    if matching_video and matching_video in VIDEO_TITLES:
        video_filename = f"{matching_video}.mp4"
        video_path = os.path.join(VIDEO_FOLDER, video_filename)
        return send_file(video_path, as_attachment=True)
    else:
        return "Video not found."

if __name__ == '__main__':
    app.run(debug=True)
