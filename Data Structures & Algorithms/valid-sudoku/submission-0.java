class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] squares = new int[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {

                // Non-Word
                if (board[r][c] == '.') continue;

                // Get value
                int val = board[r][c] - '1';
                
                // Check if val exists in row
                // Check if val exists in col
                // Checks if val already exists in corresponding 3x3 square
                // Computes index (0-8) of the square the cell (r, c) belongs to
                if ((rows[r] & (1 << val)) > 0 || 
                    (cols[c] & (1 << val)) > 0 || 
                    (squares[(r / 3) * 3 + (c / 3)] & (1 << val)) > 0) {
                    return false;
                }

               
                rows[r] |= (1 << val);  // Add to Row    
                cols[c] |= (1 << val);  // Add to Cols
                squares[(r / 3) * 3 + (c / 3)] |= (1 << val); // Add to Squares
            }
        }
        return true;
    }
}