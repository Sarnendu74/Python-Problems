def mat_design(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# Example usage
n, m = 7, 21  # Adjust dimensions as needed
mat_design(n, m)
