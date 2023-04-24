from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/analyzer', methods=['POST'])
def hello_world():
    # Getting parameters from json input body
    age = request.get_json()["age"]
    weight = request.get_json()["weight"]
    last_steps = request.get_json()["last_steps"]
    steps_goal = request.get_json()["steps_goal"]
    bcs_index = request.get_json()["bcs_index"]

    avg_steps = sum(last_steps)/len(last_steps)
    goal_weight = (100/(((bcs_index - 5) * 10) + 100)) * weight

    STEPS_SCORE = min(1, avg_steps/steps_goal)
    WEIGHT_SCORE = min(goal_weight, weight) / max(goal_weight, weight)

    # pounded formula
    # weight for diff from current weight to goal weight -> 0.8
    # weight for diff from current average steps per day to goal -> 0.2

    WEIGHT_FOR_WEIGHT_SCORE = 0.8
    WEIGHT_FOR_STEPS_SCORE = 0.2
    HEALTH_SCORE = WEIGHT_FOR_WEIGHT_SCORE * WEIGHT_SCORE + WEIGHT_FOR_STEPS_SCORE * STEPS_SCORE

    return jsonify({"health_score":HEALTH_SCORE})
