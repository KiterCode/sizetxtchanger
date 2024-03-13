if __name__ == '__main__':
    with open('original.txt', 'r') as original_file:
        original_content = original_file.read()

target_size = 10 * 1024 * 1024  # 10MB

replication_factor = target_size // len(original_content)

with open('expanded.txt', 'w') as expanded_file:
    for _ in range(replication_factor):
        expanded_file.write(original_content)

    remaining_bytes = target_size - (len(original_content) * replication_factor)
    expanded_file.write(original_content[:remaining_bytes])

