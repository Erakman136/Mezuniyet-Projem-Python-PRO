const screen = document.querySelector('.calculator-screen');
const buttons = document.querySelectorAll('button');
let input = '0';
let operator = '';
let operand1 = '';
let operand2 = '';
let result = '';

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const buttonText = button.innerText;

        if (buttonText === 'SİL') {
            input = '0';
            operand1 = '';
            operand2 = '';
            operator = '';
            screen.value = input;
        } else if (buttonText === '=') {
            operand2 = input;
            calculateResult();
            screen.value = result;
            input = result;
        } else if (['+', '-', '×', '÷', '%', 'x²', '√'].includes(buttonText)) {
            operator = buttonText;
            operand1 = input;
            input = '';
        } else {
            if (input === '0') input = buttonText;
            else input += buttonText;
            screen.value = input;
        }
    });
});

function calculateResult() {
    let num1 = parseFloat(operand1);
    let num2 = parseFloat(operand2);

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '×':
            result = num1 * num2;
            break;
        case '÷':
            result = num1 / num2;
            break;
        case '%':
            result = num1 % num2;
            break;
        case 'x²':
            result = Math.pow(num1, 2);
            break;
        case '√':
            result = Math.sqrt(num1);
            break;
        default:
            result = input;
    }
}
