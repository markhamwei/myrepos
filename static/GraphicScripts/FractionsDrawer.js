function drawFraction(canvasId, wholeNumber, numerator, denominator, fontSize=20) {
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

  // Calculate the position for the whole number, numerator, and denominator
  const x = width / 2;
  const y = height / 2;

  // Draw the numerator
  ctx.fillText(numerator.toString(), x, y - 15);

  // Draw the line separating the numerator and denominator
  ctx.beginPath();
  ctx.moveTo(30, y - 5);
  ctx.lineTo(width - 30, y - 5);
  ctx.stroke();

  // Draw the whole number
  if(wholeNumber > 0){
     ctx.fillText(wholeNumber.toString(), x-32, y+5);
  }

  // Draw the denominator
  ctx.fillText(denominator.toString(), x, y + 30);
}
