$(function(){
    $('.alert').delay(3000).fadeOut();
    $(".search").on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13) {
        e.preventDefault();
        return false;
        }
     });
    
    $(".search").keyup(function(){

        var sapid = $('#sapid').val();
        var hostname = $('#hostname').val();
        var loopback = $('#loopback').val();
        var mac_address = $('#mac_address').val();
        
		var url = '/list'; // Backend url
		var params = {'sapid':sapid, 'hostname':hostname,'loopback':loopback,'mac_address':mac_address}; // Search field value
		fetchData(url, params); // Backend call for filtered data
	}).trigger('keyup');

});

function fetchData(url, params) {
    // Call the backend
    
    $.get(url, params)
    .done(function(data){
        console.log("Hi");
        // Put the data into target div
        $("#results").html(data);
        console.log(data);
        // Get next page on navigation button click
        $(".previous, .next").click(function(elem){
            // Prevent button from taking you away from current page
            elem.preventDefault();
            // Get the page's url from the button clicked
            var url = '/list' + $(this).attr('href');

            // Call this function again with url containing page parameter
            fetchData(url, params);
        });
    });
};

function showdelete(id)
    {
        var status = 0;
        $('#autoid').val(id);
        $('#myModal').modal('show');
    }

function deleterouters()
    {
        var deleteid= $('#autoid').val();
        url='/delete/'+deleteid;
        $.ajax({
            type: 'GET',
            url:url,
            dataType: 'json',
            success: function(data) {

                if(data.message ==0)
                {
                    toastr["error"]('Something Went Wrong');
                }
                else{
                    $('#myModal').modal('hide');
                    $("#delete_success").show();
                    $('#delete_success').delay(3000).fadeOut();

                   $(".search").keyup(function(){
                        var sapid = $('#sapid').val();
                        var hostname = $('#hostname').val();
                        var loopback = $('#loopback').val();
                        var mac_address = $('#mac_address').val();

                        var url = '/list'; // Backend url
                        var params = {'sapid':sapid, 'hostname':hostname,'loopback':loopback,'mac_address':mac_address}; // Search field value
                        fetchData(url, params); // Backend call for filtered data
                   }).trigger('keyup');
                }
            },
            error: function(data) { // if error occured
                alert("Error occurred. Please try again!");
            }
        });
    }
   
   
