
function logSubmit(event){
	
	event.preventDefault();
	const city = document.getElementById("city").value;
	console.log(city);
	erase_li();
	erase_image();
	getData(city);
}

const getData = (city) =>{
	const xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://127.0.0.1:5000/city?city='+ city);
	xhr.responseType = 'json';
	const liste = ["temperature", "description", "humidite", "nom", "lever_du_soleil", "coucher_de_soleil"]
	xhr.onload = () => {
		const data = xhr.response;
		create_image(data);
		for(let parametre of liste){
			parameters(data, parametre);
		}
		console.log(data);

	};
	xhr.send();
}
function parameters(data, parametre) {
	var li = document.createElement("li");
	li.textContent = parametre + ": " + data[parametre];
	li.className = "list-group-item";
	const ul = document.getElementById("maListe");
	ul.appendChild(li);
}
function create_image(data){
	var image = document.createElement("img");
	image.src = "http://openweathermap.org/img/w/" + data["icon"]+ ".png";
	image.alt = "Weather Icon";
	image.id = "wicon";
	const div_image = document.getElementById("image");
	div_image.appendChild(image);
}
function erase_li(){
	const all_li = document.querySelectorAll('li');
	all_li.forEach(li => {
        li.remove();
    });
}
function erase_image(){
	const image = document.getElementById("wicon");
	if(image){
		image.remove();
	}
}
const form = document.getElementById("form");
let button = document.getElementById('button-addon2');
form.addEventListener("submit", logSubmit);