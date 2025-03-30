def check_memory(usage):

    if usage >30:
        return "High memory usage"
        return "memory is normal"
    print(check_memory(30))