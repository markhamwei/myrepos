// Function to convert degrees to radians
function degreesToRadians(degrees) {
	return (degrees * Math.PI) / 180;
}

// Function to draw an angle in anti-clockwise direction by degree
function drawAngleByDegree(canvasId, startX, startY, radius, startDegree, endDegree, fontSize) {
	var startAngle = degreesToRadians(startDegree);
	var endAngle = degreesToRadians(360-endDegree);
	var textEndAngle = degreesToRadians(endDegree);

	var canvas = document.getElementById(canvasId);
	var ctx = canvas.getContext("2d");

	ctx.beginPath();
	ctx.moveTo(startX, startY);
	ctx.arc(startX, startY, radius, endAngle, startAngle, false); // set the last argument to "true" for anti-clockwise
	ctx.lineTo(startX, startY);
	ctx.closePath();

	// Customize the angle appearance
	ctx.lineWidth = 1;
	ctx.strokeStyle = "black";
	ctx.fillStyle = "white";

	ctx.fill();
	ctx.stroke();

	// Draw degree labels
	ctx.fillStyle = "red";
	ctx.font = fontSize+"px Arial";
	//ctx.fillText(startDegree + "бу", startX + 10, startY);
	ctx.fillText(endDegree + "\xB0", startX + radius * Math.cos(textEndAngle/2), startY - radius * Math.sin(textEndAngle/2));
}
