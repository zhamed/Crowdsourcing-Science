
$(document).ready(function(){
  /*window.alert("boo");*/
  /*$('#zoom').elevateZoom({
  	zoomType: "inner",
  	cursor: "crosshair",
  	easing : true
  });*/
  
  Shadowbox.init({
    handleOversize: "resize",
    modal: true
  });

  /*var options = {  
            zoomType: 'innerzoom',  
            preloadImages: true 
    };  
    $('.MYCLASS').jqzoom(options);   */
/*
    var sketchpad = Raphael.sketchpad("editor", {
		width: 200,
		height: 200,
		editing: true
	});

	// When the sketchpad changes, update the input field.
	sketchpad.change(function() {
		$("#sketchpad-data").val(sketchpad.json());
	});
*/
	/*$( "#dialog-modal" ).dialog({
		autoOpen : false,
		modal: true,
		show : "blind", 
		hide : "blind"
	});*/

	/*$("#contactus").click(function() {
		window.alert("hi");
    	$("#dialog-modal").dialog({
    		modal:true
    	});
  	});

  	window.alert("hi");*/

	
	/*$('#get-json').click(function() {
    	window.alert("The Json is: " + $('input[name=sketchpad-data]').val());
    });*/

    /*$('#btn').click(function() {
    	window.alert($('#myModal').name);
        $('#myModal').modal('show');
    });*/
});

function popup() {
  window.alert('hi');

}

var script = "<script>var sketchpad = Raphael.sketchpad('editor', {width: 200,height: 200,editing: true});sketchpad.change(function() {$('#sketchpad-data').val(sketchpad.json());});</script>"

function openMessage(test, image_url) {
    Shadowbox.open({
        player:     "html",
        title:      "Explanation",
        //content:    '<div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='sketchpad-edit'><div class='editor'></div><img src='" + test + "' width='50%'/></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>',
        content:    '<input type="hidden" name="data" /><div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='sketchpad-background' align='center' style='width:325px; height:240px; display: inline-block; background-size: cover; z-index=9999999; background-image: url(\"" + test + "\"" + ");\'>" + "<div id='editor'></div></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>' + script,        
        //content:    '<div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='editor'></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>',
        width:      1200,
        height:     480,
    });
}

/*
function openMessage(test, image_url) {
    Shadowbox.open({
        player:     "html",
        title:      "Explanation",
        //content:    '<div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='sketchpad-edit'><div class='editor'></div><img src='" + test + "' width='50%'/></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>',
        content:    '<input type="hidden" name="data" /><div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='sketchpad-background' align='center' style='width:325px; height:240px; display: inline-block; background-size: cover; z-index=9999999; background-image: url(\"" + test + "\"" + ");\'>" + "<div id='editor'></div></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>',        
        //content:    '<div style="padding:10px;text-align:left;background:#000;z-index:99999999"><font color="white"><b>Explain your answer by drawing an outline around the part of the image you think contains the character.</b></font>' + "<div class='editor'></div>" + "<img src='" + image_url + "' width='50%'/>" + '</div>',
        width:      1200,
        height:     480
    });
}

*/






