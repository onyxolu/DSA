
class Edge {

    enum Type {

        inner, outer, flat

    }

  

    Piece parent;

    Type type;

  

    boolean fitsWith(Edge type) {

    }; // Inners & outer fit together.

}

  

class Piece {

    Edge left, right, top, bottom;

  

    // 90, 180, etc

    Orientation solvedOrientation = 90;

}

  

class Puzzle {

    // Remaining pieces left to put away.

    Piece[][] pieces;

    Piece[][] solution;

    Edge[] inners, outers, flats;

  

    // We're going to solve this by working our way

    // in-wards, starting with the corners.

    // This is a list of the inside edges.

    Edge[] exposed_edges;

  

    void sort() {

  

        // Iterate through all edges,

        // adding each to inners, outers, etc,

        // as appropriate.

        // Look for the corners—add those to solution.

        // Add each non-flat edge of the corner

        // to exposed_edges.

  

    }

  

    void solve() {

        for (Edge edge1 : exposed_edges) {

            // Look for a match to edge1

            if (edge1.type == Edge.Type.inner) {

                for (Edge edge2 : outers) {

                    if (edge1.fitsWith(edge2)) {

                        // We found a match!

                        // Remove edge1 from

                        // exposed_edges.

                        // Add edge2's piece

                        // to solution.

                        // Check which edges of edge2

                        // are exposed, and add

                        // those to exposed_edges.

                    }

                }

                // Do the same thing,

                // swapping inner & outer.

            }

        }

    }

}