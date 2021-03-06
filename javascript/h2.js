const change = (cents) => {
    if (cents < 0) throw RangeError();
    let result = [0, 0, 0, 0];
    result[0] = Math.floor(cents / 25);
    cents %= 25;
    result[1] = Math.floor(cents / 10);
    cents %= 10;
    result[2] = Math.floor(cents / 5);
    result[3] = cents % 5;
    return result;
}

const stripQuotes = (str) => {
    return str.replace(/['"]/g, '');
}

const scramble = (str) => {
    let result = str.split('');
    for (let i = 0; i < str.length; i++) {
        let randIndex = Math.floor(Math.random() * str.length);
        let temp = result[i];
        result[i] = result[randIndex];
        result[randIndex] = temp;
    }
    return result.join('');
}

const powers = (base, limit) => {
    let result = [];
    if (base < 1 || limit < 1) return result;
    let exp = 1, nextPow = 1;
    while (nextPow <= limit) {
        result.push(nextPow);
        nextPow = Math.pow(base, exp);
        exp++;
    }
    return result;
}

// console.log(powers(2, -5));
// console.log(powers(7, 0));
// console.log(powers(3, 1)); This call is not passing the test despite being correct
// console.log(powers(2, 63));
// console.log(powers(2, 64));

const say = (word = '') => {
    if (word == '') return word;
    return (y = null) => {
        if (y == null)
            return word;
        else
            say(word + ' ' + y);
    }
}

const interleave = (arr, ...args) => {
    let result = [];
    let totalCount = arr.length + args.length;
    let arrPtr = 0, argsPtr = 0;
    let pushArr = true;
    while (arrPtr + argsPtr < totalCount) {
        if (pushArr && arrPtr < arr.length) {
            result.push(arr[arrPtr]);
            arrPtr++;
        }
        else if (argsPtr < args.length) {
            result.push(args[argsPtr]);
            argsPtr++;
        }
        pushArr = !pushArr;
    }
    return result;
}

module.exports = { change, stripQuotes, scramble, say, powers, interleave };