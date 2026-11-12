# Search Engine

A Python implementation of a **2D range tree** for the *Search Nearby* use case in Google Maps. The project stores a set of two-dimensional points and supports queries that return all points within a given (L_\infty)-distance of a query point.

This is an academic data-structures project. The implementation is contained in `search.py`.

## Problem

Suppose a map contains a large set of locations. Scanning every location for every nearby-search request takes (O(n)) time per query. A spatial data structure can preprocess the points so that queries can avoid examining the entire dataset.

Given:
- A set of points (S\subseteq\mathbb{R}^2)
- A query point (q=(q_x,q_y))
- A non-negative distance (d)

The task is to return every point (p\in S) whose (L_\infty)-distance from (q) is at most (d).

The (L_\infty)-distance between two points (p_1=(x_1,y_1)) and (p_2=(x_2,y_2)) is:

```text
||p1 - p2||∞ = max(|x1 - x2|, |y1 - y2|)
```

Therefore, a point is returned when both conditions hold:

```text
qx - d <= x <= qx + d
qy - d <= y <= qy + d
```

Geometrically, the query searches the axis-aligned square centered at (q), with side length (2d).

## Data Structure

The project implements a **range tree** to organize the input points for spatial queries.

The `PointDatabase` class provides:
- A constructor that preprocesses a list of two-dimensional points into the range-tree representation.
- A `searchNearby` method that searches the represented points for those inside the query square.

The implementation maintains point data ordered by coordinate and uses associated Y-ordered point collections while traversing the range-tree structure.

## API

### `PointDatabase(pointlist)`

Constructs a database from a list of coordinate pairs.

- **Input:** `pointlist`, a list of `(x, y)` points.
- **Purpose:** Builds the range-tree representation used by subsequent queries.

### `searchNearby(q, d)`

Returns the points whose (L_\infty)-distance from query point `q` is at most `d`.

- **Input:** `q`, a query point `(qx, qy)`; `d`, a non-negative distance.
- **Output:** A list of matching points. The order of returned points is arbitrary.

## Usage

```python
from search import PointDatabase

points = [
    (1, 6),
    (2, 4),
    (3, 7),
    (4, 9),
    (5, 1),
    (6, 3),
    (7, 8),
    (8, 10),
    (9, 2),
    (10, 5),
]

database = PointDatabase(points)

nearby_points = database.searchNearby((5, 5), 1)
print(nearby_points)
```

The example constructs a point database and queries for points within (L_\infty)-distance 1 of `(5, 5)`.

## Complexity Requirements

The assignment specifies the following target time complexities:

| Operation | Required complexity |
|---|---:|
| Preprocessing / construction | (O(n\log n)) |
| `searchNearby(q, d)` | (O(m + \log^2 n)) |

Here:
- (n) is the number of points stored in the database.
- (m) is the number of points returned by a query.

These are the complexity requirements specified for the assignment; this README does not present them as independently benchmarked performance measurements.

## Input Assumptions

The assignment defines the following assumptions:

1. Point coordinates are integers.
2. No two input points share the same X-coordinate.
3. No two input points share the same Y-coordinate.
4. No input point is at exactly distance (d) from the query point under the (L_\infty) metric.

## Testing

The implementation was run against the test cases provided by the course instructor. The project was developed and evaluated in the context of the assigned problem specification.

## Repository Structure

```text
Search-Engine/
├── README.md
└── search.py
```

## Concepts

- Two-dimensional range searching
- Range trees and associated structures
- Spatial queries
- (L_\infty) distance
- Preprocessing for efficient query operations
- Python data structures and recursion

## Project Context

Developed as an academic data-structures project at **IIT Delhi**. The problem models the spatial-search behavior behind a map application's “Search Nearby” feature.
