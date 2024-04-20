// SPDX-FileCopyrightText: 2022 Martin Bednář
//
// SPDX-License-Identifier: GPL-3.0-or-later

function getRandomValuesArray() {
	var array = new Uint32Array(4);
	window.crypto.getRandomValues(array);
	
	var ul = document.getElementById("getRandomValues");
	
	for (var i = 0; i < array.length; i++) {
		var li = document.createElement("li");
		li.appendChild(document.createTextNode(array[i]));
		ul.appendChild(li);
	}
}

function getArrays() {
	getRandomValuesArray();
}
