from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

bids = {}

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/place_bid', methods=['POST'])
def place_bid():
    name = request.form.get("name")
    bid = request.form.get("bid")
    if name and bid:
        bids[name] = int(bid)
        return redirect(url_for('index'))
    return jsonify({"error": "Invalid bid"}), 400

@app.route('/declare_winner', methods=['GET'])
def declare_winner():
    if not bids:
        return jsonify({"error": "No bids placed"}), 400
    max_bid = max(bids.values())
    winners = [name for name, bid in bids.items() if bid == max_bid]
    return jsonify({"winners": winners, "bid": max_bid}), 200

if __name__ == '__main__':
    app.run(debug=True)