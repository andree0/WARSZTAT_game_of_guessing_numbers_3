from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def guess_of_numbers():
    if request.method == 'GET':
        user_min = 0
        user_max = 1000
        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
            <title>Guess The Number</title>
            </head>
            <body>
            <h1>Imagine number between 0 and 1000</h1>
            <form action="" method="POST">
            <input type="hidden" name="user_min" value={user_min}>
            <input type="hidden" name="user_max" value={user_max}>
            <input type="submit" value="OK">
            </form>
            </body>
            </html>
            '''
    else:
        answer = input(request.form.get("answer"))
        user_min = int(input(request.form.get("user_min")))
        user_max = int(input(request.form.get("user_max")))
        guess = int(input(request.form.get("guess")))

        if answer == 'You win':
            return f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <title>Guess The Number</title>
                </head>
                <body>
                <h1>Hurra! I guess! Your number is {guess}</h1>
                </body>
                </html>
                '''
        elif answer == 'Too big':
            user_max = guess

        elif answer == 'Too small':
            user_min = guess

        guess = int((user_max - user_min) / 2) + user_min

        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Guess The Number</title>
            </head>
            <body>
            <h1>It is number {guess}</h1>
                <form action="/" method="POST">
                    <input type="submit" name="answer" value="Too big">
                    <input type="submit" name="answer" value="Too small">
                    <input type="submit" name="answer" value="You win">
                    <input type="hidden" name="guess" value="{guess}">
                    <input type"hidden" name="user_min" value={user_min}>
                    <input type"hidden" name="user_max" value={user_max}>
                </form>            
            </body>
            </html>
            '''


if __name__ == "__main__":
    app.run(debug=True)
