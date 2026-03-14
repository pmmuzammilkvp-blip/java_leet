var solveSudoku = function(board) {

    function isValid(board, row, col, num) {

        for (let i = 0; i < 9; i++) {

            // check row
            if (board[row][i] === num) return false;

            // check column
            if (board[i][col] === num) return false;

            // check 3x3 box
            let boxRow = 3 * Math.floor(row / 3) + Math.floor(i / 3);
            let boxCol = 3 * Math.floor(col / 3) + (i % 3);

            if (board[boxRow][boxCol] === num) return false;
        }

        return true;
    }

    function backtrack() {

        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {

                if (board[r][c] === ".") {

                    for (let num = 1; num <= 9; num++) {

                        let char = num.toString();

                        if (isValid(board, r, c, char)) {

                            board[r][c] = char;

                            if (backtrack()) return true;

                            board[r][c] = "."; // backtrack
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    backtrack();
};
