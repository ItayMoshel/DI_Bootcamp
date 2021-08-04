let button = document.getElementById('insert');
let tr = document.getElementsByTagName('tr');
console.log(tr[0]);

let input = document.getElementById('insert');
input.addEventListener("click", insert_Row);

function insert_Row() {
    for (let i = 0; i < 1; i++) {
        let newTr = document.getElementById('sampleTable').insertRow(i);
        let newTb1 = newTr.insertCell(0);
        let newTb2 = newTr.insertCell(1);
        newTb1.innerHTML = "Row" + tr.length + " cell1";
        newTb2.innerHTML = "Row" + tr.length + " cell2";
    }

}