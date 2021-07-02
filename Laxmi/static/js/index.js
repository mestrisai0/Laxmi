$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $(this).toggleClass("active");
  });
});

var minDate, maxDate;

// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
  parts = data[3].split('/')
  var mydate = new Date(parts[2], parts[1] - 1, parts[0]);
  var min = minDate.val();
  var max = maxDate.val();
  var date = new Date(mydate);

  if (
    (min === null && max === null) ||
    (min === null && date <= max) ||
    (min <= date && max === null) ||
    (min <= date && date <= max)
  ) {
    return true;
  }
  return false;
});

$(document).ready(function () {
  // Create date inputs
  minDate = new DateTime($("#min"), {
    format: "D/MM/YYYY",
  });
  maxDate = new DateTime($("#max"), {
    format: "D/MM/YYYY",
  });

  // DataTables initialisation
  var table = $("#Ordertable").DataTable({
                ordering: false,
                dom: "Bfrtip",
                buttons: ["excel", "pdf"],
              });

  // Refilter the table
  $("#min, #max").on("change", function () {
    table.draw();
  });
});

// $(document).ready(function () {
  
// });
// Csrf token start

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim(); // Does this cookie string begin withthe name we want ?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

// Csrf token end

// All variable initiazation start

var client_name_dropdown = document.getElementById("client_name_dropdown");
var client_name_dropdown_div = document.getElementById(
  "client_name_dropdown_div"
);

var client_name_input = document.getElementById("client_name_input");
var client_name_input_div = document.getElementById("client_name_input_div");

var client_product_dropdown_div = document.getElementById(
  "client_product_dropdown_div"
);
var client_product_dropdown = document.getElementById(
  "client_product_dropdown"
);

var client_product_input = document.getElementById("client_product_input");
var client_product_input_div = document.getElementById(
  "client_product_input_div"
);

var order_confirm_checkbox = document.getElementById("order_confirm_checkbox");
var new_order_after_checkbox_div = document.getElementById(
  "new_order_after_checkbox_div"
);



var punch_input_div = document.getElementById("punch_input_div");
var checkpunch = document.getElementById("checkpunch");
var punch_input = document.getElementById("punch_input");

var punch_status_div = document.getElementById("punch_status_div");
var punch_status = document.getElementById("punch_status");

var board_id_div = document.getElementById("board_id_div");
var board_id = document.getElementById("board_id");

var plate_and_positive_status_div = document.getElementById(
  "plate_and_positive_status_div"
);
var plate_and_positive_status = document.getElementById(
  "plate_and_positive_status"
);

var build_location_div = document.getElementById("build_location_div");
var build_location = document.getElementById("build_location");

var logo_check_div = document.getElementById("logo_check_div");
var logo_check = document.getElementById("logo_check");

var company_box_div = document.getElementById("company_box_div");
var company_box = document.getElementById("company_box");

var keyline_div = document.getElementById("keyline_div");
var keyline = document.getElementById("keyline");

var negative_div = document.getElementById("negative_div");
var negative = document.getElementById("negative");

var positive_div = document.getElementById("positive_div");
var positive = document.getElementById("positive");

var proofless_file_div = document.getElementById("proofless_file_div");
var proofless_file = document.getElementById("proofless_file");

var embose_div = document.getElementById("embose_div");
var embose = document.getElementById("embose");

var spotuv_div = document.getElementById("spotuv_div");
var spotuv = document.getElementById("spotuv");

var foiling_div = document.getElementById("foiling_div");
var foiling = document.getElementById("foiling");

var perforation_div = document.getElementById("perforation_div");
var perforation = document.getElementById("perforation");

var carton_style_div = document.getElementById("carton_style_div");
var carton_style = document.getElementById("carton_style");

var paper_type_div = document.getElementById("paper_type_div");
var paper_type = document.getElementById("paper_type");

var colors_div = document.getElementById("colors_div");
var colors = document.getElementById("colors");

var due_date_div = document.getElementById("due_date_div");
var due_date = document.getElementById("due_date");

var job_priority_div = document.getElementById("job_priority_div");
var job_priority = document.getElementById("job_priority");

var file_upload_div = document.getElementById("file_upload_div");
var file_upload_input = document.getElementById("file_upload_input");

var input_file_div = document.getElementById("input_file_div");
var input_file = document.getElementById("input_file");

var submit_btn = document.getElementById("submit_btn");
var save_btn = document.getElementById("save_btn");

// modal in dashboard
var showPunch = document.getElementById("showPunch");

var edit_table_row_dashboard = document.getElementById("edit_table_row_dashboard");

var delete_punch = document.getElementById("delete_punch");

var notification_div = document.getElementById("notification_div");
var notification_count = document.getElementById("notification_count");
var notify_user_select = document.getElementById("notify_user_select");
var notify_description = document.getElementById("notify_description");
var notify_user_submit = document.getElementById("notify_user_submit");



