<template>
  <div class="bg-gray-50 p-8 w-full max-h-full">
    <div>
      <div class="flex justify-end items-center w-full">
        <button
          @click="runScaper"
          :disabled="isScraperRunning"
          class="flex items-center border rounded-lg px-4 py-4 text-gray-500 mr-2 hover: hover:text-gray-400"
        >
          {{ isScraperRunning ? "Running..." : "Run Scraper" }}
        </button>
        <button
          @click="showAddModal = true"
          class="flex items-center border rounded-lg px-4 py-4 text-gray-500 mr-2 hover:text-gray-400"
        >
          Add Project
        </button>
        <button
          @click="showSelectModal = true"
          class="flex items-center border rounded-lg px-4 py-4 text-gray-500 mr-2 hover:text-gray-400"
        >
          Select Project
        </button>
        <button
          class="flex items-center border rounded-lg px-4 py-4 text-gray-500"
        >
          <img src="/icons/calendar.svg" alt="calendar Icon" />
          <span class="ml-2">Select Date</span>
        </button>
      </div>
      <div class="py-6">
        <div class="flex space-x-4">
          <StatisticCard :data="pagesCrawled" />
          <StatisticCard :data="crawlingFrequency" />
          <StatisticCard :data="crawlingSpeed" />
        </div>
      </div>
      <div class="py-6">
        <LineChart />
      </div>
      <div class="py-6">
        <ScrapersDataTable />
      </div>
    </div>
    <template v-if="showAddModal">
      <ModalAddProject @close-modal="handleCloseAddModal" />
    </template>
    <template v-if="showSelectModal">
      <ModalSelectProject
        @close-modal="handleCloseSelectModal"
        @select-project="handleSelectProject"
      />
    </template>
  </div>
</template>

<script>
import LineChart from "@/components/LineChart.vue";
import ScrapersDataTable from "@/components/ScrapersDataTable.vue";
import StatisticCard from "@/components/StatisticCard.vue";
import ModalAddProject from "@/components/ModalAddProject.vue";
import ModalSelectProject from "@/components/ModalSelectProject.vue";
import { stats as cardData } from "@/Data/statistics";
import { useScrapersStore } from "@/store/scrapersStore";
import axios from "axios";

export default {
  components: {
    LineChart,
    ScrapersDataTable,
    StatisticCard,
    ModalAddProject,
    ModalSelectProject,
  },
  data() {
    return {
      cardData: cardData,
      isScraperRunning: false,
      crawlingFrequency: {
        title: "Crawling Frequency",
        value: "",
        percentage: "122.2%",
      },
      pagesCrawled: {
        title: "Pages crawled",
        value: 0,
        percentage: "122.2%",
      },
      crawlingSpeed: {
        title: "Speed of crawling",
        value: 0,
        percentage: "122.2%",
      },
      showAddModal: false,
      showSelectModal: false,
    };
  },
  computed: {
    getProjectId() {
      const store = useScrapersStore();
      return store.projectId;
    },
  },
  methods: {
    async runScaper() {
      console.log("runScaper called");
      this.isScraperRunning = true;

      const payload = {
        script_path: "playwright/main.py",
        args: { project_id: this.getProjectId.toString() },
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
        this.isScraperRunning = false;
      }
    },

    async runAnalytics() {
      await this.fetchCrawlingFrequency();
      await this.fetchCrawlingSpeed();
      await this.fetchPagesCrawled();
    },
    async fetchCrawlingFrequency() {
      const projectId = this.getProjectId;
      if (!projectId) {
        console.error("projectId is not available in sessionStorage");
        return;
      }
      axios
        .post("http://127.0.0.1:8000/api/dashboard/get_crawling_frequency", {
          project_id: projectId,
        })
        .then((response) => {
          const data = response.data;
          this.crawlingFrequency.value = data.crawling_frequency;
        })
        .catch((error) => {
          console.error("There was an error fetching the data", error);
        });
    },
    async fetchCrawlingSpeed() {
      const projectId = this.getProjectId;
      if (!projectId) {
        console.error("projectId is not available in sessionStorage");
        return;
      }
      axios
        .post("http://127.0.0.1:8000/api/dashboard/get_crawler_speed", {
          project_id: projectId,
        })
        .then((response) => {
          const data = response.data;
          this.crawlingSpeed.value = data.crawler_speed;
        })
        .catch((error) => {
          console.error("There was an error fetching the data", error);
        });
    },
    async fetchPagesCrawled() {
      const projectId = this.getProjectId;
      if (!projectId) {
        console.error("projectId is not available in sessionStorage");
        return;
      }
      axios
        .post("http://127.0.0.1:8000/api/dashboard/get_crawled_urls_count", {
          project_id: projectId,
        })
        .then((response) => {
          const data = response.data;
          this.pagesCrawled.value = data.crawled_urls;
        })
        .catch((error) => {
          console.error("There was an error fetching the data", error);
        });
    },
    handleCloseAddModal() {
      this.showAddModal = false;
    },
    handleCloseSelectModal() {
      this.showSelectModal = false;
    },
    async handleSelectProject(projectId) {
      useScrapersStore().setProjectId(projectId);
      await this.runAnalytics();
    },
  },

  async created() {
    await this.runAnalytics();
  },
};
</script>
import { MAIN_SCRIPT } from "@/env";
