const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = 1300;
canvas.height = 100;

const confettiColors = ["#EF476F", "#FFD166", "#06D6A0", "#118AB2", "#073B4C"];

class Confetti {
  constructor() {
    this.x = Math.random() * canvas.width/2; // position within the left half of canvas
    this.y = canvas.height + 10;
    this.color = confettiColors[Math.floor(Math.random() * confettiColors.length)];
    this.radius = Math.random() * 6 + 2;
    this.speed = Math.random() * 2 + 1;
    this.angle = Math.atan2(canvas.height, canvas.width) + Math.random() * (Math.PI / 3) - Math.PI / 6; // diagonal angle with random deviation
    this.velocity = {
      x: Math.cos(this.angle) * this.speed,
      y: -Math.sin(this.angle) * this.speed
    };
  }

  update() {
    this.x += this.velocity.x;
    this.y += this.velocity.y;
    
    if (this.x > canvas.width + this.radius || this.y < -this.radius) {
      this.x = Math.random() * canvas.width/2;
      this.y = canvas.height + 10;
      this.color = confettiColors[Math.floor(Math.random() * confettiColors.length)];
      this.radius = Math.random() * 6 + 2;
      this.speed = Math.random() * 2 + 1;
      this.angle = Math.atan2(canvas.height, canvas.width) + Math.random() * (Math.PI / 3) - Math.PI / 6;
      this.velocity = {
        x: Math.cos(this.angle) * this.speed,
        y: -Math.sin(this.angle) * this.speed
      };
    }
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
  }
}

const confettis = [];

function shootConfetti() {
  const confettiAmount = Math.floor(Math.random() * 50 + 10);
  
  for (let i = 0; i < confettiAmount; i++) {
    confettis.push(new Confetti());
  }

  setTimeout(() => {
    confettis.length = 0;
  }, 2000);
}

function animate() {
  requestAnimationFrame(animate);
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < confettis.length; i++) {
    confettis[i].update();
    confettis[i].draw();
  }
}

animate();

window.onload = function() {
    shootConfetti();
};