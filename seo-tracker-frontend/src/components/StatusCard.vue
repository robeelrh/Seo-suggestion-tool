<template>
  <div class="flex gap-10">
    <div
      class="bg-white p-6 rounded-lg w-1/5 flex items-center justify-between"
    >
      <div class="flex flex-col justify-center gap-4 pt-6">
        <div class="text-4xl text-gray-800">{{ data.value }}</div>
        <div class="text-lg text-gray-500">{{ data.title }}</div>
      </div>
      <div class="flex flex-col justify-center">
        <div>
          <AreaChart />
        </div>
        <div class="text-sm text-center text-green-400">
          <span class="font-bold">{{ data.percentage }}</span>
        </div>
      </div>
    </div>

    <div
      class="bg-white px-6 rounded-lg w-1/5 flex items-center justify-between"
    >
      <div class="flex flex-col justify-center gap-3">
        <div
          v-if="Boolean(data.indexable)"
          class="text-xl text-green-400 bg-green-50 py-3 px-3 rounded-lg"
        >
          Indexable
        </div>
        <div
          v-else
          class="text-xl text-yellow-400 bg-yellow-50 py-3 px-3 rounded-lg"
        >
          Not Indexable
        </div>
        <div class="text-lg text-gray-500">{{ data.indexed }}</div>
      </div>
    </div>
    <button
      @click="runAnalyzer"
      :disabled="isAnalyzerRunning"
      class="flex items-center mt-auto border rounded-lg px-4 py-4 text-gray-500 mr-2 hover: hover:text-gray-400"
    >
      {{ isAnalyzerRunning ? "Running..." : "Run Analyzer" }}
    </button>
  </div>
</template>

<script>
import AreaChart from "@/components/AreaChart.vue";
import { useScrapersStore } from "@/store/scrapersStore";
import axios from "axios";

export default {
  components: {
    AreaChart,
  },
  data() {
    return {
      isAnalyzerRunning: false,
    };
  },
  props: ["data"],
  methods: {
    async runAnalyzer() {
      this.isAnalyzerRunning = true;

      const payload = {
        script_path: "playwright/seo_analyzer.py",
        args: { scraped_url_id: this.getScrapedUrlId.toString() },
      };
      console.log("payload: ", payload);

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/script_runner/run",
          payload
        );
        console.log("Response:", response.data);
      } catch (error) {
        console.error(
          "Error:",
          error.response ? error.response.data : error.message
        );
      } finally {
        this.isAnalyzerRunning = false;
      }
    },
  },
  computed: {
    getScrapedUrlId() {
      const store = useScrapersStore();
      return store.scrapedUrlId;
    },
  },
};
</script>
