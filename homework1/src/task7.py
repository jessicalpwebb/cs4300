import matplotlib.pyplot as plt

def plot(output_file: str = "plot.png") -> str:
    x = [1, 2, 3, 4, 5]
    y = [n+10 for n in x] 
    
    plt.figure()
    plt.plot(x, y, marker="o", label="y = x+10")
    plt.title("Example Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig(output_file)
    plt.close()
    
    return output_file