import copy


class Process:
    def __init__(self, allocate, max, required):
        self.allocate: [] = allocate
        self.max: [] = max
        self.required: [] = required
        self.is_executable: bool = False
        self.has_already_executed: bool = False

    # TODO: fazer um do while, marca todos os executaveis, e dps executar os possiveis, verificar novamente com o
    # novo estado do banco, e o while acaba ao nao ter mais executaveis ou nao houver processos sem ser executados antes.


class Bank:
    def __init__(self, available, processes=None):
        if processes is None:
            processes = []
        self.available: [] = available
        self.processes: [Process] = processes

    def load_processes_and_calculate_required(self, allocate, max):
        for i in range(0, len(allocate), 1):
            aux_allocate = []
            aux_max = []
            aux_required = []
            for j in range(0, len(self.available), 1):
                aux_allocate.append(int(allocate[i][j]))
                aux_max.append(int(max[i][j]))
                aux_required.append(int(max[i][j]) - int(allocate[i][j]))
            self.processes.append(Process(aux_allocate, aux_max, aux_required))

    def is_security_state(self):
        aux_process: [Process] = copy.deepcopy(self.processes)
        aux_available = copy.deepcopy(self.available)

        for p in aux_process:
            notIsminor = False
            for i in range(0, len(self.available), 1):
                notIsminor = not p.required[i] <= int(self.available[i])
            if not notIsminor:
                p.is_executable = True

        has_some_execution = None
        aux_count = 0
        while has_some_execution != False:
            if aux_count == 0:
                has_some_execution = False

            for p in aux_process:
                if (p.has_already_executed or not p.is_executable):
                    continue
                notIsminor = False
                for i in range(0, len(self.available), 1):
                    notIsminor = not p.required[i] <= int(self.available[i])
                if not notIsminor:
                    p.has_already_executed = True
                    for x in range(0, len(self.available), 1):
                        aux_available[x] = int(aux_available[x]) + p.allocate[x]

            if not aux_count < len(self.processes):
                aux_count = 0

        is_security = True
        for p in aux_process:
            if not p.has_already_executed:
                is_security = False
                return False

        # for y in aux_process:
        #     print('aux_process:', y.has_already_executed)
        # print('aux_available:', aux_available)
        return True

    def request(self, id_p, resource):
        # dont change the bank directly
        aux_bank:Bank = copy.deepcopy(self)

        for i in range(0, len(resource), 1):
            if (int(aux_bank.available[i]) - resource[i] ) < 0:
                return False
            aux_bank.available[i] = int(aux_bank.available[i]) - resource[i]

        for i in range(0, len(aux_bank.processes[id_p].allocate), 1):
            aux_bank.processes[id_p].allocate[i] += resource[i]

        return aux_bank.is_security_state()

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
    bank = Bank(vector_available)
    bank.load_processes_and_calculate_required(matrix_allocate, matrix_max)

    print('\nRequired:')
    for i in bank.processes:
        print(i.required)
    print('\nIs_security:', bank.is_security_state())
    print('\nIs_security after request:', bank.request(0, [1, 0, 0, 0]))



if __name__ == "__main__":
    main()
