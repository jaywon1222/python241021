const canvas = document.getElementById('gameBoard');
const ctx = canvas.getContext('2d');

const ROWS = 20;
const COLS = 10;
const BLOCK_SIZE = 30;

// 테트로미노 모양
const SHAPES = [
    [],
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
];

// 게임 보드
let board = Array(ROWS).fill().map(() => Array(COLS).fill(0));

// 현재 테트로미노
let currentShape;
let currentX;
let currentY;

// 새 테트로미노 생성
function newShape() {
    const shapeIndex = Math.floor(Math.random() * (SHAPES.length - 1)) + 1;
    currentShape = SHAPES[shapeIndex];
    currentX = Math.floor(COLS / 2) - Math.floor(currentShape[0].length / 2);
    currentY = 0;
}

// 충돌 검사
function collision() {
    for (let y = 0; y < currentShape.length; y++) {
        for (let x = 0; x < currentShape[y].length; x++) {
            if (currentShape[y][x] && 
                (board[y + currentY] && board[y + currentY][x + currentX]) !== 0) {
                return true;
            }
        }
    }
    return false;
}

// 테트로미노 고정
function freeze() {
    for (let y = 0; y < currentShape.length; y++) {
        for (let x = 0; x < currentShape[y].length; x++) {
            if (currentShape[y][x]) {
                board[y + currentY][x + currentX] = 1;
            }
        }
    }
}

// 줄 제거
function clearLines() {
    for (let y = ROWS - 1; y >= 0; y--) {
        if (board[y].every(cell => cell === 1)) {
            board.splice(y, 1);
            board.unshift(Array(COLS).fill(0));
        }
    }
}

// 게임 오버 체크
function isGameOver() {
    return board[0].some(cell => cell === 1);
}

// 게임 보드 그리기
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // 보드 그리기
    for (let y = 0; y < ROWS; y++) {
        for (let x = 0; x < COLS; x++) {
            if (board[y][x]) {
                ctx.fillStyle = 'blue';
                ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
            }
        }
    }
    
    // 현재 테트로미노 그리기
    if (currentShape) {
        ctx.fillStyle = 'red';
        for (let y = 0; y < currentShape.length; y++) {
            for (let x = 0; x < currentShape[y].length; x++) {
                if (currentShape[y][x]) {
                    ctx.fillRect((currentX + x) * BLOCK_SIZE, (currentY + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
                }
            }
        }
    }
}

// 게임 루프
function gameLoop() {
    currentY++;
    if (collision()) {
        currentY--;
        freeze();
        clearLines();
        if (isGameOver()) {
            alert('게임 오버!');
            return;
        }
        newShape();
    }
    draw();
}

// 키보드 이벤트 처리
document.addEventListener('keydown', (e) => {
    switch(e.keyCode) {
        case 37: // 왼쪽
            currentX--;
            if (collision()) currentX++;
            break;
        case 39: // 오른쪽
            currentX++;
            if (collision()) currentX--;
            break;
        case 40: // 아래
            currentY++;
            if (collision()) currentY--;
            break;
        case 38: // 위 (회전)
            const rotated = currentShape[0].map((_, i) => currentShape.map(row => row[i]).reverse());
            const prevShape = currentShape;
            currentShape = rotated;
            if (collision()) currentShape = prevShape;
            break;
    }
    draw();
});

// 게임 시작
newShape();
setInterval(gameLoop, 500);
