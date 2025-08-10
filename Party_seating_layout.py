def layout(N, C, L):
    # Initialize dictionary to store guest to table assignments
    assignment = {}
    
    # Try to assign each guest to a table
    for guest in range(N):
        # Assign to a random table (0 to C-1), but check restrictions
        valid_tables = list(range(C))
        for other_guest, table in assignment.items():
            if (guest, other_guest) in L or (other_guest, guest) in L:
                if table in valid_tables:
                    valid_tables.remove(table)
        
        if not valid_tables:
            return False  # No valid table available due to restrictions
        
        assignment[guest] = valid_tables[0]  # Assign to first valid table
    
    return assignment

# Example usage
N = 5  # Number of guests
C = 2  # Number of tables
L = [(0, 1), (2, 3)]  # Restricted pairs
result = layout(N, C, L)
print(result)