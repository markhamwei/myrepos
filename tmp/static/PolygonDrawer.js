
const DrawingScope = (function() {
	
	// A binary search helper function
	// 
	function find(array, rad) {
		var ang = 0;
		var ret = new Array(array.length);
		for(let i = 0; i < array.length; i++) {
			let cur = Math.acos(1-array[i]/2/rad);
			ang += cur;
			ret[i] = [rad * Math.cos(ang), rad * Math.sin(ang)];
		}
		return ret;
	}

	// A binary search helper function.
	// Takes in an array of lengths and determines if it satisfies the equation
	//   sum acos(1-array[i]/2/rad) >= 2PI
	function fit(array, rad) {
		var ang = 0;
		for(let i = 0; i < array.length; i++) {
			let cur = Math.acos(1-array[i]/2/rad);
			ang += cur;
		}
		return ang >= 2*Math.PI;
	}
	
	// Main polygon generator function.
	// Takes in an array of integers representing lengths and the id of an html canvas item
	// If possible, draws a polygon whose side lengths match up to the array side lengths in order
	//   onto the canvas labeled by canvasID
	function drawPoly(array, canvasID) {
		
		var highest = -1, highestidx;
		var sum = 0;
		for(let i = 0; i < array.length; i++) {
			if(array[i] > highest) {
				highest = array[i];
				highestidx = i;
			}
			sum += array[i];
		}
		console.log(highest);
		console.log(highestidx);
		console.log(sum);
		if(2*highest >= sum) {
			//in this case, it's impossible to draw a polygon, so we do nothing.
			console.log('impossible');
			return;
		}
		if((1+Math.PI/4)*highest >= sum) {
			specialcase(array, highestidx, canvasID);
		}
		else {
			let minrad = sum/2/Math.PI;
			let maxrad = sum/4;
			for(let it = 0; it < 30; it++) {
				let rad = (minrad + maxrad) / 2;
				if(fit(array, rad)) {
					minrad = rad;
				}
				else {
					maxrad = rad;
				}
			}
			let poly = find(array, minrad);
			for(let i = 0; i < poly.length; i++) {
				poly[i][0] = 200+poly[i][0]/minrad*150;
				poly[i][1] = 200+poly[i][1]/minrad*150;
			}
			tracePoints(poly, canvasID);
		}
	}
	
	// A binary search helper function.
	// Takes in an array, the index of its highest element, and an angle value
	// returns if the sum of vectors incrementally increasing in angle by arg
	//   whose length is given by all the nonhighest elements in the array
	//   has a magnitude of less than the value of the highest element of the array
	function specialfit(array, idx, ang) {
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
	function specialfind(array, idx, ang) {
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
	
	function specialcase(array, idx, canvasID) {
		let minang = 0, maxang = 2*PI/(array.length-1);
		for(let it = 0; it < 30; it++) {
			let ang = (minang+maxang)/2;
			if(specialfit(array, idx, ang)) {
				minang = ang;
			}
			else {
				maxang = ang;
			}
		}
		let poly = specialfind(array, idx, maxang);
		//this polygon is way off center, and would appear cut off in the canvas itself.
		//Thus we translate and resize it.
		let midx = 0, midy = 0;
		for(let i = 0; i < poly.length; i++) {
			midx += poly[i][0];
			midy += poly[i][1];
		}
		midx /= poly.length; midy /= poly.length;
		let maxx = 0, maxy = 0;
		for(let i = 0; i < poly.length; i++) {
			poly[i][0] -= midx;
			poly[i][1] -= midy;
			if(poly[i][0]*poly[i][0]+poly[i][1]*poly[i][1] > maxx*maxx + maxy*maxy) {
				maxx = poly[i][0];
				maxy = poly[i][1];
			}
		}
		let maxlen = Math.sqrt(maxx*maxx+maxy*maxy);
		for(let i = 0; i < poly.length; i++) {
			poly[i][0] = poly[i][0]/maxlen*200+200;
			poly[i][1] = poly[i][1]/maxlen*200+200;
		}
		tracePoints(poly, canvasID);
	}
	
	// Function to draw onto the canvas.
	// Takes in an array of 2d vectors, each vector representing a point, and a canvas ID
	// Resizes the canvas to 400x400 and the polygon onto the canvas
	function tracePoints(points, canvasID) {
		var canvas = document.getElementById(canvasID);
		canvas.setAttribute('width', '400');
		canvas.setAttribute('height', '400');
		var context = canvas.getContext('2d');
			console.log(points); //DEBUG
		context.clearRect(0, 0, canvas.width, canvas.height);
		context.beginPath();
		context.moveTo(points[0][0], points[0][1]);
		for(let i = 1; i < points.length; i++) {
			context.lineTo(points[i][0], points[i][1]);
		}
		context.closePath();
		context.stroke();
	}
	return {
		// The only public function.
		// Takes in a canvasID
		// resizes the canvas to 400x400 and draws a random polygon on it.
		generatePoly: function(canvasID) {
			let len = 3;
			let arr = new Array(len);
			for(let i = 0; i < len; i++) arr[i] = Math.floor(Math.random()*10+1.1)*10;
				console.log(arr); //DEBUG
			drawPoly(arr, canvasID);
		}
	};
})();