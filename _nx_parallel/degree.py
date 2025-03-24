from joblib import Parallel, delayed
import networkx as nx

def parallel_degree(G, n_jobs=2):
    """Calculate node degrees in parallel."""
    def calc_degree(node):
        return (node, G.degree(node))
    
    result = Parallel(n_jobs=n_jobs)(delayed(calc_degree)(node) for node in G.nodes())
    return dict(result)
