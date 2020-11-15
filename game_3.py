from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def guess_of_numbers():
    if request.method == 'GET':
        min = 0
        max = 1000
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
            <input type="hidden" name="min" value={min}></input>
            <input type="hidden" name="max" value={max}></input>
            <input type="submit" value="OK"></input>
            </form>
            </body>
            </html>
            '''
    else:
        answer = input(request.form.get("answer"))
        min = int(input(request.form.get("min")))
        max = int(input(request.form.get("max")))
        guess = int((max - min) / 2) + min

        if min == max:
            return f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                <title>Guess The Number</title>
                </head>
                <body>
                <h1>NOT CHEAT!</h1>
                <h1>It is number {guess}</h1>
                <form action="/" method="POST">
                    <input type="submit" name="answer" value="Too big"></input>
                    <input type="submit" name="answer" value="Too small"></input>
                    <input type="submit" name="answer" value="You win"></input>
                    <input type="hidden" name="guess" value="{guess}"></input>
                    <input type"hidden" name="min" value={min}></input>
                    <input type"hidden" name="max" value={max}></input>
                </form>
                </body>
                </html>
                '''

        elif answer == 'You win':
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
            max = guess

        elif answer == 'Too small':
            min = guess

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
                    <input type="submit" name="answer" value="Too big"></input>
                    <input type="submit" name="answer" value="Too small"></input>
                    <input type="submit" name="answer" value="You win"></input>
                    <input type="hidden" name="guess" value="{guess}"></input>
                    <input type"hidden" name="min" value={min}></input>
                    <input type"hidden" name="max" value={max}></input>
                </form>            
            </body>
            </html>
            '''


if __name__ == "__main__":
    app.run(debug=True)
