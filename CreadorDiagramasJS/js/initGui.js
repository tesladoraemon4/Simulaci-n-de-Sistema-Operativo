function lanzarGui () {
	//COntenedor del diagrama
	diagramContainer = document.getElementById("diagramContainer");
	var secondInstance = jsPlumb.getInstance({
	  PaintStyle:{ 
	    strokeWidth:6, 
	    stroke:"#567567", 
	    outlineStroke:"black", 
	    outlineWidth:1 
	  },
	  Connector:[ "Flowchart", { curviness: 30 } ],
	  Endpoint:[ "Dot", { radius:8 } ],
	  EndpointStyle : { fill: "#30AF0E"  },
	  Anchor : [ 0.5, 0.5, 1, 1 ]
	});
	//configuracion de los puntos finales JSON
	configJsonPuntoFInal = {
	  endpoint:["Dot",{ radius:7 }],
	  paintStyle:{ width:20, height:42, fill:'#19C3D1' },
	  isSource:true,
	  isTarget:true,
	  connectorStyle : { stroke:"#7E0EAF" },
	  connectorOverlays: [ [ "Arrow", { location:0.5 } ] ],
	  maxConnections:-1
	};


	//configuracion para los Elementos arrastrables
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
	    
	    Connector:[ "Bezier", { curviness: 30 } ],
	    Endpoint:[ "Dot", { radius:5 } ],
	    EndpointStyle : { fill: "#567567"  },
	    //atributos de nodo
	    parent: document.getElementById('cajaItems'),
	    shape:"rectangulo",
	    class:"row",
	    isDrag:true,
	};

	var nomElementos = ["Inicio","Fin","Flecha","Rectangulo","Rombo"];
	for (var i = nomElementos.length - 1; i >= 0; i--) {
		common.typeElement = nomElementos[i];
		nodo = new Nodo(nomElementos[i],nomElementos[i],common);
		elemento = nodo.crearElemento();
		elemento.puntoNorte = true;
		elemento.puntoSur = true;
		elemento.puntoEste = true;
		elemento.puntoOeste = true;
		common.parent.appendChild(elemento);
	};



	jsPlumb.on(document, "tap", ".node-edit", function () {
	  var info = renderer.getObjectInfo(this);
	  jsPlumbToolkit.Dialogs.show({
	    id: "dlgText",
	    data: info.obj.data,
	    title: "Edit " + info.obj.data.type + " name",
	    onOK: function (data) {
	      if (data.text && data.text.length > 2) {
	        // if name is at least 2 chars long, update the underlying data and update the UI.
	        toolkit.updateNode(info.obj, data);
	      }
	    }
	  });
	});






}


//agrega los puntos finales al nodo 
function agregarConexiones (nombreElemento,anchors,configJson) {
	for (var i = anchors.length - 1; i >= 0; i--) {
		configJson.anchors = [anchors[i]];
		jsPlumb.addEndpoint(nombreElemento, configJson);
	};
}
//agrega los puntos finales al nodo 
function agregarConexionesCompletas (nombreElemento,anchorsCompletes,configJson) {
	var anchors =  anchorsCompletes.posiciones;
	var sourceOrTarget =  anchorsCompletes.sourcesTarjets;
	for (var i = anchors.length - 1; i >= 0; i--) {
		configJson.anchors = [anchors[i]];
		configJson.isTarget = sourceOrTarget[i].isTarget;
		configJson.isSource = sourceOrTarget[i].isSource;
		if(configJson.isSource==true)
			configJson.maxConnections = 1
		else
			configJson.maxConnections = -1

		jsPlumb.addEndpoint(nombreElemento, configJson);
	};
}

