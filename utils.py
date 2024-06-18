from random import randrange
import matplotlib.pyplot as plt

def get_resultado_operacion(p_ganar: float) -> bool:
    value = randrange(1, 100000)
    return value < p_ganar*1000

def get_profit(promedio_ganadora: float, curr_balance: float) -> float:
    return curr_balance*(promedio_ganadora/100)

def get_loss(promedio_perdedora: float, curr_balance: float) -> float:
    return curr_balance*(promedio_perdedora/100)*-1
    
def simulate(
    p_ganar: float, 
    promedio_ganadora: float, 
    promedio_perdedora: float,
    balance_inicial: float,
    objetivo: float,
    objetivo_perdida: float
) -> list:
    curr_balance = balance_inicial
    operaciones = [curr_balance]
    while curr_balance < objetivo and curr_balance > objetivo_perdida:
        # Operamos y obtenemos el resultado
        resultado = get_resultado_operacion(p_ganar)
        
        # Establecemos el profit en base al resultado
        profit = get_profit(promedio_ganadora, curr_balance) if resultado else get_loss(promedio_perdedora, curr_balance)
        
        # Actualizamos el balance
        curr_balance += profit
        
        # Añadimos el nuevo balance
        operaciones.append(curr_balance)
        
    return operaciones

def draw_results(results: list, balance_inicial: float):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    markers = ['o', 's', '^', 'd']
    linestyles = ['-', '--', '-.', ':']
    colors = ['b', 'g', '#0088ff', '#00ff00']
    colors_fail = ['#ff0000', '#ff2200', '#ff6600', '#ff8800', '#ff8822']
    
    for i, result in enumerate(results):
        ax.plot(
            result, 
            marker=markers[i%len(markers)], 
            linestyle=linestyles[i%len(linestyles)], 
            color=colors[i%len(colors)] if result[-1] > balance_inicial else colors_fail[i%len(colors_fail)], 
            linewidth=2, 
            markersize=8,
        )
        
    ax.set_title('Simulación prueba de fondeo')
    ax.set_xlabel('Operaciones')
    ax.set_ylabel('Balance')
    
    plt.show()
    

def run_simulations(
    number_simulations: int,
    p_ganar: float, 
    promedio_ganadora: float, 
    promedio_perdedora: float,
    balance_inicial: float,
    objetivo: float,
    objetivo_perdida: float
):
    results = []
    successes = []
    failures = []
    num_success = 0
    for _ in range(number_simulations):
        result = simulate(p_ganar, promedio_ganadora, promedio_perdedora, balance_inicial, objetivo, objetivo_perdida)
        results.append(result)
        num_success += 1 if result[-1] >= objetivo else 0
        if result[-1] >= objetivo:
            successes.append(result)
        else:
            failures.append(result)
    print(f"Porcentaje de pruebas de fondeo pasadas: {(num_success/number_simulations)*100}% ({num_success}/{number_simulations})")
    return results, successes, failures

def get_shortest(results, balance_inicial):
    idx = -1
    for i, r in enumerate(results):
        if idx == -1 or (len(results[idx]) > len(r) and r[-1] > balance_inicial):
            idx = i
    
    return None if idx == -1 else results[idx]


def get_longest(results, balance_inicial):
    idx = -1
    for i, r in enumerate(results):
        if idx == -1 or (len(results[idx]) < len(r) and r[-1] > balance_inicial):
            idx = i
    
    return None if idx == -1 else results[idx]


def get_longest(results, balance_inicial):
    idx = -1
    for i, r in enumerate(results):
        if idx == -1 or (len(results[idx]) < len(r) and r[-1] > balance_inicial):
            idx = i
    
    return None if idx == -1 else results[idx]

def get_average_duration(results):
    num_operations = []
    for r in results:
        num_operations.append(len(r))
        
    return sum(num_operations)/len(num_operations)