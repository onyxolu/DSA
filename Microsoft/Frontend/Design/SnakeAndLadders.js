// We will have four classes (Models)

// Player
// Snake
// Ladder
// SnakeAndLadderBoard

class Snake {
  start; // int
  end; // int
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  getStart() {
    return this.start;
  }

  getEnd() {
    return this.end;
  }
}

class Ladder {
  start; // int
  end; // int
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  getStart() {
    return this.start;
  }

  getEnd() {
    return this.end;
  }
}

class Player {
  name; // string
  id; // string
  constructor(name) {
    this.name = name;
    this.id = uuid.generate();
  }

  getName() {
    return this.name;
  }

  getId() {
    return this.id;
  }
}

class SnakeAndLadderBoard {
  size; //int
  snakes; // array of snakes => Snake[]
  ladders; // array of ladders => Ladder[]
  playerPieces; // object
  constructor(size) {
    this.size = size;
    this.snakes = [new Snake()]; // array of snakes => Snake[]
    this.ladders = [new Ladder()]; // array of ladders => Ladder[]
    this.playerPieces = {};
  }

  getSize() {
    return this.size;
  }

  //snakes
  getSnakes() {
    return this.snakes;
  }

  setSnakes(snakes) {
    // Snake[]
    this.snakes = snakes;
  }

  // ladders
  getLadders() {
    return this.ladders;
  }

  setLadders(ladders) {
    // Ladder[]
    this.ladders = ladders;
  }

  // playerPieces
  getPlayerPieces() {
    return this.playerPieces;
  }

  setPlayerPieces(playerPieces) {
    this.playerPieces = playerPieces;
  }
}

// Services

// DiceService
// SnakeAndLadderService
// Game

class DiceService {
  roll() {
    return Math.floor(Math.random() * max) + 1;
  }
}

class SnakeAndLadderService {
  snakeAndLadderBoard;
  initialNoOfPlayers; // int
  players; // Comment: Keeping players in game service as they are specific to this game and not the board. Keeping pieces in the board instead.
  isGameCompleted; // bool
  // optional
  noOfDices; // int
  shouldGameContinueTillLastPlayer; // bool
  shouldAllowMultipleDiceRollOnSix; // bool
  // static
  static DEFAULT_BOARD_SIZE = 36;
  static DEFAULT_NO_OF_DICES = 1;

  constructor(boardSize) {
    this.snakeAndLadderBoard = new this.snakeAndLadderBoard(boardSize);
    this.players = []; // players[]
    this.noOfDices = SnakeAndLadderService.DEFAULT_NO_OF_DICES;
  }

  // Setters

  setNoOfDices(noOfDices) {
    this.noOfDices = noOfDices;
  }

  setShouldGameContinueTillLastPlayer(shouldGameContinueTillLastPlayer) {
    // bool
    this.shouldGameContinueTillLastPlayer = shouldGameContinueTillLastPlayer;
  }

  setShouldAllowMultipleDiceRollOnSix(shouldAllowMultipleDiceRollOnSix) {
    this.shouldAllowMultipleDiceRollOnSix = shouldAllowMultipleDiceRollOnSix;
  }

  /**
   * ==================Initialize board==================
   */

  setPlayers(players) {
    this.initialNoOfPlayers = players.length;
    let playerPieces = {};
    let playersCopy = this.players;
    players.forEach((player) => {
      playersCopy.push(player);
      playerPieces[player.getId()] = 0;
    });
    snakeAndLadderBoard.setPlayerPieces(playerPieces);
  }

  setSnakes(snakes) {
    snakeAndLadderBoard.setSnakes(snakes); // Add snakes to board
  }

  setLadders(ladders) {
    this.snakeAndLadderBoard.setLadders(ladders);
  }

  /**
   * ==========Core business logic for the game==========
   */
  movePlayer(player, positions) {
    let oldPosition = snakeAndLadderBoard.getPlayerPieces()[player.getId()];
    let newPosition = oldPosition + positions; // Based on the dice value, the player moves their piece forward that number of cells.
    let boardSize = snakeAndLadderBoard.getSize();
    // Can modify this logic to handle side case when there are multiple dices (Optional requirements)
    if (newPosition > boardSize) {
      newPosition = oldPosition; // After the dice roll, if a piece is supposed to move outside position 100, it does not move.
    } else {
      newPosition =
        getNewPositionAfterGoingThroughSnakesAndLadders(newPosition);
    }

    snakeAndLadderBoard.getPlayerPieces()[player.getId()] = newPosition;

    console.log(
      player.getName() +
        " rolled a " +
        positions +
        " and moved from " +
        oldPosition +
        " to " +
        newPosition
    );
  }

  getNewPositionAfterGoingThroughSnakesAndLadders(newPosition) {
    let previousPosition;
    while (newPosition != previousPosition) {
      // There could be another snake/ladder at the tail of the snake or the end position of the ladder and the piece should go up/down accordingly.
      previousPosition = newPosition;
      snakeAndLadderBoard.getSnakes().forEach((snake) => {
        if (snake.getStart() == newPosition) {
          newPosition = snake.getEnd(); // Whenever a piece ends up at a position with the head of the snake, the piece should go down to the position of the tail of that snake.
        }
      });

      snakeAndLadderBoard.getLadders().forEach((ladder) => {
        if (ladder.getStart() == newPosition) {
          newPosition = ladder.getEnd(); // Whenever a piece ends up at a position with the start of the ladder, the piece should go up to the position of the end of that ladder.
        }
      });
    }
    return newPosition;
  }

  getTotalValueAfterDiceRolls() {
    // Can use noOfDices and setShouldAllowMultipleDiceRollOnSix here to get total value (Optional requirements)
    return DiceService.roll();
  }

  hasPlayerWon(player) {
    const playerPosition =
      this.snakeAndLadderBoard.getPlayerPieces()[player.getId()];
    const winningPosition = this.snakeAndLadderBoard.getSize();
    return playerPosition == winningPosition;
  }

  isGameCompleted() {
    // Can use shouldGameContinueTillLastPlayer to change the logic of determining if game is completed (Optional requirements)
    let currentNoOfPlayers = this.players.length;
    return currentNoOfPlayers < this.initialNoOfPlayers;
  }

  startGame() {}
}

class Game {}
