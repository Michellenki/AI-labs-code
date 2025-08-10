# Knowledge base: rules mapping (item, color) to actions
knowledge_base = {
    ("Designer Handbag", "Rose Gold"): "Dazzles",
    ("Stiletto Heels", "Champagne"): "Slays"
}
items = ["Designer Handbag", "Stiletto Heels"]
colors = ["Rose Gold", "Champagne"]
actions = ["Struts", "Dazzles", "Charms", "Slays"]

def display_items():
    print("\nSelect a chic item:")
    print("1. Designer Handbag")
    print("2. Stiletto Heels")
    print("Enter choice (1 or 2): ", end='')

def display_colors():
    print("\nColor options:")
    print("1. Rose Gold")
    print("2. Champagne")
    print("Enter color choice (1 or 2): ", end='')

def forward_chain(facts):
    """
    Apply forward chaining to derive an action based on item and color facts.
    Returns the action if a rule matches, else None.
    """
    item, color = facts
    return knowledge_base.get((item, color), None)

def main():
    while True:
        print("\n*----- Chic Style Selector (Forward Chaining) -----*")
        display_items()
        
        # Get item input
        try:
            x = int(input())
            if x not in [1, 2]:
                print("\nError: Please select 1 (Designer Handbag) or 2 (Stiletto Heels).")
                continue
        except ValueError:
            print("\nError: Invalid input! Please enter a number (1 or 2).")
            continue
        
        selected_item = items[x - 1]