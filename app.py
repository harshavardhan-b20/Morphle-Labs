from flask import Flask, redirect, url_for
import os
import datetime
import platform
import subprocess  

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    
    name = "Harshavardhan Bellamkonda"
    
    
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    
    
    server_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime("%Y-%m-%d %H:%M:%S")
    
    
    system_info = platform.platform()
    python_version = platform.python_version()
    
    
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Could not retrieve top command output: {str(e)}"
    

    html_content = f"""
    <html>
        <body>
            <h2>Name: {name}</h2>
            <h3>User: {username}</h3>
            <h3>Server Time (IST): {server_time}</h3>
            <h3>System Info: {system_info}</h3>
            <h3>Python Version: {python_version}</h3>
            <h3>Top Output:</h3>
            <pre>{top_output}</pre>
            
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
