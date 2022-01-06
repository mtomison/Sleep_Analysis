// d3.json("/ML/7/8").then(result => console.log(result));

function dothething(event) {
    event.preventDefault();
    console.log('clicksubmit');
    let timeInBed = d3.select('#timeInBed').property('value');
    let fellAsleep = d3.select('#fellAsleep').property('value');
    let activity = d3.select('#activity').property('value');
    let stressfulDay = Number(d3.select('#stressfulDay').property('checked'));
    let workedOut = Number(d3.select('#workedOut').property('checked'));
    let drankCoffee = Number(d3.select('#drankCoffee').property('checked'));
    let drankTea = Number(d3.select('#drankTea').property('checked'));
    let ateLate = Number(d3.select('#ateLate').property('checked'));

    d3.json(`/ML/${timeInBed}/${activity}/${stressfulDay}/${drankCoffee}/${drankTea}/${ateLate}/${workedOut}/${fellAsleep}`).then(result => {
        d3.select('#result').property('value',result);
        console.log('shoudl have worked')
    });
    


}



function getInput(){
    var input = document.getElementById("number").value;
    // conversion from string to integer
    if(isNaN(input)) return 0; // value is not a number
    var value = parseInt(input);
}
document.getElementById('submit').addEventListener('click',dothething, false);
