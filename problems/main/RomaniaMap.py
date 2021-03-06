from problems.model.impl.MapProblem import MapProblem
from search.model.Heuristic import Heuristic
from search.model.impl.uninformed.BidirectionalSearch import BidirectionalSearch
from search.model.impl.uninformed.BreadthFirstSearch import BreadthFirstSearch
from search.model.impl.uninformed.UniformCostSearch import UniformCostSearch
from search.model.impl.uninformed.DepthFirstSearch import DepthFirstSearch
from search.model.impl.uninformed.DepthFirstSearch import IterativeDeepingDFS
from search.model.impl.informed.GreedySearch import GreedySearch
from search.model.impl.informed.AStarSearch import AStarSearch

map_graph = dict(
    Arad=dict(
        Zerind=dict(distance=75),
        Sibiu=dict(distance=140),
        Timisoara=dict(distance=118)
    ),
    Bucharest=dict(
        Urziceni=dict(distance=85),
        Pitesti=dict(distance=101),
        Giurgiu=dict(distance=90),
        Fagaras=dict(distance=211)
    ),
    Craiova=dict(
        Drobeta=dict(distance=120),
        Rimnicu=dict(distance=146),
        Pitesti=dict(distance=138)
    ),
    Drobeta=dict(
        Mehadia=dict(distance=75)
    ),
    Eforie=dict(
        Hirsova=dict(distance=86)
    ),
    Fagaras=dict(
        Sibiu=dict(distance=99)
    ),
    Hirsova=dict(
        Urziceni=dict(distance=98)
    ),
    Iasi=dict(
        Vaslui=dict(distance=92),
        Neamt=dict(distance=87)
    ),
    Lugoj=dict(
        Timisoara=dict(distance=111),
        Mehadia=dict(distance=70)
    ),
    Oradea=dict(
        Zerind=dict(distance=71),
        Sibiu=dict(distance=51)
    ),
    Pitesti=dict(
        Rimnicu=dict(distance=97)
    ),
    Rimnicu=dict(
        Sibiu=dict(distance=80)
    ),
    Urziceni=dict(
        Vaslui=dict(distance=142)
    )
)

locations_positions = dict(
    Arad=(91, 492),
    Bucharest=(400, 327),
    Craiova=(253, 288),
    Drobeta=(165, 299),
    Eforie=(562, 293),
    Fagaras=(305, 449),
    Giurgiu=(375, 270),
    Hirsova=(534, 350),
    Iasi=(473, 506),
    Lugoj=(165, 379),
    Mehadia=(168, 339),
    Neamt=(406, 537),
    Oradea=(131, 571),
    Pitesti=(320, 368),
    Rimnicu=(233, 410),
    Sibiu=(207, 457),
    Timisoara=(94, 410),
    Urziceni=(456, 350),
    Vaslui=(509, 444),
    Zerind=(108, 531)
)

table = dict(
    Arad=366,
    Bucharest=0,
    Craiova=160,
    Drobeta=242,
    Eforie=161,
    Fagaras=178,
    Giurgiu=77,
    Hirsova=151,
    Iasi=226,
    Lugoj=244,
    Mehadia=241,
    Neamt=234,
    Oradea=380,
    Pitesti=98,
    Rimnicu=193,
    Sibiu=253,
    Timisoara=329,
    Urziceni=80,
    Vaslui=199,
    Zerind=374
)

heuristic = Heuristic(table)


p = MapProblem(map_graph, locations_positions, "Arad", "Bucharest")

s = UniformCostSearch(p)
print(s.solve(), s.solution_cost)

s = DepthFirstSearch(p, 7)
print(s.solve(), s.solution_cost)

s = IterativeDeepingDFS(p)
print(s.solve(), s.solution_cost)

s = BidirectionalSearch(p)
print(s.solve(), s.solution_cost)

s = BreadthFirstSearch(p)
print(s.solve(), s.solution_cost)

s = GreedySearch(p, heuristic)
print(s.solve(), s.solution_cost)

s = AStarSearch(p, heuristic)
print(s.solve(), s.solution_cost)

p.show_map()