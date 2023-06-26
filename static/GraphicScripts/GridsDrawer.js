function drawGrid(canvasid, rows, cols, gridx1=-1, gridy1=-1, gridx2=-1, gridy2=-1) {
  canvas = document.getElementById(canvasid);
  ctx = canvas.getContext('2d');
  cellWidth = 40
  cellHeight = 40
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const x = col * cellWidth + 30;
      const y = row * cellHeight;

      ctx.strokeRect(x, y, cellWidth, cellHeight);

	  ctx.fillStyle = "red";
	  ctx.font = "20px Arial";
      // Add labels
      if (row === rows - 1) {
        // Draw horizontal labels (A to H) below the grid
        ctx.fillText(String.fromCharCode(65 + col), x + cellWidth / 2, cellHeight * rows + (cellHeight)/2 + 5);
      }

      if (col === 0) {
        // Draw vertical labels (1 to 6) on the left side of the grid
        ctx.fillText(rows - row, x - 20, y + cellHeight / 2);
      }
	
	  if(((rows - row) == gridy1) && (col == gridx1-1)) {
		ctx.fillText("X", x + (cellWidth/2 - 5), y + cellHeight / 2 +10);
	  }
	
	  ctx.fillStyle = "green";
	  if(((rows - row) == gridy2) && (col == gridx2-1)) {
		ctx.fillText("X", x + (cellWidth/2 - 5), y + cellHeight / 2 +10);
	  }
    }
  }
}
