def parse_log_file(log_path):
    log_counts = {}
    try:
        with open(log_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.startswith("INFO:") or line.startswith("WARNING:") or line.startswith("ERROR:"):
                    level = line.split(':')[0]
                    log_counts[level] = log_counts.get(level, 0) + 1
    except FileNotFoundError:
        raise FileNotFoundError(f'Log file not found at path: {log_path}')
    return log_counts

if __name__ == "__main__":
    try:
        log_counts = parse_log_file('server.log')
        print("Статистика логов:", log_counts)
    except FileNotFoundError as e:
        print(e)