var cont=0;
function allowDrop(ev) {
    ev.preventDefault();
}
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
	//Crear elemento para arrastrar 
	var elemento = document.createElement("div");
	diagramContainer.appendChild(elemento);
	elemento.setAttribute("id",cont+""+data);
	if(data== "Rombo")
		elemento.setAttribute("class",data.toLowerCase()+"Item text-RightMiddle");
	else
		elemento.setAttribute("class",data.toLowerCase()+"Item text-center");
	//FIN Crear elemento para arrastrar 
	configuraNuevoNodo(cont+""+data);

    cont++;
	jsPlumb.draggable(elemento);
}
/*
	COnfigura las caracteristicas del nuevo item soltado =)
*/
function configuraNuevoNodo(valStr){
	var elemento = document.getElementById(valStr),
	valor;
	var nomElementos = ["Inicio","Fin","Flecha","Rectangulo","Rombo"];
    var arraysRegExp = new Array(
	    	RegExp("[0-9]*"+nomElementos[0]),
	    	RegExp("[0-9]*"+nomElementos[1]),
	    	RegExp("[0-9]*"+nomElementos[2]),
	    	RegExp("[0-9]*"+nomElementos[3]),
	    	RegExp("[0-9]*"+nomElementos[4])
    	);
	if (arraysRegExp[0].test(valStr)) {//inicio
		agregarConexionesCompletas(valStr,
			{posiciones:["Bottom"],
			sourcesTarjets:[{isSource:true,isTarget:false}]},
			configJsonPuntoFInal);
		elemento.appendChild(crearNodoTexto("Inicio"));
	}else if(arraysRegExp[1].test(valStr)){//fin
		console.log("fin")
		agregarConexionesCompletas(valStr,
			{posiciones:["Top"],
			sourcesTarjets:[{isSource:false,isTarget:true}]},
			configJsonPuntoFInal);
		elemento.appendChild(crearNodoTexto("Fin"));
	}else if(arraysRegExp[3].test(valStr)){//rectangulo
		console.log("rectangulo");
		agregarConexionesCompletas(valStr,
			{posiciones:["Top","Bottom"],
			sourcesTarjets:[{isSource:false,isTarget:true},{isSource:true,isTarget:false} ]},
			configJsonPuntoFInal);
		valor = prompt("Introduce las sentencias (no olvides el ;)","int x=0;");
		elemento.appendChild(crearNodoTexto(valor));
	}else if(arraysRegExp[4].test(valStr)){//Rombo
		console.log("Rombo");
		agregarConexionesCompletas(valStr,
			{posiciones:["Left","Right","Top"],
			sourcesTarjets:[
				{isSource:true,isTarget:false},
				{isSource:true,isTarget:false} ,
				{isSource:false,isTarget:true}
			]},
			configJsonPuntoFInal);
		valor = prompt("Introduce la condicion ","x <= 4");
		elemento.appendChild(crearNodoTexto(valor));
	}
}

function crearNodoTexto (contenido) {
	var elemP = document.createElement('p');
	elemP.setAttribute("name","contenidoItem");
	var nuevoTexto = document.createTextNode(contenido);
	elemP.appendChild(nuevoTexto);
	return elemP;
}
function dragStartEvent(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
var addfLechasEntrada = function (toId, targetAnchors) {
 	for (var i = targetAnchors.length - 1; i >= 0; i--) {
 		jsPlumb.addEndpoint(toId, targetEndpoint, 
 			{ anchor: targetAnchors[i], 
 				uuid: toId.id+""+i 
 			});
 	};
};



/*
	Obtiene una lista de id objects de todos los nodos que hay en el diagrama.

*/
function crearDiagrama() {
	console.log("Creando diagrama");
	var connectionList = jsPlumb.getConnections(); // you get a list of Connection objects that are in the default scope.
	for (var i = connectionList.length - 1; i >= 0; i--) {
		console.log(connectionList[i]);
	};
	crearMatrizAdyacencia(connectionList);
}
/*
	Obtiene una lista de id objects de todos los nodos que hay en el diagrama.
*/
function obtenerNodos(connectionList){
	//sacamos los nodos en la lista
	var a = [];
	for (var i = connectionList.length - 1; i >= 0; i--) {
		a.push(connectionList[i].target);
		a.push(connectionList[i].source);
	};
	var unicos = [];
	var rs;
	/*
	sourceId
	targetId
	*/
	for (var i = a.length - 1; i >= 0; i--) {
		rs = unicos.find(function (item) {
			return (a[i] == item);
		});
		if(rs === undefined){
			unicos.push(a[i]);
		}
	};
	return unicos;
}
function crearMatrizAdyacencia(connectionList){
	//buscamos los nodos 
	var lN = obtenerNodos(connectionList);
	//Creamos la matriz de adyacencia
	var tam = lN.length;
	var matriz=new Array(tam);
	for (i = 0; i < tam; i++){
		matriz[i] = new Array(tam);
		matriz[i] = matriz[i].fill(0);
	}
	console.log(matriz);
	var lc = connectionList,ci,no,nd,indexNo,indexNd;
	for (var i = lc.length - 1; i >= 0; i--) {
		ci = lc[i];
		no = ci.source;
		nd = ci.target;
		indexNo = lN.findIndex(function (item) {
			return (item == no);
		});
		indexNd = lN.findIndex(function (item) {
			return (item == nd);
		});
		matriz[indexNo][indexNd] = 1;
	};
	for (var y = 0;y < lN.length;y++) {
		console.log(lN[y].getAttribute("id"));
	};
	var buffer = "";
	for (var y = 0;y < matriz.length;y++) {
		for (var x = 0;x < matriz[y].length;x++) {
			buffer += matriz[y][x]+" "
		};
		console.log(buffer);
		buffer = "";
	};


}

function sacarNumeroNodosMaximo (tamVertices) {
	return  1+Math.sqrt(1+8*tamVertices)/2;
}
jsPlumb.ready(lanzarGui);




