"""
    Explain with the runtime analysis on each method you have implemented in each of the representation using Big-O notation

	If the graph have n nodes and m edges, then
		For the Adjacency Matrix:
			Nodes
			The time to check one node is O(1), so time to check all n nodes is n*O(1) = O(n)
			The time to check one edge connect to a node is O(1), so total time to iterate over edges incident to nodes is m*O(1) = O(m)
			Total time need is: O(n + m)

		For Adjacency Matrix:
			The time to check one node is O(1), and Matrix size is n x n, so time to check all the node is n x n x O(1) = O(n^2)
			Total time is O(n^2)

		For ObjectedOriented:
			The time to check one node is O(1), so time to check all n nodes is n*O(1) = O(n)
			The time to check one edge is O(1), so total time to iterate all the edges is m*O(1) = O(m)
			Total time need is: O(n + m)


    Consider Chess, what is the performance measure, environment, actuator and sensor?
	    performance measure:
            protect the one's king safe, attack and capture the opponent's pieces, especially the opponent's king in order to win the game. make a move fast.
	    environment:
            gameboard with 64 squares arranged in an 8×8 grid, the position and the posibility of the move of the opponent's pieces (initial 16 pieces).The colors of the 64 squares alternate and are referred to as light and dark squares.
	    actuator:
            move the pieces so that they can block the move and attack the opponent's pieces, especially the king, meanwhile, protecting its own king.
	    sensor:
            the position and all the move that each piece can make.


    Same with Chess, formulate the problem in 5 components (initial state, possible actions, transition model, goal test, and path cost)

        initial state:
            Each player begins with 16 pieces: one king, one queen, two rooks, two knights, two bishops, and eight pawns
        possible actions:
            Each of the six piece types moves differently, with the most powerful being the queen and the least powerful the pawn.

            The king moves one square in any direction. The king also has a special move called castling that involves also moving a rook.
            The rook can move any number of squares along a rank or file, but cannot leap over other pieces. Along with the king, a rook is involved during the king's castling move.
            The bishop can move any number of squares diagonally, but cannot leap over other pieces.
            The queen combines the power of a rook and bishop and can move any number of squares along a rank, file, or diagonal, but cannot leap over other pieces.
            The knight moves to any of the closest squares that are not on the same rank, file, or diagonal, thus the move forms an "L"-shape: two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The knight is the only piece that can leap over other pieces.
            The pawn can move forward to the unoccupied square immediately in front of it on the same file, or on its first move it can advance two squares along the same file, provided both squares are unoccupied (black dots in the diagram); or the pawn can capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square (black "x"s). A pawn has two special moves: the en passant capture and promotion.

        transition model:
             Given state, the position, the possible move and the action that the opponent could make, the player will make a move.
        goal test:
            Block or attack the opponent'king in the check.
        path cost:
            Each move would cost 1

    Define Chess environment type, is it fully observable or partially observable, is it deterministic or stochastic, is it discrete or continuous, is it benign or adversarial?

        The Chess environment is fully observable
            since agent can fully observe all variables of environment.
        It is deterministic
            since there is no random effects,each moves determines next state deterministically
        It is discrete
            since Number of states in games is countable.
        It is adversarial.
            since Environment goes against you.
"""
