def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to n rows.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists containing the values of Pascal's triangle.
  """
  if n <= 0:
    return []  # Return empty list for non-positive n

  triangle = [[1]]  # Initialize with first row (1)

  for i in range(1, n):
    next_row = [1]
    for j in range(1, i):
      prev_row = triangle[i-1]
      next_row.append(prev_row[j-1] + prev_row[j])
    next_row.append(1)
    triangle.append(next_row)

  return triangle
