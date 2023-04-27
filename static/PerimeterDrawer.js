
const DrawingScope = (function() {

	const canvasSize = 750;
	const halfSize = 375;
	var array;
	var points;
	var canvasID;
	var canvas;
	var context;

	var inputbox = document.getElementById('inputbox');
	var nextbutton = document.getElementById('nextbutton');
	var resultimg = document.getElementById('resultimgleft');
	
	// A binary search helper function
	// finds points along the circumference of a circle with a given radius
	//   such that the side lengths of the traced polygon matches up with
	//   the side lengths in the array
	function find(rad) {
		var ang = 0;
		var ret = new Array(array.length);
		for(let i = 0; i < array.length; i++) {
			let cur = Math.acos(1-array[i]*array[i]/2/rad/rad);
			ang += cur;
			ret[i] = [rad * Math.cos(ang), rad * Math.sin(ang)];
		}
		return ret;
	}

	// A binary search helper function.
	// Takes in an array of lengths and determines if it satisfies the equation
	//   sum acos(1-array[i]/2/rad) >= 2PI
	function fit(rad) {
		var ang = 0;
		for(let i = 0; i < array.length; i++) {
			let cur = 1-array[i]*array[i]/2/rad/rad;
			if(cur < -1) {
				return true;
			}
			cur = Math.acos(cur);
			ang += cur;
		}
		return ang >= 2*Math.PI;
	}
	
	// Main polygon generator function.
	// Takes in an array of integers representing lengths and the id of an html canvas item
	// If possible, draws a polygon whose side lengths match up to the array side lengths in order
	//   onto the canvas labeled by canvasID
	function drawPoly() {
		
		var highest = -1, highestidx;
		var sum = 0;
		for(let i = 0; i < array.length; i++) {
			if(array[i] > highest) {
				highest = array[i];
				highestidx = i;
			}
			sum += array[i];
		}
		if(2*highest >= sum) {
			//in this case, it's impossible to draw a polygon, so we do nothing.
			alert('An internal error has occurred. Please reload the page')
			return;
		}
		if((1+Math.PI/4)*highest >= sum) {
			specialcase(highestidx);
		}
		else {
			let minrad = sum/2/Math.PI;
			let maxrad = sum/4;
			for(let it = 0; it < 30; it++) {
				let rad = (minrad + maxrad) / 2;
				if(fit(rad)) {
					minrad = rad;
				}
				else {
					maxrad = rad;
				}
			}
			points = find(maxrad);
			//for(let i = 0; i < points.length; i++) {
			//	points[i][0] = halfSize+points[i][0]/minrad*halfSize*0.7;
			//	points[i][1] = halfSize+points[i][1]/minrad*halfSize*0.7;
			//}
			tracePoints();
		}
	}
	
	// A binary search helper function.
	// Takes in an array, the index of its highest element, and an angle value
	// returns if the sum of vectors incrementally increasing in angle by arg
	//   whose length is given by all the nonhighest elements in the array
	//   has a magnitude of less than the value of the highest element of the array
	function specialfit(idx, ang) {
		let cur = 0;
		let x = 0, y = 0;
		for(let i = idx+1; i < array.length; i++) {
			cur += ang;
			x += array[i]*Math.cos(cur);
			y += array[i]*Math.sin(cur);
		}
		for(let i = 0; i < idx; i++) {
			cur += ang;
			x += array[i]*Math.cos(cur);
			y += array[i]*Math.sin(cur);
		}
		return Math.sqrt(x*x+y*y) >= array[idx];
	}
	// Takes in an array, the index of its highest element, and an angle value
	// returns an array of vectors created by the process described in specialfit
	function specialfind(idx, ang) {
		let cur = 0;
		let x = 0, y = 0;
		let ret = new Array(array.length);
		for(let i = idx+1; i < array.length; i++) {
			cur += ang;
			x += array[i]*Math.cos(cur);
			y += array[i]*Math.sin(cur);
			ret[i] = [x, y];
		}
		for(let i = 0; i < idx; i++) {
			cur += ang;
			x += array[i]*Math.cos(cur);
			y += array[i]*Math.sin(cur);
			ret[i] = [x, y];
		}
		return ret;
	}
	
	// drawPoly delegates its task to this function under a special case
	// (1+Math.PI/4)*highest >= sum
	function specialcase(idx) {
		let minang = 0, maxang = 2*PI/(array.length-1);
		for(let it = 0; it < 30; it++) {
			let ang = (minang+maxang)/2;
			if(specialfit(idx, ang)) {
				minang = ang;
			}
			else {
				maxang = ang;
			}
		}
		points = specialfind(idx, maxang);
		//this polygon is way off center, and would appear cut off in the canvas itself.
		//Thus we translate and resize it.
		let midx = 0, midy = 0;
		for(let i = 0; i < points.length; i++) {
			midx += points[i][0];
			midy += points[i][1];
		}
		midx /= points.length; midy /= points.length;
		//let maxx = 0, maxy = 0;
		//for(let i = 0; i < points.length; i++) {
		//	points[i][0] -= midx;
		//	points[i][1] -= midy;
		//	if(points[i][0]*points[i][0]+points[i][1]*points[i][1] > maxx*maxx + maxy*maxy) {
		//		maxx = points[i][0];
		//		maxy = points[i][1];
		//	}
		//}
		//let maxlen = Math.sqrt(maxx*maxx+maxy*maxy);
		//for(let i = 0; i < points.length; i++) {
		//	points[i][0] = points[i][0]/maxlen*halfSize*0.7+halfSize;
		//	points[i][1] = points[i][1]/maxlen*halfSize*0.7+halfSize;
		//}
		tracePoints();
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
		drawLength(points[0][0], points[0][1], points[points.length-1][0], points[points.length-1][1], array[0]);
		for(let i = 1; i < points.length; i++) {
			drawLength(points[i][0], points[i][1], points[i-1][0], points[i-1][1], array[i]);
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
			let rng = Math.random();
			let len = 6;
			if(rng < 0.4) len = 3;
			else if(rng < 0.8) len = 4;
			else if(rng < 0.9) len = 5;
			array = new Array(len);
			let max = -1, maxidx = 0, sum = 0;
			for(let i = 0; i < len; i++) {
				array[i] = Math.floor(Math.random()*10+1.1);
				if(array[i] > max) {
					max = array[i];
					maxidx = i;
				}
				sum += array[i];
			}
			if(2*max >= sum) {
				array[maxidx] = sum-max-1; //this is to ensure the polygon will always be possible to draw
			}
				console.log(array); //DEBUG
			drawPoly();
		},
		
		// takes in an input box ID and a list of html IDs and sets their src to
		//   /static/smile.png or static/frown.png depending on if the answer was correct
		checkPoly: function() {
			let sum = 0;
			for(let i = 0; i < array.length; i++) {
				sum += array[i];
			}
			if(resultimg.classList.contains('hiddenimg')) {
				resultimg.classList.remove('hiddenimg');
			}
			if(inputbox.value == sum.toString()) {
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
			let sum = 0;
			for(let i = 0; i < array.length; i++) {
				sum += array[i];
			}
			inputbox.value = sum.toString();
		}
	};
})();
