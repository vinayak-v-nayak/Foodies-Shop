$.ajax({
            url:  "dummy?parameter1=Dosa",
            method: 'GET',
            dataType: 'json',  // Ensures the response is treated as JSON
            success: function(data) {
            console.log(data);
            let item = document.getElementById("name_section");
            if (item) {
                item.innerHTML = data["FoodName"] ? data["FoodName"] : "No food found";
            }
        },
        error: function(xhr, status, error) {
            console.error("AJAX Error:", error);
        }

       
        
    });


    let item = document.getElementById("name_section")
                    item.innerHTML = data["name"];


                    <h1 id= "name_section"></h1>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>