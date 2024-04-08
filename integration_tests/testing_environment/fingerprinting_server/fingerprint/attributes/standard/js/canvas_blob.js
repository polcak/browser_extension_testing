function get_blob_canvas(name) {
    try {
        var canvas = document.getElementById(name);
        return new Promise(function(resolve, reject) {
            canvas.toBlob(function(blob) {
                if (blob) {
                    resolve(blob.arrayBuffer().then(a => Array.from(new Int8Array(a))));
                } else {
                    resolve("Blob is null or undefined");
                }
            });
        });
    } catch (error) {
        return "ERROR";
    }
}

(function() {
    api.register("canvas_blob", async function () {
        try {
            var canvas_blob = {
                'name': 'canvas_blob',
                'data': '0'};

            canvas_blob.data = await get_blob_canvas('canvasx');
        } catch(e){
            canvas_blob.data = "Not supported " + e;
        }
        return canvas_blob;
    });
})();
