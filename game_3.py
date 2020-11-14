from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def guess_of_numbers():
    if request.method == 'GET':
        return f'''
            <form action="/" method="POST">
                <p>
                    <input type"hidden" name="min" value=0>
                    <input type"hidden" name="max" value=1000> 
                </p>    
            <label>
                Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbkach
            </label>
            <label>
                <button type="submit" name="answer" value="OK">
                OK
                </button>
            </label>
            </form>
            '''
    elif request.method == 'POST':
        answer = input(request.form["answer"])
        min = int(input(request.form["min"]))
        max = int(input(request.form["max"]))
        guess = int((max - min) / 2) + min

        if min == max:
            return f'''
                <form action="/" method="POST">
                <p>
                    <p type"hidden" name="guess" value={min}></p>
                    <p type"hidden" name="guess" value={max}> </p>
                </p>                
                <label>
                    NIE OSZUKUJ!
                </label>
                <label>   
                Zgaduję: {guess}
                </label>
                <label>   
                    Jaka jest twoja odpowiedź
                    <button type="submit" name="answer" value="Too big">
                    Too big
                    </button>
                    <button type="submit" name="answer" value="Too small">
                    Too small
                    </button>
                    <button type="submit" name="answer" value="You win">
                    You win
                    </button>
                </label>
                </form>
                '''

        elif answer == 'You win':
            return "Wygrałeś!"
        elif answer == 'Too big':
            max = guess
            return f'''
                <form action="/" method="POST">
                <p>
                    <p type"hidden" name="guess" value={min}></p>
                    <p type"hidden" name="guess" value={max}> </p>
                </p>
                <label>   
                Zgaduję: {guess}
                </label>                  
                <label>
                    Jaka jest twoja odpowiedź
                    <button type="submit" name="answer" value="Too big">
                    Too big
                    </button>
                    <button type="submit" name="answer" value="Too small">
                    Too small
                    </button>
                    <button type="submit" name="answer" value="You win">
                    You win
                    </button>
                </label>
                </form>
                '''
        elif answer == 'Too small':
            min = guess
            return f'''
                <form action="/" method="POST">
                <p>
                    <p type"hidden" name="guess" value={min}></p>
                    <p type"hidden" name="guess" value={max}> </p>
                </p>
                <label>   
                Zgaduję: {guess}
                </label>                  
                <label>
                    Jaka jest twoja odpowiedź
                    <button type="submit" name="answer" value="Too big">
                    Too big
                    </button>
                    <button type="submit" name="answer" value="Too small">
                    Too small
                    </button>
                    <button type="submit" name="answer" value="You win">
                    You win
                    </button>
                </label>
                </form>
                '''
        else:
            return f'''
                <form action="/" method="POST">
                <label>   
                Zgaduję: {guess}
                </label>
                <p>
                    <p type"hidden" name="guess" value={min}></p>
                    <p type"hidden" name="guess" value={max}> </p>
                </p>
                <label>
                    Jaka jest twoja odpowiedź
                    <button type="submit" name="answer" value="Too big">
                    Too big
                    </button>
                    <button type="submit" name="answer" value="Too small">
                    Too small
                    </button>
                    <button type="submit" name="answer" value="You win">
                    You win
                    </button>
                </label>
                </form>
                '''

if __name__ == "__main__":
    app.run(debug=True)
