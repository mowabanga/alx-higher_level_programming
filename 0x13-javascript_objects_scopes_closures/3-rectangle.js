#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }

        function print() {
            for (const i = 0; i < this.height; i++) {
                print(i)
            }
        }
    }
}