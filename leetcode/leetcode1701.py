class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0.0
        if len(customers) == 1:
            return customers[0][1]
        length = len(customers)
        service_time = customers[0][0]
        all_time = 0
        for item in customers:
            if item[0] > service_time:  # 不需要等待直接服务
                all_time += item[1]
                service_time = item[0]
                service_time += item[1]

            else:
                all_time += service_time - item[0] + item[1]
                service_time += item[1]
        return all_time / length
