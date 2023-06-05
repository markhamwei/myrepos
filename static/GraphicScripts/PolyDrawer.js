const PolyDrawer = (function() {

	/*
	Raw point data drawn onto a canvas is nearly useless. The points must be scaled and translated in appropriate accordance to the
	dimensions of the canvas in order to draw a clear picture. 

	This function takes in points and a canvas and then calibrates the scaling/translating operators to fit the points into the canvas

	returns the scaling/translating function
	*/
	function calibrate(points, canvas) {
		var min_x = 1e7, min_y = 1e7, max_x = -1e7, max_y = -1e7;
		for(var i = 0; i < points.length; i++) {
			min_x = Math.min(min_x, points[i][0]);
			min_y = Math.min(min_y, points[i][1]);
			max_x = Math.max(max_x, points[i][0]);
			max_y = Math.max(max_y, points[i][1]);
		}
		var cent_x = (min_x+max_x)/2, cent_y = (min_y+max_y)/2, scale = 0.85*Math.min(canvas.width/(max_x-min_x), canvas.height/(max_y-min_y));
		return (point) => {
			return [(point[0]-cent_x)*scale, (point[1]-cent_y)*scale];
		};
	}

	/*
	Utility function to display the side length onto the canvas
	it takes in two points: start and ending points of the line,
	a length value to draw, whether or not to draw dotted lines as a ruler,
	a calibrator function
	and a target context object
	*/
	function drawLength(p1, p2, val, draw_ruler, func, context) {
		p1 = func(p1);
		p2 = func(p2);
		let dx = p1[1]-p2[1], dy = p2[0]-p1[1];
		let d = Math.sqrt(dx*dx+dy*dy);
		dx*=45/d; dy*=45/d;
		context.font='35px verdana';
		context.fillText(val.toString(), (p1[0]+p2[0])/2+dx-6, (p1[1]+p2[1])/2+dy+3);
		if(draw_ruler) {
			context.setLineDash([10,10]);
			context.beginPath();
			context.moveTo(p1[0], p1[1]);
			context.lineTo(p2[0], p2[1]);
			context.stroke();
		}
	}

	/*
	Utility function to display the angle onto the canvas
	it takes in three points creating an angle between two lines,
	an angle val to drawm a calibrator function, and a target context object
	*/
	function drawAngle(p1, p2, p3, val, func, context) {
		p1 = func(p1); p2 = func(p2); p3 = func(p3);
		d = [(p1[0]+p3[0])/2,(p1[1]+p3[1])/2];
		ad = Math.sqrt(d[0]**2 + d[1]**2);
		p2p1p3 = [p2[0]+d[0]*40/ad, p2[1]+d[1]*40/ad];
		context.font='35px verdana';
		context.fillText(val.toString(), p2p1p3[0]-6, p2p1p3[1]+3);
	}

	/*
	utility function to trace the points in the canvas context
	it takes in an array of points along with a calibrator function and draws the calibrated points into the context
	*/
	function tracePoints(points, func, context) {
		context.setLineDash([]);
		context.beginPath();
		context.moveTo(func(points[0][0]), func(points[0][1]));
		for(var i = 1; i < points.length; i++) {
			context.moveTo(func(points[i][0]), func(points[i][1]));
		}
		context.closePath();
		context.stroke();
	}
	

	return {
		/*
		drawPolygon_l: given an array of side lengths, draws a matching polygon onto the given canvas
		if display_side_lengths is true, then side lengths are drawn as well
		*/
		drawPolygon_l: function(length_array, display_side_lengths, canvas_id) {
			// TODO
		},
		/*
		drawTrapezoid: given a base, height, top, topoffset, whether or not to display side lengths, and a canvas ID, draws a matching
		trapezoid onto the corresponding canvas.
		note: topoffset is the horizontal displacement from the leftmost point of the base to the leftmost point of the top
		if display_side_lengths is true, then the base, height, and top measurements are drawn
		*/
		drawTrapezoid: function(base, height, top, topoffset, display_side_lengths, canvas_id) {
			var canvas = document.getElementById(canvas_id);
			var context = canvas.getContext('2d');
			var points = [[0,0],[base,0],[top+topoffset,height],[topoffset,height]];
			var heightruler = [[Math.min(-10, topoffset-10), 0], [Math.min(-10, topoffset-10), height]];
			var func = calibrate(points, canvas);
			tracePoints(points, func, context);
			if(display_side_lengths) {
				drawLength(heightruler[1], heightruler[0], height, true, func, context);
				drawLength(points[0], points[1], base, false, func, context);
				if(base != top) drawLength(points[2], points[3], top, false, func, context);
			}
		},
		/*
		drawRectangle: given a base and a height, draws a matching rectangle onto the corresponding canvas.
		if display_side_lengths is true, then the base and height measurements are drawn
		*/
		drawRectangle: function(base, height, display_side_lengths, canvas_id) {
			var canvas = document.getElementById(canvas_id);
			var context = canvas.getContext('2d');
			var points = [[0, 0], [base, 0], [base, height], [0, height]];
			var func = calibrate(points, canvas);
			tracePoints(points, func, context);
			if(display_side_lengths) {
				drawLength(points[0], points[1], base, false, func, context);
				drawLength(points[3], points[0], height, false, func, context);
			}
		},
		/*
		drawTriangle_bh: given a base, height, and topoffset, displays the corresponding triangle onto the canvas
		if display_side_lengths is true, then the base and height measurements are drawn
		*/
		drawTriangle_bh: function(base, height, topoffset, display_side_lengths, canvas_id) {
			var canvas = document.getElementById(canvas_id);
			var context = canvas.getContext('2d');
			var points = [[0, 0], [base, 0], [base+topoffset, height]];
			var heightruler = [[Math.min(-10, topoffset-10), 0], [Math.min(-10, topoffset-10), height]];
			var func = calibrate(points, canvas);
			tracePoints(points, func, context);
			if(display_side_lengths) {
				drawLength(points[0], points[1], base, false, func, context);
				drawLength(heightruler[1], heightruler[0], height, true, func, context);
			}
		},
		/*
		drawTriangle_saa: given a base and two angles adjacent to the base, draws the corresponding side-angle-angle triangle onto the canvas
		if display_side_lengths is true, then the base measurement is drawn
		if display_angles is true, then the two angles adjacent to the base are shown
		*/
		drawTriangle_saa: function(base, angle_1, angle_2, display_side_lengths, display_angles, canvas_id) {
			var canvas = document.getElementById(canvas_id);
			var context = canvas.getContext('2d');
			var side = base/Math.sin(2*Math.PI-angle_1-angle_2)*Math.sin(angle_2);
			var points = [[0, 0], [base, 0], [Math.cos(angle_1)*side,Math.sin(angle_1)*side]];
			var func = calibrate(points, canvas);
			tracePoints(points, func, context);
			if(display_side_lengths) {
				drawLength(points[0], points[1], base, false, func, context);
			}
			if(display_angles) {
				drawAngle(points[2],points[0],points[1],angle_1,func,context);
				drawAngle(points[2],points[1],points[0],angle_2,func,context);
			}
		},
		/*
		drawTriangle_sas: given a length, an angle, and another length, draws the corresponding length-angle-length triangle onto the canvas
		if display_side_lengths is true, then the length measurements are drawn
		if display_angles is true, then the given angle is drawn onto the appropriate location on the triangle
		*/
		drawTriangle_sas: function(length_1, angle, length_2, display_side_lengths, display_angles, canvas_id) {
			var canvas = document.getElementById(canvas_id);
			var context = canvas.getContext('2d');
			var points = [[0,0],[length_2,0],[Math.cos(angle)*length_1,Math.sin(angle)*length_1]];
			var func = calibrate(points,canvas);
			tracePoints(poitns,func,context);
			if(display_side_lengths) {
				drawLength(points[0],points[1],length_2,false,func,context);
				drawLength(points[2],points[0],length_1,false,func,context);
			}
			if(display_angles) {
				drawAngle(points[2],points[0],points[1],angle, func, context);
			}
		}
	};
})()