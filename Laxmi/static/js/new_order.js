const save_btn_called = (url) => {
  if ($("#client_name_dropdown_div").hasClass("d-none")) {
    var client = $("#client_name_input").val();
  } else {
    var client = $("#client_name_dropdown").val();
  }

  if ($("#client_product_dropdown_div").hasClass("d-none")) {
    var product_pending = $("#client_product_input").val();
  } else {
    var product_pending = $("#client_product_dropdown").val();
  }
  console.log(client, product_pending);
  let csr = $("input[name=csrfmiddlewaretoken").val();

  data = {
    client: client,
    product: product_pending,
    csrfmiddlewaretoken: csr,
  };

  var method_type = "POST";

  const show_modal_of_saved_client = (response) => {
    console.log(response);

    host_port = window.location.origin
    new_path = host_port + "/pending_order_page";

    location.replace(new_path);
    // setInterval("location.reload()", 5000);
    // $("#save_pending_orders_modal_popup").modal("show");
  };

  common_ajax_call(url, data, method_type, show_modal_of_saved_client);
};
