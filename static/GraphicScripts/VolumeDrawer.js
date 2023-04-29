
const VolumeScope = (function() {

	const canvasSize = 750;
	const halfSize = 375;
	
	var volume;
	var points;

	var canvasID;
	var canvas;
	var context;

	var inputbox = document.getElementById('inputbox');
	var nextbutton = document.getElementById('nextbutton');
	var resultimg = document.getElementById('resultimgleft');

	
	
	// tracePoints helperfunction
	// postprocess: centralizes the polygon on the screen and scales the polygon appropriately
	//   (should reach at most 70% of the canvas)
	function centralizePoints() {
		let sumx = 0, sumy = 0;
		for(let i = 0; i < points.length; i++) {
			sumx += points[i][0];
			sumy += points[i][1];
		}
		sumx /= points.length;
		sumy /= points.length;
		let maxdist = 0;
		for(let i = 0; i < points.length; i++) {
			points[i][0] -= sumx;
			points[i][1] -= sumy;
			if(points[i][0]*points[i][0]+points[i][1]*points[i][1]>maxdist) {
				maxdist = points[i][0]*points[i][0]+points[i][1]*points[i][1];
			}
		}
		maxdist = Math.sqrt(maxdist);
		for(let i = 0; i < points.length; i++) {
			points[i][0] = halfSize + points[i][0]/maxdist*halfSize*0.7;
			points[i][1] = halfSize + points[i][1]/maxdist*halfSize*0.7;
		}
	}

	// Helper function
	// given a line and an integer, draws the integer beside the midpoint at a fixed distance of 45 pixels
	//   perpendicular to the line
	function drawLength(x1, y1, x2, y2, val) {
		let dx = y1-y2, dy = x2-x1;
		let d = Math.sqrt(dx*dx+dy*dy);
		dx*=45/d; dy*=45/d;
		context.fillText(val.toString(), (x1+x2)/2+dx-6, (y1+y2)/2+dy+3);
	}
	
	// Function to draw onto the canvas.
	// Takes in an array of 2d vectors, each vector representing a point, and a canvas ID
	// Resizes the canvas to canvasSizexcanvasSize and the polygon onto the canvas
	// Additionally draws the side lengths of the polygons
	function tracePoints() {

		centralizePoints();

		canvas = document.getElementById(canvasID);
		canvas.setAttribute('width', canvasSize.toString());
		canvas.setAttribute('height', canvasSize.toString());

		context = canvas.getContext('2d');
		context.clearRect(0, 0, canvas.width, canvas.height);
		context.beginPath();

		context.moveTo(points[0][0], points[0][1]);
		for(let i = 1; i < points.length; i++) {
			context.lineTo(points[i][0], points[i][1]);
		}

		context.closePath();
		context.stroke();


		context.font='35px verdana';
		
	}
	return {

		// Takes in a canvasID
		// resizes the canvas to canvasSizexcanvasSize and draws a random polygon on it.
		// resets the nextbutton element
		// clears the perimeter textbox
		// hides the result face
		generatePoly: function(cID) {
			
			//reset html elements
			if(!nextbutton.hasAttribute('disabled')) {
				nextbutton.toggleAttribute('disabled');
			}
			inputbox.value = "";
			if(!resultimg.classList.contains('hiddenimg')) {
				resultimg.classList.add('hiddenimg');
			}

			canvasID = cID;
			
			

			tracePoints();
		},
		
		// takes in an input box ID and a list of html IDs and sets their src to
		//   /static/img/smile.png or static/img/frown.png depending on if the answer was correct
		checkPoly: function() {
			
			if(resultimg.classList.contains('hiddenimg')) {
				resultimg.classList.remove('hiddenimg');
			}
			if(!isNaN(inputbox.value) && Math.abs(parseFloat(inputbox.value)-volume)<1e-5) {
				resultimg.setAttribute('src', '/static/img/smile.png');
				if(nextbutton.hasAttribute('disabled')) {
					nextbutton.toggleAttribute('disabled');
				}
			}
			else {
				resultimg.setAttribute('src', '/static/img/frown.png');
			}
		},

		// takes in an input box ID and sets its value to the correct answer
		showSolution: function() {
			inputbox.value = volume.toString();
		}
	};
})();
