customers = [[5,2],[5,4],[10,3],[20,1]]
def avg_time(customers):
    curr_time = 0
    waiting_time = []
    for arr_time,time_req in customers:
        if(arr_time>curr_time):
            iroh_waiting_time = arr_time - curr_time
            curr_time = curr_time + iroh_waiting_time
        
        wait_time = curr_time + time_req - arr_time
        waiting_time.append(wait_time)
        
        curr_time = curr_time + time_req
        
    avg = sum(waiting_time)/ len(customers)
    return avg

avg_time = avg_time(customers)
print(f"Average waiting time will be: {avg_time}")