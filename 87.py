#https://www.youtube.com/watch?v=0YZqY_zQop4&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=157
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Accessing form data
        form_data = request.form['exampleInput']

        # Create a string to hold all header information
        headers_info = "Headers Received:\n"
        for header, value in request.headers:
            headers_info += f"{header}: {value}\n"

        # Accessing a specific header (e.g., User-Agent)
        user_agent = request.headers.get('User-Agent', 'No-User-Agent')

        # Combine form data, specific header, and all headers for display
        response = (f"Received input: {form_data}\n"
                    f"Specific User-Agent Header: {user_agent}\n\n"
                    f"All Headers:\n{headers_info}")

        return response
    else:
        # Render a simple form when the method is GET
        return '''
            <form method="post">
                <label for="exampleInput">Example Input:</label>
                <input type="text" id="exampleInput" name="exampleInput">
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
#Host

# Key: request.headers['Host']
# Value: '127.0.0.1:5000'
# User-Agent

# Key: request.headers['User-Agent']
# Value: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
# Accept

# Key: request.headers['Accept']
# Value: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
# Accept-Language

# Key: request.headers['Accept-Language']
# Value: 'nl,en-US;q=0.7,en;q=0.3'
# Accept-Encoding

# Key: request.headers['Accept-Encoding']
# Value: 'gzip, deflate, br'
# Referer

# Key: request.headers['Referer']
# Value: 'http://127.0.0.1:5000/'
# Content-Type

# Key: request.headers['Content-Type']
# Value: 'application/x-www-form-urlencoded'
# Content-Length

# Key: request.headers['Content-Length']
# Value: '18'
# Origin

# Key: request.headers['Origin']
# Value: 'http://127.0.0.1:5000'
# Dnt (Do Not Track)

# Key: request.headers['Dnt']
# Value: '1'
# Connection

# Key: request.headers['Connection']
# Value: 'keep-alive'
# Upgrade-Insecure-Requests

# Key: request.headers['Upgrade-Insecure-Requests']
# Value: '1'
# Sec-Fetch-Dest

# Key: request.headers['Sec-Fetch-Dest']
# Value: 'document'
# Sec-Fetch-Mode

# Key: request.headers['Sec-Fetch-Mode']
# Value: 'navigate'
# Sec-Fetch-Site

# Key: request.headers['Sec-Fetch-Site']
# Value: 'same-origin'
# Sec-Fetch-User

# Key: request.headers['Sec-Fetch-User']
# Value: '?1'
