from flask import Flask, request, render_template
import openai

# Set up OpenAI API key
openai.api_key = "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"
app = Flask(__name__)

# Define the route for the file upload page
@app.route("/")
def upload_file():
    return '''
    <!doctype html>
    <title>Upload a File</title>
    <h1>Upload a file for analysis</h1>
    <form action="/analyze" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

# Define the route to handle file upload and analysis
@app.route("/analyze", methods=["POST"])
def analyze_file():
    if "file" not in request.files:
        return "No file part in the request"
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    if file:
        content = file.read().decode("utf-8")
        # Call ChatGPT API to analyze the content
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an assistant analyzing uploaded files."},
                {"role": "user", "content": f"Analyze the following content:\n\n{content}"}
            ]
        )
        result = response['choices'][0]['message']['content']
        return f"<h1>Analysis Result</h1><p>{result}</p>"

if __name__ == "__main__":
    app.run(debug=True)
