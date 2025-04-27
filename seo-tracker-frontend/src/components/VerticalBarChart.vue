<template>
  <div id="vertical-bar-chart" class="bg-white rounded-lg px-6">
    <div class="flex flex-row w-full">
      <div class="flex flex-col w-10/12">
        <h2 class="text-lg pt-8 text-gray-500">
          Quality of the Website User Experience
        </h2>
        <h1 class="text-6xl pt-4">88%</h1>
        <apexchart
          type="bar"
          height="280"
          :options="chartOptions"
          :series="series"
        ></apexchart>
      </div>
      <div class="flex flex-col justify-between py-6">
        <div class="flex flex-col gap-3">
          <h2 class="text-xl text-gray-500">Great</h2>
          <div class="flex flex-row gap-2">
            <h1 class="text-3xl">70%</h1>
            <h2 class="bg-green-50 text-green-400 p-1">+11.4%</h2>
          </div>
        </div>
        <div class="flex flex-col gap-3">
          <h2 class="text-xl text-gray-500">Need to improve</h2>
          <div class="flex flex-row gap-2">
            <h1 class="text-3xl">20%</h1>
            <h2 class="bg-green-50 text-green-400 p-1">+11.4%</h2>
          </div>
        </div>
        <div class="flex flex-col gap-3">
          <h2 class="text-xl text-gray-500">Poor</h2>
          <div class="flex flex-row gap-2">
            <h1 class="text-3xl">10%</h1>
            <h2 class="bg-green-50 text-green-400 p-1">+11.4%</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "VerticalBarChart",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [
        {
          name: "PRODUCT A",
          data: [44, 55, 41],
        },
        {
          name: "PRODUCT B",
          data: [13, 23, 20],
        },
        {
          name: "PRODUCT C",
          data: [11, 17, 15],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: false,
          },
        },
        colors: ["#FF6347", "#FF7F50", "#FFA07A"],
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: {
                position: "bottom",
              },
            },
          },
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 5,
          },
        },
        xaxis: {
          categories: ["LCP", "FLD", "CLS"],
        },
        yaxis: {
          labels: {
            formatter: function (value) {
              return `${value}%`;
            },
            show: false,
          },
        },
        legend: {
          show: false,
          position: "right",
          offsetY: 40,
        },
        grid: {
          show: false,
        },
        fill: {
          opacity: 1,
        },
        dataLabels: {
          enabled: false,
        },
      },
    };
  },
};
</script>
