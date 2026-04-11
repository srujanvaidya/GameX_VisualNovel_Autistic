// Monochromatic Centered Black Hole Canvas
const canvas = document.getElementById('void-canvas');
const ctx = canvas.getContext('2d');
let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
});

const particles = [];
class Matter {
    constructor() {
        this.reset();
    }
    reset() {
        this.angle = Math.random() * Math.PI * 2;
        this.radius = Math.random() * (Math.max(w, h)) + 100;
        this.speed = Math.random() * 0.0015 + 0.0005;
        this.size = Math.random() * 1.2 + 0.3;
        this.inwardSpeed = Math.random() * 0.3 + 0.1;
    }
    update() {
        this.angle += this.speed;
        this.radius -= this.inwardSpeed;
        
        if(this.radius < 200) {
            this.speed += 0.0002;
            this.inwardSpeed += 0.02;
        }

        // Crosses event horizon
        if (this.radius < 50) {
            this.reset();
        }
    }
    draw() {
        const centerX = w * 0.5; // Centered
        const centerY = h * 0.5;
        const x = centerX + Math.cos(this.angle) * this.radius;
        const y = centerY + Math.sin(this.angle) * this.radius;

        let alpha = 1;
        if(this.radius > w * 0.8) alpha = 0;
        else if (this.radius < 100) alpha = this.radius / 100;
        else alpha = 1 - ((this.radius - 100) / (w * 0.8));

        ctx.fillStyle = `rgba(255, 255, 255, ${alpha * 0.5})`;
        ctx.beginPath();
        ctx.arc(x, y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

for(let i=0; i<600; i++) particles.push(new Matter());

function loop() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.15)'; // Fading trail effect
    ctx.fillRect(0, 0, w, h);
    
    // Draw event horizon circle
    ctx.fillStyle = '#000000';
    ctx.beginPath();
    ctx.arc(w * 0.5, h * 0.5, 48, 0, Math.PI * 2);
    ctx.fill();

    particles.forEach(p => {
        p.update();
        p.draw();
    });
    requestAnimationFrame(loop);
}
loop();

// Accordion Logic
document.querySelectorAll('.acc-header').forEach(button => {
    button.addEventListener('click', () => {
        const accContent = button.nextElementSibling;

        button.classList.toggle('active');

        if (button.classList.contains('active')) {
            accContent.style.maxHeight = accContent.scrollHeight + 'px';
        } else {
            accContent.style.maxHeight = 0;
        }
    });
});
