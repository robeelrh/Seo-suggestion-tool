<template>
  <div id="status-code-chart" class="bg-white rounded-lg px-6">
    <h2 class="text-xl font-semibold pt-8 text-gray-800">
      Pages Status Code Status
    </h2>
    <apexchart
      type="bar"
      height="353"
      :options="chartOptions"
      :series="series"
      :key="chartKey"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "axios";
import { useScrapersStore } from "@/store/scrapersStore";
// import { setTimeout } from 'core-js';

export default {
  name: "StatusCodeBarChart",
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      series: [
        {
          name: "Status Code",
          data: [],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            horizontal: true,
            distributed: true,
            barHeight: "40%",
          },
        },
        colors: ["#ff3e14", "#FF7F50"],
        legend: {
          show: false,
        },
        dataLabels: {
          enabled: false,
        },
        xaxis: {
          categories: ["Indexable", "Not Indexable"],
        },
        yaxis: {
          labels: {
            style: {
              colors: "#c8c7c6",
              fontSize: "14px",
            },
          },
        },
        grid: {
          borderColor: "#f1f1f1",
          xaxis: {
            lines: {
              show: true,
            },
          },
          yaxis: {
            lines: {
              show: false,
            },
          },
        },
        tooltip: {
          enabled: false,
        },
      },
      chartKey: 0,
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
          "http://127.0.0.1:8000/api/scraper/get_page_status_code_status",
          {
            scraper_id: scraperId,
          },
        );
        this.series[0]["data"] = [
          response.data.indexable_url_count,
          response.data.non_indexable_url_count,
        ];
        this.chartKey++;
      } catch (error) {
        console.error("There was an error fetching the data", error);
      }
    },
  },
};
</script>
