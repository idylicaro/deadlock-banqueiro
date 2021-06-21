class Process:
    def __init__(self, allocate, max):
        self.allocate: [] = allocate
        self.max: [] = max
        self.required: [] = []
        self.is_executable: bool = False
        self.has_already_executed: bool = False

    # TODO: fazer um do while, marca todos os executaveis, e dps executar os possiveis, verificar novamente com o
    # novo estado do banco, e o while acaba ao nao ter mais executaveis ou nao houver processos sem ser executados antes.


class Bank:
    def __init__(self, available, processes):
        self.available: [] = available
        self.processes: [Process] = processes


def process_required_matrix(allocate, max, available):
    matrix_required = []
    count_process = len(allocate)
    count_resource = len(available)
    for i in range(0, count_process, 1):
        aux_resource = []
        for j in range(0, count_resource, 1):
            aux_resource.append(int(max[i][j]) - int(allocate[i][j]))
        matrix_required.append(aux_resource)

    return matrix_required


def main():
    archive = open('test.txt', 'r')

    i = 0;
    matrix_allocate = []
    matrix_max = []
    vector_available = []

    for line in archive:
        line = line.replace('\n', '')
        if line == ';':
            i += 1
            continue
        data = line.split(' ')
        if i == 0:
            matrix_allocate.append(data)
        elif i == 1:
            matrix_max.append(data)
        elif i == 2 and line != '':
            vector_available = data

    archive.close()
    result = process_required_matrix(matrix_allocate, matrix_max, vector_available)
    print(result)


if __name__ == "__main__":
    main()
