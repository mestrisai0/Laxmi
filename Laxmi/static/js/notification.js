// Make all notification seen on click of bell icon
const make_noti_seen = (url) => {
  if (notification_count.innerText == "0"){
    return
  }

  method_type = 'GET'
  data = 'No data'
  $.ajax({
    type: method_type,
    dataType: "json",
    url: url,
    data: data,
    success: function (datas) {
      console.log(datas);
      notification_count.innerText = 0;
    },
  });

};
// Make all notification seen on click of bell icon

const notification_tab = (color_class, subject, text, date) => {
  var new_noti = `<a class="pl-3 my-1 notification_tab ${color_class}">
                      <div class="d-flex flex-row justify-content-between">
                          <span class="subject">${subject}</span>
                          <small class="text-secondary date">${date}</small>
                      </div>
                      <span class="message">${text}</span>
                      <span class="text-danger text-right tablecounts"></span>
                  </a>`;
  $("#notification_div_1").prepend(new_noti);
}


// Initial Setting process

var change_ip = 'localhost:8000'
console.log(change_ip);

let socket = new WebSocket(`ws://${change_ip}/ws/alert/`);


socket.open = function (e) {
  console.log("connection establishde");
};

socket.onmessage = function (e) {
  var data = JSON.parse(e.data);
  console.log(data.noti_receive);
  if (data.noti_receive) {
    notification_tab(
      data.noti_receive.color_class,
      data.noti_receive.subject,
      data.noti_receive.text,
      data.noti_receive.date,
    );
  }
};




// const notify_user = () => {


// }

