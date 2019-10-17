function Nodo (id,valStr,confJson) {
	this.valStr = valStr;
	this.id = id;
	this.confJson = confJson
	this.puntoNorte = confJson.puntoNorte;
	this.puntoSur = confJson.puntoSur;
	this.puntoEste = confJson.puntoEste;
	this.puntoOeste = confJson.puntoOeste;
}


Nodo.prototype.metodo = function() {
	alert("Mama de miguel"+this.id);
};



Nodo.prototype.crearCanvas = function() {
	if (this.confJson.shape == undefined)
		return undefined
	var canvas  = document.createElement("canvas");
	canvas.setAttribute("id",this.id+"Canvas");
	canvas.setAttribute("width","50");
	canvas.setAttribute("height","50");
	lienzo = canvas.getContext('2d');
	switch(this.confJson.shape){
		case "inicio":
			lienzo.ellipse(70/2, 26/2, 70, 26);
		break;
		case "fin":
			lienzo.ellipse(70/2, 26/2, 70, 26);
		break;
		case "flecha":
		break;
		case "rectangulo":
			lienzo.clearRect(0,0,30,30);
		break;
		case "rombo":
			lienzo.triangle(0, 0, 300/2, 0, 150/2, 150/2);
		break;
		default:
			alert("Algo se chingo");
		break;
	}
	return canvas;
}


Nodo.prototype.crearElemento = function() {
	if (this.confJson.parent == undefined)
		return undefined
	var div  = document.createElement("div");
	div.setAttribute("id",this.id);
	div.setAttribute("class",this.confJson.class+" text-center");
	div.innerHTML = this.valStr;
	



	if(this.confJson.isDrag != undefined && this.confJson.isDrag == true )
	{
		div.setAttribute("ondragstart","dragStartEvent(event)");
		div.setAttribute("draggable","true");
	}else if(this.confJson.isDrop != undefined && this.confJson.isDrop == true ){
		div.setAttribute("ondragover","allowDrop(event)");
		div.setAttribute("ondrop","dropEvent(event)");
	}
	//div.appendChild(this.crearCanvas());
	return div;
};





