def get_distance_matrix(num_routers):
    distance_matrix = []
    print(f"Enter the distance matrix for {num_routers} routers:")
    for i in range(num_routers):
        row = input(f"Enter distances for router {i+1} : ")
        distance_matrix.append(list(map(float, row.split())))
    return distance_matrix

def distance_vector_routing(distance_matrix):
    num_routers = len(distance_matrix)
    distance_vectors = [list(row) for row in distance_matrix]

    for i in range(num_routers):
        for j in range(num_routers):
            for k in range(num_routers):
                if distance_vectors[i][j] > distance_vectors[i][k] + distance_vectors[k][j]:
                    distance_vectors[i][j] = distance_vectors[i][k] + distance_vectors[k][j]

    for i in range(num_routers):
        print(f"Router {i+1} distance vector: {distance_vectors[i]}")

def main():
    num_routers = int(input("Enter the number of routers: "))
    distance_matrix = get_distance_matrix(num_routers)
    distance_vector_routing(distance_matrix)

main()

