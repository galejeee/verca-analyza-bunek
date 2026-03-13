from flask import Flask, request

app = Flask(__name__)


def calculate_growth_rate(values):
    differences = []

    for i in range(len(values) - 1):
        diff = values[i + 1] - values[i]
        differences.append(diff)

    if len(set(differences)) == 1:
        return differences[0]
    else:
        return None


@app.route("/")
def home():
    return """
    <h1>Analýza růstu buněk</h1>

    <form action="/analyze" method="post">
        Zadej hodnoty oddělené čárkou:<br><br>

        <input name="values" placeholder="např. 10,12,14,16">

        <br><br>

        <button type="submit">Analyzovat</button>
    </form>
    """


@app.route("/analyze", methods=["POST"])
def analyze():
    values = request.form["values"]

    try:
        numbers = list(map(int, values.split(",")))
    except:
        return """
        <h2>Chyba: zadej jen čísla oddělená čárkou</h2>
        <a href="/">Zpět</a>
        """

    rate = calculate_growth_rate(numbers)

    result = f"""
    <h2>Výsledky</h2>

    Min: {min(numbers)}<br>
    Max: {max(numbers)}<br>
    Průměr: {sum(numbers) / len(numbers)}<br>
    """

    if rate is None:
        result += "<br><b>Růst není lineární ❌</b>"
    else:
        result += f"<br><b>Lineární růst ✅</b><br>Rychlost růstu: {rate}"

    result += "<br><br><a href='/'>Zpět</a>"

    return result


if __name__ == "__main__":
    app.run(debug=True)