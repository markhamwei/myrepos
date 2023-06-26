function drawSpinner(canvasid, myarray) {
	const colors = ["#808080", "green", "blue", "Magenta", "#B4B400", "purple", "orange", "cyan"]
    const canvas = document.getElementById(canvasid);
    const ctx = canvas.getContext("2d");

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) - 10;

    const numSlices = myarray.length;
    const sliceAngle = (2 * Math.PI) / numSlices;

    for (let i = 0; i < numSlices; i++) {
      const startAngle = i * sliceAngle - Math.PI / 2;
      const endAngle = (i + 1) * sliceAngle - Math.PI / 2;

      ctx.beginPath();
      ctx.arc(centerX, centerY, radius, startAngle, endAngle);
      ctx.lineWidth = 1;
      ctx.strokeStyle = "green";
      ctx.stroke();

	  ctx.strokeStyle = 'white'
      ctx.lineTo(centerX, centerY);
	  ctx.stroke();
	  ctx.fillStyle = colors[myarray[i]-1];
      ctx.fill();
	  ctx.stroke();

      // Calculate the position to write the slice number
      const textRadius = radius * 0.75;
      const textAngle = (startAngle + endAngle) / 2;
      const textX = centerX + textRadius * Math.cos(textAngle);
      const textY = centerY + textRadius * Math.sin(textAngle);

      // Write the slice number inside the slice
	  ctx.font = "35px Arial";
	  displayNumber = myarray[i];
      ctx.fillStyle = "white";
	  if(i < 9)
		ctx.fillText(displayNumber, textX, textY);
	  else
		ctx.fillText(displayNumber, textX-20, textY);
    }
	ctx.beginPath();
	pointerX = canvas.width / 2;
	pointerY = canvas.height / 8;
	ctx.moveTo(pointerX, pointerY);
	pointerRadius = radius / 4;
	pointerAngle = (2 * Math.PI) / 16;
	pointerStartAngle = -(pointerAngle/2 + Math.PI / 2);
	pointerEndAngle = pointerAngle/2 - Math.PI / 2;
	ctx.arc(pointerX, pointerY, pointerRadius, pointerStartAngle, pointerEndAngle);
	ctx.closePath();
	ctx.lineWidth = 2;
	ctx.fillStyle = 'red'
    ctx.fill();
}
