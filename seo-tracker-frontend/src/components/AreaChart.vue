<template>
  <div id="chart">
    <apexchart
      type="area"
      :height="100"
      :width="100"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "AreaChart",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [
        {
          name: "STOCK ABC",
          data: [
            { x: new Date(2023, 0, 1), y: 34 },
            { x: new Date(2023, 1, 1), y: 43 },
            { x: new Date(2023, 2, 1), y: 31 },
            { x: new Date(2023, 3, 1), y: 43 },
            { x: new Date(2023, 4, 1), y: 33 },
            { x: new Date(2023, 5, 1), y: 52 },
          ],
        },
      ],
      chartOptions: {
        chart: {
          type: "area",
          height: 350,
          toolbar: {
            show: false, // This will remove the toolbar
          },
          zoom: {
            enabled: false,
          },
        },
        colors: ["#32CD32"], // Green color for the area
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth", // Smooth curve
          width: 1, // This will make the stroke narrower
        },
        xaxis: {
          type: "datetime",
          labels: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
        },
        yaxis: {
          opposite: true,
          labels: {
            show: false,
          },
        },
        legend: {
          horizontalAlign: "left",
        },
        grid: {
          show: false, // This will remove the gridlines
        },
        tooltip: {
          x: {
            format: "dd MMM yyyy",
          },
        },
      },
    };
  },
};
</script>
