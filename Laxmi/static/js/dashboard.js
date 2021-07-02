
var orders_punch = JSON.parse(
  document.getElementById("lst_to_pass").textContent
);
var orders_plate = JSON.parse(
  document.getElementById("lst_to_pass_plate").textContent
);

console.log(orders_punch, orders_plate);


// First graph **************************************************************

const data1 = {
  labels: [
    "Send Order Warning",
    "Send Order Warning",
    "Plate Warning",
    "Plate Danger",
  ],
  datasets: [
    {
      label: "Plate & Positives",
      data: orders_plate,
      backgroundColor: [
        "rgb(255, 99, 132)",
        "rgb(54, 162, 235)",
        "rgb(255, 205, 86)",
        "rgb(75, 192, 192)",
      ],
      hoverOffset: 4,
    },
  ],
};

const config1 = {
  type: "doughnut",
  data: data1,
  options: {
    plugins: {
      legend: false,
    },
  },
};

var myChart1 = new Chart(document.getElementById("myChart1"), config1);

// $(document).ready(function () {
//   var canvas = document.getElementById("myChart1");
//   var ctx = canvas.getContext("2d");
//   var myChart1 = new Chart(ctx, {
//     type: "doughnut",
//     data: data1,
//   });

//   canvas.onclick = function (evt) {
//     var activePoints = myChart1.getElementsAtEvent(evt);
//     if (activePoints[0]) {
//       var chartData = activePoints[0]["_chart"].config.data;
//       var idx = activePoints[0]["_index"];

//       var label = chartData.labels[idx];
//       var value = chartData.datasets[0].data[idx];

//       var url = value;
//       console.log(url);
//       alert("Plate Positive Progress -  " + label + " : " + url);
//     }
//   };
// });

// Second Graph ************************************************************
const labels = ["Jan", "Feb", "Mar", "Apr", "May", "June","July", "Aug", "Sep", "Oct", "Nov", "Dec"];
const data2 = {
  labels: labels,
  datasets: [
    {
      label: "Monthly orders",
      backgroundColor: "rgb(255, 99, 132)",
      borderColor: "rgb(255, 99, 132)",
      data: [0, 10, 5, 2, 20, 30, 15, 20, 2, 35, 10, 5],
    },
  ],
};

const config2 = {
  type: "line",
  data: data2,
  options: {
    plugins: {
      legend: {
        labels: {
          postition: 'bottom',
          color: "rgb(255, 99, 132)",
        },
      },
    },
    // This chart will not respond to mousemove, etc
  },
};

var myChart2 = new Chart(document.getElementById("myChart2"), config2);


// Third Graph ***********************************************************

const data3 = {
  labels: [
    "Send Order Warning",
    "Send Order Danger",
     "Punch In Progtress Warning ", 
     "Punch In Progress In Danger",
  ],
  datasets: [
    {
      label: "My First Dataset",
      data: orders_punch,
      backgroundColor: [
        "rgb(75, 192, 192)",
        "rgb(255, 99, 132)",
        "rgb(255, 205, 86)",
        "rgb(54, 162, 235)",
      ],
    },
  ],
};

const config3 = {
  type: "doughnut",
  data: data3,
  options: {
    plugins: {
      legend: false,
    },
  },
};

var myChart3 = new Chart(document.getElementById("myChart3"), config3);

// $(document).ready(function () {
//   var canvas = document.getElementById("myChart3");
//   var ctx = canvas.getContext("2d");
//   var myChart3 = new Chart(ctx, {
//     type: "doughnut",
//     data: data3,
//   });

//   canvas.onclick = function (evt) {
//     var activePoints = myChart3.getElementsAtEvent(evt);
//     if (activePoints[0]) {
//       var chartData = activePoints[0]["_chart"].config.data;
//       var idx = activePoints[0]["_index"];

//       var label = chartData.labels[idx];
//       var value = chartData.datasets[0].data[idx];

//       var url =  value;
//       console.log(url);
//       alert("Punch " + label + " : " + url);
//     }
//   };
// });

