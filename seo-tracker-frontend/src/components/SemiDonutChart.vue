<template>
  <div id="health-score-chart" class="bg-white rounded-lg px-6">
    <h2 class="text-xl font-semibold pt-8 text-gray-800">Health Score</h2>
    <apexchart
      type="donut"
      height="405"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "SemiDonutChart",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: "donut",
        },
        plotOptions: {
          pie: {
            size: "70%",
            donut: {
              labels: {
                show: true,
                total: {
                  show: true,
                  showAlways: true,
                  label: "Score",
                  formatter(W) {},
                },
              },
            },
            startAngle: -90,
            endAngle: 90,
            offsetY: 0,
          },
        },
        grid: {
          padding: {
            bottom: -80,
          },
        },
        colors: ["#FF6347", "#D3D3D3"],
        legend: {
          show: false,
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: {
                position: "bottom",
                show: false,
              },
            },
          },
        ],
      },
      health: 0,
    };
  },

  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const store = useScrapersStore();
      const scraperId = store.scraperId;
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/scraper/get_health_info",
          {
            scraper_id: scraperId,
          }
        );

        // this.series = [90, 10]
        this.series = [
          response.data.health_precentage,
          100 - response.data.health_precentage,
        ];
        // this.chartKey++
      } catch (error) {
        console.error("There was an error fetching the data", error);
      }
    },
  },
};
</script>
