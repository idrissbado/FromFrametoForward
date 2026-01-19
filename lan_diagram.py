"""
LAN Diagram Generator
Author: idrissbado
Generates a simple network diagram for the small LAN scenario using matplotlib and networkx.
"""
import matplotlib.pyplot as plt
import networkx as nx

def draw_lan_diagram():
    G = nx.Graph()
    # Add nodes
    G.add_node('Router', type='router')
    G.add_node('Switch 1', type='switch')
    G.add_node('Switch 2', type='switch')
    for i in range(1, 5):
        G.add_node(f'PC {i}', type='pc')
    G.add_node('Printer', type='printer')
    G.add_node('Wi-Fi AP', type='ap')
    G.add_node('Wireless Dev 1', type='wifi')
    G.add_node('Wireless Dev 2', type='wifi')
    G.add_node('Internet', type='cloud')
    # Add edges
    G.add_edge('Router', 'Internet')
    G.add_edge('Router', 'Switch 1')
    G.add_edge('Router', 'Switch 2')
    for i in range(1, 3):
        G.add_edge('Switch 1', f'PC {i}')
    for i in range(3, 5):
        G.add_edge('Switch 2', f'PC {i}')
    G.add_edge('Switch 2', 'Printer')
    G.add_edge('Router', 'Wi-Fi AP')
    G.add_edge('Wi-Fi AP', 'Wireless Dev 1')
    G.add_edge('Wi-Fi AP', 'Wireless Dev 2')
    # Node positions
    pos = {
        'Internet': (0, 3),
        'Router': (0, 2),
        'Switch 1': (-2, 1),
        'Switch 2': (2, 1),
        'PC 1': (-3, 0),
        'PC 2': (-1, 0),
        'PC 3': (1, 0),
        'PC 4': (3, 0),
        'Printer': (2, -0.5),
        'Wi-Fi AP': (0, 1),
        'Wireless Dev 1': (-0.7, 0),
        'Wireless Dev 2': (0.7, 0),
    }
    # Node colors/icons
    color_map = {
        'router': '#FF9800',
        'switch': '#2196F3',
        'pc': '#4CAF50',
        'printer': '#9C27B0',
        'ap': '#00BCD4',
        'wifi': '#FFC107',
        'cloud': '#BDBDBD',
    }
    node_colors = [color_map[G.nodes[n]['type']] for n in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1800, font_size=10, font_weight='bold', edge_color='#888')
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#FF9800', label='Router'),
        Patch(facecolor='#2196F3', label='Switch'),
        Patch(facecolor='#4CAF50', label='PC'),
        Patch(facecolor='#9C27B0', label='Printer'),
        Patch(facecolor='#00BCD4', label='Wi-Fi AP'),
        Patch(facecolor='#FFC107', label='Wireless Device'),
        Patch(facecolor='#BDBDBD', label='Internet'),
    ]
    plt.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=4)
    plt.title('Small Office LAN Diagram')
    plt.tight_layout()
    plt.savefig('lan_diagram.png', bbox_inches='tight')
    plt.close()
    print("LAN diagram saved as lan_diagram.png")

if __name__ == "__main__":
    draw_lan_diagram()
