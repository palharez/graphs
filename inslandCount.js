const islandCount = (grid) => {
  const visited = new Set();

  let count = 0;

  for (let r = 0; r < grid.length; r += 1) {
    for (let c = 0; r < grid[r].length; c += 1) {
      if (explore(grid, r, c, visited) === true) {
        count += 1;
      }
    }
  }

  return count;
};

const explore = (grid, r, c, visited) => {
  const rowInBounds = r >= 0 && r < grid.length;
  const colInBounds = c >= 0 && c < grid.length;

  if (!rowInBounds || !colInBounds) return false;

  if (grid[r][c] == "W") return false;

  const pos = r + "," + c;

  if (visited.has(pos)) return false;

  visited.add(pos);

  explore(grid, r - 1, c, visited);
  explore(grid, r + 1, c, visited);
  explore(grid, r, c - 1, visited);
  explore(grid, r, c + 1, visited);

  return true;
};
