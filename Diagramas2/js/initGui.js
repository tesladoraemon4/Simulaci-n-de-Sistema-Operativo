
function lanzarGui () {
	jsPlumb.setContainer("diagramContainer");
	var common = {
	    isSource:true,
	    isTarget:true,
	    connector:"Straight",
	    endpoint:"Rectangle",
	    paintStyle:{ fill:"white", outlineStroke:"blue", strokeWidth:3 },
	    hoverPaintStyle:{ outlineStroke:"lightblue" },
	    connectorStyle:{ outlineStroke:"green", strokeWidth:1 },
	    connectorHoverStyle:{ strokeWidth:2 },
	    overlays:[ 
	        ["Arrow" , { width:12, length:12, location:0.67 }]
	    ],
	    //atributos de nodo
	    parent: document.getElementById('cajaItems'),
	    shape:"rectangulo",
	    class:"row",
	    isDrag:true
	};

	var nomElementos = ["Inicio","Fin","Flecha","Rectangulo","Rombo"];
	for (var i = nomElementos.length - 1; i >= 0; i--) {
		nodo = new Nodo(nomElementos[i],nomElementos[i],common);
		elemento = nodo.crearElemento();
		elemento.puntoNorte = true;
		elemento.puntoSur = true;
		elemento.puntoEste = true;
		elemento.puntoOeste = true;
		common.parent.appendChild(elemento);
	};
	jsPlumb.addEndpoint("item_left", { 
		endpoint:"Dot",
		anchor: ["TopCenter",{ shape:"Circle" }],
	    anchor:[ "Perimeter", { shape:"Circle" } ]
	}, common); 
	//cuatroConexiones("item_right",common); agrega 4 conexiones
	jsPlumb.draggable("item_left");
	jsPlumb.draggable("item_right");
	/*Conector con flechas 
	    var common = {
	        connector: ["Straight"],
	        anchor: ["Left", "Right"],
	        endpoint:"Dot"
	    };
	    jsPlumb.connect({
	        source:"item_left",
	        target:"item_right",
	        paintStyle:{ stroke:"lightgray", strokeWidth:3 },
	        endpointStyle:{ fillStyle:"lightgray", outlineStroke:"gray" },
	        overlays:[ 
	            ["Arrow" , { width:12, length:12, location:0.67 }]
	        ]
	    }, common);
	*/
	
}

jsPlumb.ready(lanzarGui);
var cont=0;
function allowDrop(ev) {
    ev.preventDefault();
}
function drop(ev) {

    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    //"Inicio","Fin","Flecha","Rectangulo","Rombo"

    var nodo = new Nodo(cont+""+data,cont+""+data,common);
    elemento = nodo.crearElemento();
    elemento.setAttribute("class","item text-center");


    cont++;
    ev.target.appendChild(div);

}
function dragStartEvent(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
