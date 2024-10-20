def minOperations(n):
  """
  Calculates the minimum number of operations to reach n characters with only Copy All and Paste operations.

  Args:
      n: The target number of characters.

  Returns:
      The minimum number of operations needed, or 0 if impossible.
  """
  if n == 0:
    return 0  # Cannot create 0 characters

  # Start with 1 character (the initial H)
  operations = 0
  current = 1

  while current < n:
    # Double the current number of characters (efficient copy-paste)
    operations += 2
    current *= 2

    # If we overshot the target (can happen on even n), adjust
    if current > n:
      # Check if we can reach n with remaining operations by adding 1
      if operations + 1 <= n:
        operations += 1
        current = n
      else:
        # Impossible to reach n with current strategy
        return 0

  return operations
