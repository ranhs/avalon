
const fs = require('fs')

const obj = JSON.parse(fs.readFileSync('avalonscores.json').toString())

let line = newLine()
console.log(Object.keys(line).join(','))
for ( const key of Object.keys(obj) ) {
    line = newLine()
    //console.log(key)
    line.turn = key[2]
    for (let i = 3; i<key.length; i+=4) {
        line[key.substring(i,i+3)] = key[i+3]
    }
   line.score = obj[key].s
    console.log(Object.keys(line).map(k=>line[k]).join(','))
    //break
}

function newLine() {
   const obj = {turn:''}
   for (let i = 1; i<=9; i++) {
      for (let j = 1; j<=9; j++) {
         const k = i+j-5
         if ( k <=0 || k >=10 ) continue
         obj[`${j}${i}${k}`] = ''
      }
   }
  obj.score = 0
  return obj
}
