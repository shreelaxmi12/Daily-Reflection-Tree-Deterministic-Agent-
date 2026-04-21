import json

# load tree
with open("reflection-tree.json", encoding="utf-8") as f:
    tree = json.load(f)

# convert list to dictionary
nodes = {node["id"]: node for node in tree}

current = "START"
last_answer = None

while True:
    node = nodes[current]

    # print text if exists
    if "text" in node:
        print("\n" + node["text"])

    # END node
    if node["type"] == "end":
        break

    # START node → move to first question
    elif node["type"] == "start":
        current = "A1_Q1"

    # QUESTION node
    elif node["type"] == "question":
        options = node["options"]

        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        choice = int(input("Select option: ")) - 1
        last_answer = options[choice]

        # routing logic
        if current == "A1_Q1":
            current = "A1_D1"
        elif current == "A1_Q_HIGH":
            current = "A1_R_INT"
        elif current == "A1_Q_LOW":
            current = "A1_R_EXT"
        elif current == "A2_Q1":
            current = "A2_D1"
        elif current == "A3_Q1":
            current = "A3_R"

    # DECISION node
    elif node["type"] == "decision":
        for rule in node["condition"]:
            if last_answer in rule["if"]:
                current = rule["go_to"]
                break

    # REFLECTION, BRIDGE, SUMMARY
    elif node["type"] in ["reflection", "bridge", "summary"]:
        input("Press Enter to continue...")
        current = node["next"]