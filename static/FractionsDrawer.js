function drawFraction(cavasId, numerator, denominator, fontSize=20) {
  // Get the canvas element
  var canvas = document.getElementById(cavasId);
  
  // Get the context of the canvas
  var ctx = canvas.getContext('2d');
  
  // Set the font size and style
  ctx.font = fontSize+"px Arial";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  
  // Draw the numerator and denominator
  ctx.fillText(numerator, 25, 30);
  ctx.fillText(denominator, 25, 70);
  
  // Draw the fraction line
  ctx.beginPath();
  ctx.moveTo(10, 47);
  ctx.lineTo(40, 47);
  ctx.stroke();
}