// All variable initiazation end


// checkbox on click show rest divs in new order form inside common_order_code.html
order_confirm_checkbox.onclick = function () {
  // console.log("hereee");
  if (this.checked) {
    new_order_after_checkbox_div.classList.remove("d-none");
    submit_btn.classList.remove("d-none");
    save_btn.classList.add("d-none");
  } else {
    new_order_after_checkbox_div.classList.add("d-none");
    submit_btn.classList.add("d-none");
    save_btn.classList.remove("d-none");
  }
};

// Common Ajax Code

const common_ajax_call = (url, data, method_type, success_function_name) => {
  $.ajax({
    type: method_type,
    headers: {
      "X-CSRFToken": csrftoken,
    },
    dataType: "json",
    url: url,
    data: data,
    success: function (datas) {
      console.log(datas, "In common ajax code");
      success_function_name(datas);
    },
  });
};

// Common Ajax code

// Common submit code

const submit_btn_called = (url) => {

  
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

  // punch_input = punch_input.value;
  punch_status = punch_status.value;
  board_id = board_id.value;
  plate_and_positive_status = plate_and_positive_status.value;
  build_location = build_location.value;
  logo_check = logo_check.value;
  company_box = company_box.value;
  keyline = keyline.value;
  negative = negative.value;
  positive = positive.value;
  proofless_file = proofless_file.value;
  embose = embose.value;
  spotuv = spotuv.value;
  foiling = foiling.value;
  perforation = perforation.value;
  carton_style = carton_style.value;
  paper_type = paper_type.value;
  colors = colors.value;
  due_date = due_date.value;
  job_priority = job_priority.value;

  // sid = $(".btn_model_from").attr("data-sid");
  sid = localStorage.getItem("row_id");

  path = window.location.pathname

  var File = input_file.files[0];
  var formData = new FormData();

  if (path.includes("new_order")) {
    formData.append("sid", "create");
  } else {
    formData.append("sid", sid);
  }

  
  formData.append("file", File);
  formData.append("client", client);
  formData.append("product", product_pending);
  formData.append("logo", logo_check);

  
  formData.append("location", build_location);
  formData.append("company_box", company_box);
  formData.append("keyline", keyline);
  formData.append("negative", negative);
  formData.append("positive", positive);
  formData.append("proofless_file", proofless_file);
  formData.append("embose", embose);
  formData.append("spotuv", spotuv);
  formData.append("foiling", foiling);
  formData.append("perforation", perforation);
  formData.append("carton_style", carton_style);
  formData.append("paper_type", paper_type);
  formData.append("colors", colors);
  formData.append("board_id_new", board_id);

  formData.append("due_date", due_date);
  formData.append("job_priority", job_priority);
  formData.append("punch_status", punch_status);
  formData.append("plate_and_positive_status", plate_and_positive_status);

  $.ajax({
    type: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    processData: false,
    contentType: false,
    data: formData,
    url: url,
    success: function (response) {
      console.log(response);
      window.location.reload();
    },
  });
};

// Common submit code

// Common modal edit form
$(".btn_model_from").on("click", function () {
  client_name_dropdown_div.classList.add("d-none");
  client_name_input_div.classList.remove("d-none");
  client_product_dropdown_div.classList.add("d-none");
  client_product_input_div.classList.remove("d-none");
  new_order_after_checkbox_div.classList.remove("d-none");
  submit_btn.classList.remove("d-none");
  save_btn.classList.add("d-none");

  id = $(this).attr("data-sid");
  url = $(this).attr("id");

  localStorage.setItem("row_id", id);

  console.log(id, url);
  data_form = {
    sid: id,
  };

  const fill_value_in_edit = (data) => {
    if (data.status == "Save") {
      x = data.data_form;

      x.map((item) => {
        client_name_input.value = data.client_name_pass;
        client_product_input.value = data.product_name_pass;
        punch_status.value = item.punch_status;
        board_id.value = item.board_id_id;
        plate_and_positive_status.value = item.plate_status;
        build_location.value = data.location_pass;
        logo_check.value = item.logo;
        company_box.value = item.company_box;
        keyline.value = item.keyline;
        negative.value = item.negative;
        positive.value = item.positive;
        proofless_file.value = item.proofless_file;
        embose.value = item.EMBOSE;
        spotuv.value = item.spotuv;
        foiling.value = item.Foiling;
        perforation.value = item.Perforation;
        carton_style.value = item.carton_style;
        paper_type.value = item.paper_type;
        colors.value = item.product_colors;
        due_date.value = item.due_date;
        job_priority.value = item.priority;

        $("#get_id").val(item.id);
      });
    }
  };

  common_ajax_call(url, data_form, "GET", fill_value_in_edit);
});
// Common modal edit form

// Common punch modal fill data

