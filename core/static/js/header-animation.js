(function(){
    var stage, circles;
    var numCircles = 150;
    var colors = ['#F16623', '#FCBD2A', '#E34B25', '#E84642', '#2CAC70', '#3992CF', '#FFF'];

    function init() {
        initStages();
        initCircles();
        animate();
    }

    // Init Canvas
    function initStages() {
        canvash = document.getElementById('stage-canvas').height;
        canvasw = document.getElementById('stage-canvas').width;
        stage = new createjs.Stage("stage-canvas");
        stage.canvas.width = window.innerWidth;
        stage.canvas.height = canvash;
    }

    function initCircles() {
        circles = [];
        for(var i=0; i<numCircles; i++) {
            var circle = new createjs.Shape();
            var r = 15*Math.random()+4;
            var x = document.getElementById('stage-canvas').width*2*Math.random();
            var y = 350*Math.random();
            var color = colors[Math.floor(i%colors.length)];
            var alpha = Math.random()*0.7;
            circle.alpha = alpha;
            circle.radius = r;
            circle.graphics.beginFill(color).drawCircle(0, 0, r);
            circle.x = x;
            circle.y = y;
            circles.push(circle);
            stage.addChild(circle);
            circle.movement = 'float';
            tweenCircle(circle);
        }
    }


    // animating circles
    function animate() {
        stage.update();
        requestAnimationFrame(animate);
    }

    function tweenCircle(c) {
        if(c.tween) c.tween.kill();
        c.tween = TweenLite.to(c, 5 + Math.random()*3.5,
            {x: c.x + -100+Math.random()*200, y: c.y + -100+Math.random()*200,
                ease:Quad.easeInOut, alpha: 0.2 + Math.random()*0.5,
        onComplete: function() {
            tweenCircle(c);
        }});
    }

    window.onload = function() { init() };
})();