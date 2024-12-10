const readline = require("readline");

let input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

input.question("Your Name: ",(name)=> {
    console.log("hello "+ name);
    input.question("primeiro numero: ",(n1)=>{
        input.question("segundo numero: ",(n2)=>{
            
            console.log(parseInt(n1)+parseInt(n2));
            input.close();
        });
    });
    
});




