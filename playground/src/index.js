const express = require('express');
const app = express();

const port = process.env.PORT || 4000;

function solve() {
    var readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    var lines = [];
    var lineIndex = 0;
    var filters = [];
    rl.on('line', (line) => {
        if (lineIndex === 0) {
            lines.push(line);
            lineIndex += 1;
        } else {
            lines.push(line);
            filters = [...lines[0]].filter((item) => {
                return item.toLowerCase() === lines[1].toLowerCase()
            })
            lineIndex = 0;
            console.log(filters.length);
        }
    })
}

app.get('/', (req, res) => res.send('Hello World!!!'));

app.listen(port, () =>
    console.log(`Server running at http://localhost:${port}`)
);