const common_punch_fill_data = (x) => {
  for (i = 0; i < x.length; i++) {
    output += `<tr value= "${x[i].id}" class = 'side-link' value2 = "${x[i].punch_no}">
                    <td>${x[i].id}</td>
                    <td>${x[i].client_product_id_id}</td>
                    <td>${x[i].punch_no}</td>
                    <td>${x[i].size}</td>
                    <td>${x[i].ups}</td>
                    <td>${x[i].design}</td>
                    <td>${x[i].tuck_in_flap}</td>
                    <td>${x[i].cam_pam}</td>
                    <td>${x[i].plate_maker}</td>
                    <td>${x[i].plate_maker_code}</td>
                    <td>${x[i].remark}</td>
                    <td>${x[i].location_id}</td>
                </tr>`;
  }

  return output
}

// Common punch modal fill data

// Common check punch code
const check_punch_modal = (url) => {
  var punch_val = punch_input.value;

  if (!punch_val) {
    alert("Please Input Punch value");
    return;
  }

  var data = {
    punches: punch_val,
  };
  var method_type = "POST";

  const show_modal_of_punch_value = (datas) => {

    output = "";
    x = datas.response_punches;

    //   let h = "board_";
    if (x.length == 0) {
      var message = "Borad is not available";
      output += `<p> ${message} </p>`;
      $(".mdal-b").html(output);
      $(".board_not_avlable").modal("show");
      $(".board_not_avlable").on("click", "#not_available", function () {
        var op = "Not Available";
        // board_id.value = op;
        punch_status.value = 'Send Order'
        $(".board_not_avlable").modal("hide");
        edit_table_row_dashboard.style.overflowY = 'auto'

      });
    } else {
      
      output = common_punch_fill_data(x)

      $(".punch_table_fill").html(output);
      $("#showPunch").modal("show");

      //console.log(id);
      $("#showPunch").on("click", ".side-link", function () {
        var id = $(this).attr("value");
        board_id.value = id
        punch_status.value = "Available";
        $("#showPunch").modal("hide");
        edit_table_row_dashboard.style.overflowY = "auto";
      });
    }
  };

  common_ajax_call(url, data, method_type, show_modal_of_punch_value);
  //   });
  // });
};
// Common check punch code



// Cancel Order
$(".cancel_order_call").on("click", function () {
    id = $(this).attr("data-sid");
    url = $(this).attr("id");
    
    console.log(url)

    data_form = {
      sid: id,
    };

    const succes_func_after_cancel = (data) => {
      console.log($(this));
      $(this).parents("tr").remove();
    }


    common_ajax_call(url, data_form, "GET", succes_func_after_cancel);
});
// Cancel Order


// select 2dependent dropdown 
const depedent_dropdown_client_product = (url) => {

    var optionValues = [];
    $("#client_name_dropdown option").each(function () {
        optionValues.push($(this).val());
    });
    $("#client_name_dropdown")
    .select2({})
    .on("select2:select", function (e) {
      var element = $(this);
      var new_category = $.trim(element.val());

      if (new_category == "Create New Client") {
        client_name_dropdown_div.classList.add("d-none");
        client_name_input_div.classList.remove("d-none");
        client_product_dropdown_div.classList.add("d-none");
        client_product_input_div.classList.remove("d-none");
      } else {
        var data = {
          client: $("#client_name_dropdown option:selected").val(),
        };
        var method_type = "POST";

        const client_name_product_dropdown = (datas) => {
          htmlcollectionarray = client_product_dropdown.getElementsByTagName(
            "option"
          );
          all_option = [];
          for (var i = htmlcollectionarray.length - 1; i >= 2; --i) {
            htmlcollectionarray[i - 1].remove();
          }
          for (i in datas.response_products) {
            $("#client_product_dropdown option:first-child").after(
              `<option>${datas.response_products[i]}</option>`
            );
          }
        };

        common_ajax_call(url, data, method_type, client_name_product_dropdown);
      }
    });
    $("#client_product_dropdown")
    .select2({})
    .on("select2:select", function (e) {
      var element = $(this);
      var new_category = $.trim(element.val());

      if (new_category == "Create New Product") {
        client_product_dropdown_div.classList.add("d-none");
        client_product_input_div.classList.remove("d-none");
      }
    });
};

// Hide input dropdown
const hideInputDropdown = (data) => {
  if (data == "client_name") {
    client_name_input_div.classList.add("d-none");
    client_name_dropdown_div.classList.remove("d-none");
    client_product_input_div.classList.add("d-none");
    client_product_dropdown_div.classList.remove("d-none");

    dropdown_width = client_name_dropdown.getElementsByTagName("span")[0].style
      .width;
    client_product_dropdown.getElementsByTagName(
      "span"
    )[0].style.width = dropdown_width;
  } else {
    client_product_input_div.classList.add("d-none");
    client_product_dropdown_div.classList.remove("d-none");
  }
};
