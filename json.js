fetch('./js.json')
var data = JSON.parse("js.json")
switch(data[0].case){
    case 1:
        document.getElementById("img").src = "case1.png"
    case 2:
        document.getElementById("img").src = "case2.png"
    case 3:
        document.getElementById("img").src = "case3.png"
    case 4:
        document.getElementById("img").src = "case4.png"
    case 5:
        document.getElementById("img").src = "case5.png"
    case 6:
        document.getElementById("img").src = "case6.png"
    case 7:
        document.getElementById("img").src = "case7.png"
}
document.getElementById("al").innerHTML= data[0].alg;