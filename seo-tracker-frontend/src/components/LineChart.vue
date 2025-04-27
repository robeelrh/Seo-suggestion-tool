<template>
  <div id="chart" class="bg-white rounded-lg px-6">
    <h2 class="text-xl font-semibold pt-8 text-gray-800">
      Improvements Over Time
    </h2>
    <apexchart
      :type="'line'"
      :height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
import moment from "moment";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "LineChart",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {},
    };
  },
  mounted() {
    this.initChartOptions();
    this.fetchData();
  },
  methods: {
    initChartOptions() {
      this.chartOptions = {
        chart: {
          height: 350,
          type: "line",
          toolbar: {
            show: false,
          },
        },
        colors: ["#FF6347"], // Red color for the line
        xaxis: {
          type: "datetime",
          labels: {
            formatter: function (val) {
              return moment(val).format("DD-MM-YY"); // Format the date
            },
            style: {
              colors: Array(7).fill("#A3A3A3"), // Gray color for x-axis labels
            },
          },
        },
        yaxis: {
          labels: {
            style: {
              color: "#A3A3A3", // Gray color for y-axis labels
            },
            formatter: function (val) {
              return val.toFixed(0); // Rounds the value to the nearest whole number
            },
          },
          title: {
            style: {
              color: "#A3A3A3", // Gray color for y-axis title
            },
          },
        },
      };
    },
    fetchData() {
      const store = useScrapersStore();
      const projectId = store.projectId;

      axios
        .post("http://127.0.0.1:8000/api/dashboard/get_scraper_performance", {
          project_id: projectId,
        })
        .then((response) => {
          const performanceData = response.data.scraperPerformanceResults;
          const seriesData = performanceData.map((item) => ({
            x: new Date(item.started_at).getTime(),
            y: item.percentage_weight,
          }));

          this.series = [
            {
              name: "Performance",
              data: seriesData,
            },
          ];
        })
        .catch((error) => {
          console.error("Error fetching performance data:", error);
        });
    },
  },
};
</script>
