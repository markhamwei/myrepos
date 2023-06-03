function drawDecimal(canvasId, decimal, fontSize=20) {
  // Get the canvas element
  const canvas = document.getElementById(canvasId);
  if (!canvas.getContext) {
    console.error('Canvas is not supported in this browser.');
    return;
  }

  // Get the canvas context
  const ctx = canvas.getContext('2d');

  // Set the font and text alignment
  ctx.font = fontSize+'px Arial';
  ctx.textAlign = 'center';

  // Calculate the width and height of the canvas
  const width = canvas.width;
  const height = canvas.height;

  // Calculate the position to draw decimal
  const x = width / 2;
  const y = height / 2;

  // Draw the decimal
  ctx.fillText(decimal, x, y);
}
