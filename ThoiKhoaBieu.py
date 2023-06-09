import random
import math

# khởi tạo các hằng số
INITIAL_TEMPERATURE = 100
COOLING_RATE = 0.03
MIN_TEMPERATURE = 1e-8
MAX_STEPS = 5000


# khởi tạo thời khóa biểu ngẫu nhiên
def generate_initial_assignments(m, n, p):
    assignments = [[random.choice([0, 1]) for _ in range(p)] for _ in range(m * n)]
    return assignments


# Tính năng lượng của thời khóa biểu hiện tại
def calculate_energy(assignments, R, T, C, D):
    energy = 0
    for i in range(len(assignments)):
        for j in range(len(assignments[i])):
            if assignments[i][j] == 1:
                class_idx = i % len(R)
                teacher_idx = i // len(R)
                energy += R[class_idx][teacher_idx]
                energy += T[teacher_idx][j] * C[class_idx][j] * D[class_idx][j]
    return energy


# Thuật toán Simulated annealing để tìm ra phương án tối ưu
def simulated_annealing(m, n, p, R, T, C, D):
    # khởi tạo thời khóa biểu ngẫu nhiên
    current_assignments = generate_initial_assignments(m, n, p)
    # print("----------")
    # for i in range(m*n):
    #     print(current_assignments[i])
    # print("----------")
    current_energy = calculate_energy(current_assignments, R, T, C, D)
    best_assignments = current_assignments
    best_energy = current_energy
    temperature = INITIAL_TEMPERATURE
    step = 0

    while temperature > MIN_TEMPERATURE and step < MAX_STEPS:
        # Tạo thời khóa biểu mới bằng cách hoàn đổi lịch trong thời khóa biểu hiện tại
        new_assignments = current_assignments.copy()
        idx1 = random.randint(0, len(new_assignments) - 1)
        idx2 = random.randint(0, len(new_assignments) - 1)
        new_assignments[idx1], new_assignments[idx2] = new_assignments[idx2], new_assignments[idx1]

        # Tính năng lượng của thời khóa biểu mới
        new_energy = calculate_energy(new_assignments, R, T, C, D)

        # Xác định xem thời khóa biểu mới có tối ưu hơn không
        delta_energy = new_energy - current_energy
        if delta_energy < 0 or math.exp(-delta_energy / temperature) > random.uniform(0, 1):
            current_assignments = new_assignments
            current_energy = new_energy

        # Nếu tối ưu hơn thì cập nhật lại thời khóa biểu
        if current_energy < best_energy:
            best_assignments = current_assignments
            best_energy = current_energy

        # Giảm nhiệt độ xuống để tiếp tục xét các trường hợp khác
        temperature *= 1 - COOLING_RATE

        # tăng bước lặp lên 1
        step += 1

    # trả về thời khóa biểu tốt nhất
    return best_assignments  # , best_energy


# Define the main function
def main():
    # Define the input matrices
    m = 3  # m: lớp học c1,c2,c3,...cm
    n = 5  # n : giáo viên t1,t2,..,tn
    p = 10  # p: số tiết học trong mỗi tuần 1,2,...,p

    # start
    #      #. Ma trận R kích thước m x n thể hiện phân công giáo viên
    #     #  sao cho phần tử rij  là số tiết mà giáo viên tj  phải dạy cho lớp ci trong một tuần
    R = [[10, 3, 1, 4, 3],
         [1, 6, 3, 4, 8],
         [1, 2, 2, 3, 6]]
    #     #[[random.randint(1, p) for j in range(n)] for i in range(m)]

    #     # Hai ma trậnTnxp và Cmxp thể hiện các tiết
    #     # mà giáo viên và lớp có thể dạy hoặc học.
    # trậnTnxp và Cmxp thể hiện các tiết mà giáo viên và lớp có thể dạy hoặc học.
    # Cụ thể, tjk =1 nếu giáo viên j có thể dạy vào tiết k, và tjk = 0 nế
    T = [[1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
         [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0]]
    #     #[[random.randint(0, 1) for j in range(p)] for i in range(n)] #
    C = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]]
    # #    [[random.randint(0, 1) for j in range(p)] for i in range(m)]

    #     # Dm x p là ma trận ràng buộc sao cho tjk =1 nếu lớp i bắt buộc
    #     # phải học vào tiết k và tjk = 0 nếu không bắt buộc.
    D = [[0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]]

    #   T = [[1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    #      [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    #      [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    #      [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    #        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0]]
    # #  [[random.randint(0, 1) for j in range(p)] for i in range(m)]
    #     # Chạy thuật toán simulated annealing để tìm ra thời khóa biểu tối ưu

    # end
    # R=[[random.randint(1, p) for j in range(n)] for i in range(m)]
    # print(R)
    # T= [[random.randint(0, 1) for j in range(p)] for i in range(n)] #
    # print(T)
    # C= [[random.randint(0, 1) for j in range(p)] for i in range(m)]
    # print(C)
    # D=[[random.randint(0, 1) for j in range(p)] for i in range(m)]
    # print(D)
    best_R = simulated_annealing(m, n, p, R, T, C, D)

    # In ra kết quả
    print("Thời khóa biểu tối ưu :")
    for i in range(n):
        print(best_R[i])
# Call the main function
if __name__ == '__main__':
    main()