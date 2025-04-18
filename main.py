def minimax(node, depth, maximizing_player, tree):

    if node not in tree:
        return node

    if maximizing_player:
        return max(minimax(child, depth + 1, False, tree) for child in tree[node])
    else:
        return min(minimax(child, depth + 1, True, tree) for child in tree[node])



tree = {
    'a': ['b', 'c', 'd'],
    'b': ['e', 'f'],
    'c': ['g', 'h'],
    'd': ['i', 'j', 'k'],
    'e': [4, 8],
    'f': [8, 3],
    'g': [7, 9],
    'h': [4, 1],
    'i': [0, 5],
    'j': [7, 8],
    'k': [1, 5]
}


value = minimax('a', 0, True, tree)
print("Valeur minimax de l'arbre :", value)


best_move = None
best_value = float('-inf')

for child in tree['a']:
    child_value = minimax(child, 1, False, tree)
    print(f"Valeur de {child} : {child_value}")
    if child_value > best_value:
        best_value = child_value
        best_move = child

print("Meilleur coup pour MAX :", best_move)
#finish