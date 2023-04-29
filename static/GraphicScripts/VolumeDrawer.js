
const VolumeScope = (function() {

	const canvasSize = 750;
	const halfSize = 375;
	
	var volume;
	var lengthdata; // [length, base, height]
	// length is drawn from C (2) to B (1)
	// base is drawn from G (6) to F (5)
	// height is drawn from B (1) to G (6)
	var lengthdraw = [[2,1],[6,5],[1,6]];
	var points; // [A B C D E F G] where the 7 points make up the following diagram
	/*  
	      __(C)-----(D)
	  __--    __--   |
	(B)-----(A)      |
	 |       |       |
	 |       |    __(E)
	 |       |__--
	(G)-----(F)
	*/
	var axismask = [[1,1,1],[1,0,1],[0,0,1],[0,1,1],[0,1,0],[1,1,0],[1,0,0]];
	// if we were a perfect cube, then points=axismask (before projecting)

	var cameraYaw = Math.PI/4; // yaw of camera
	var tickselapsed = 0; //number of times drawPrism was called

	var canvasID;
	var canvas;
	var context;

	var inputbox = document.getElementById('inputbox');
	var nextbutton = document.getElementById('nextbutton');
	var resultimg = document.getElementById('resultimgleft');

	// takes in 2 matrices of dimensions nxm and mxr
	// returns the product of those two matrices (nxr)
	function matrixmult(A, B) {
		let C = new Array(A.length);
		for(let i = 0; i < A.length; i++) {
			C[i] = new Array(B[0].length);
			for(let i2 = 0; i2 < B[0].length; i2++) {
				C[i][i2] = 0;
				for(let i3 = 0; i3 < B.length; i3++) {
					C[i][i2] += A[i][i3] * B[i3][i2];
				}
			}
		}
		return C;
	}

	// takes in 3 numbers - a point in 3d space
	// x and y are horizontal axes, z is vertical axis
	// takes in 2 angles - the yaw and pitch we wish to rotate by
	// returns the point's rotation
	function rotate(x, y, z, yaw, pitch) {
		let V = matrixmult(matrixmult(
			[
				[Math.cos(pitch),0,Math.sin(pitch)],
				[0,1,0],
				[-Math.sin(pitch),0,Math.cos(pitch)]
			],
			[
				[Math.cos(yaw),-Math.sin(yaw),0],
				[Math.sin(yaw),Math.cos(yaw),0],
				[0,0,1]
			]
		),
		[[x],[y],[z]]
		);
		return [V[0][0],V[1][0],V[2][0]];
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

		context.moveTo(points[6][0], points[6][1]);
		for(let i = 1; i < points.length; i++) {
			context.lineTo(points[i][0], points[i][1]);
		}

		for(let i = 1; i < points.length; i+=2) {
			context.moveTo(points[0][0],points[0][1]);
			context.lineTo(points[i][0],points[i][1]);
		}

		context.closePath();
		context.stroke();


		context.font='35px verdana';
		
		for(let i = 0; i < 3; i++) {
			drawLength(points[lengthdraw[i][0]][0],points[lengthdraw[i][0]][1],points[lengthdraw[i][1]][0],points[lengthdraw[i][1]][1], lengthdata[i]);
		}
	}
	return {

		// generatePoly helper function
		// extrapolates lengthdata to points in 3 dimensions and draws them onto the canvas
		// additionally updates yaw slightly
		drawPrism: function() {

			tickselapsed += 1;

			points = new Array(axismask.length);
			for(let i = 0; i < axismask.length; i++) {
				points[i] = new Array(3);
				for(let i2 = 0; i2 < 3; i2++) points[i][i2] = axismask[i][i2]*lengthdata[i2];
				points[i] = rotate(points[i][0],points[i][1],points[i][2],-cameraYaw+Math.sin(tickselapsed/100)/10,Math.PI/10);
				points[i] = [points[i][1], -points[i][2]];
			}

			tracePoints();
		},

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
			
			lengthdata = [
				Math.floor(Math.random()*10)+1,
				Math.floor(Math.random()*10)+1,
				Math.floor(Math.random()*10)+1
			]
			volume = lengthdata[0]*lengthdata[1]*lengthdata[2];

			setInterval(() => {
				this.drawPrism();
			}, 50);
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
