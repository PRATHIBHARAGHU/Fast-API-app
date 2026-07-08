// console.log("hello world");
// let x=10;
// console.log(x);
// const y=20;
// console.log(y);
// // console.log(x+y);

// function add(a,b){
//     return a+b;
// }
// console.log(add(5,10));
// const arr=[10,20,30,40,50];
// console.log(arr[0]);
// console.log(arr[1]);
// console.log(arr[2]);
// console.log(arr[3]);
// console.log(arr[4]);

//dictionary
// const dict={"name":"John","age":30,"city":"New York"};
// console.log(dict["name"]);

// //destructuring
// let {name,age,city}=dict;
// console.log(name);
// console.log(age);
// console.log(city);

//destructuring array
// const arr=[10,20,30,40,50];
// let [a,b,c,d,e]=arr;
// console.log(a);
// console.log(b);
// console.log(c);
// console.log(d);
// console.log(e);

//rest and spread operator

//spread operator --> ...
// a=[10,20]
// b=[30,40]
// console.log(...a,...b);
// console.log([...a,...b]);
// O/P - 10 20 30 40
// [ 10, 20, 30, 40 ]

//rest operator --> ...
// function add(a,...b){
//     return a+b;
// }
// console.log(add(10,20));
// console.log(add(10,20,30));
// o/p 1020
// 1020,30

//Template literals

const a =10;
const b =20;
console.log(`The sum of ${a} and ${b} is ${a+b}`);