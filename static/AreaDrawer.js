
const AreaScope = (function() {

	const canvasSize = 750;
	const halfSize = 375;
	
	var area;
	var points; // used to draw a polygon onto the canvas
	// is of the form [A, B, C, D], where A, B, C, D are vectors that make up the following diagram for some quadrilateral
	/*
		      top
		(D)---------(C) - - -o
		 |            \      | height
		 |             \     |
		(A)------------(B)- -o
		      base
	*/
	var lengthdata; // used to draw length values onto the canvas
	// is of the form [base, height, top]

	var canvasID;
	var canvas;
	var context;

	var inputbox = document.getElementById('inputbox');
	var nextbutton = document.getElementById('nextbutton');
	var resultimg = document.getElementById('resultimgleft');

	// generatePoly helper function
	// Since all of the available polygons can be generated with the following:
	// a base dimension
	// a height dimension (ie base to top vertical offset)
	// a top length dimension
	// a base to top horizontal offset
	// This function produces a points creating a random polygon fitting
	// upper and lower bounds for the measurements
	// an additional parameter is included: topeqbase, stating whether or not the top should be forced to be equal to the base
	function generatePolyHelper(baseL, baseH, heightL, heightH, topL, topH, offsetL, offsetH, topeqbase=false) {
		let base = Math.floor(Math.random()*(baseH-baseL)+baseL);
		let height = Math.floor(Math.random()*(heightH-heightL)+heightL);
		let top = Math.floor(Math.random()*(topH-topL)+topL);
		if(topeqbase) {top = base;}
		let offset = Math.floor(Math.random()*(offsetH-offsetL)+offsetL);
		area = (base+top)*height/2;
		lengthdata = [base, height, top];
		points = new Array(4);
		points[0] = [0,0];
		points[1] = [base,0];
		points[2] = [top+offset, -height];
		points[3] = [offset, -height];
	}
	
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
		drawLength(points[0][0], points[0][1], points[1][0], points[1][1], lengthdata[0]);
		
		//draw height line if the shape doesnt have a vertical D to A line
		if(points[0][0] != points[3][0]) {
			let x = Math.min(points[0][0],points[3][0])-30, y1 = points[0][1], y2 = points[3][1];

			context.beginPath();
			context.moveTo(x-15, y1); context.lineTo(x+15, y1);
			context.moveTo(x-15, y2); context.lineTo(x+15, y2);
			context.closePath();
			context.stroke();
	
			context.beginPath();
			context.setLineDash([15,15]);
			context.moveTo(x, y1);
			context.lineTo(x, y2);
			context.closePath();
			context.stroke();

			drawLength(x, y2, x, y1, lengthdata[1]);
		}
		else { //otherwise just draw the length like a sane person
			drawLength(points[3][0], points[3][1], points[0][0], points[0][1], lengthdata[1]);
		}

		if(lengthdata[2] > 0) {
			drawLength(points[2][0], points[2][1], points[3][0], points[3][1], lengthdata[2]);
		}
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
			
			let rng = Math.floor(Math.random()*4);
			if(rng == 0) generatePolyHelper(1, 15, 1, 10, 0, 0, -7, 7); //triangle
			if(rng == 1) generatePolyHelper(1, 15, 1, 15, 0, 0, 0, 0, topeqbase=true); //rectangle
			if(rng == 2) generatePolyHelper(1, 15, 1, 15, 0, 0, -7, 7, true); //paralellogram
			if(rng == 3) generatePolyHelper(1, 15, 1, 10, 1, 15, -6, 6); //trapezoid

			console.log(lengthdata);

			tracePoints();
		},
		
		// takes in an input box ID and a list of html IDs and sets their src to
		//   /static/smile.png or static/frown.png depending on if the answer was correct
		checkPoly: function() {
			
			if(resultimg.classList.contains('hiddenimg')) {
				resultimg.classList.remove('hiddenimg');
			}
			if(!isNaN(inputbox.value) && Math.abs(parseFloat(inputbox.value)-area)<1e-5) {
				resultimg.setAttribute('src', '/static/smile.png');
				if(nextbutton.hasAttribute('disabled')) {
					nextbutton.toggleAttribute('disabled');
				}
			}
			else {
				resultimg.setAttribute('src', '/static/frown.png');
			}
		},

		// takes in an input box ID and sets its value to the correct answer
		showSolution: function() {
			inputbox.value = area.toString();
		}
	};
})();
