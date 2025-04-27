<template>
  <div>
    <div class="w-100 max-w-4xl mx-auto my-4 py-5 text-center">
      <div class="pt-5 py-3 px-4 sm:px-0 flex-col justify-between">
        <h3 class="text-3xl font-semibold leading-7 text-gray-900">
          Compare Scrapers & their features
        </h3>
        <p class="py-3 text-sm">
          Compare scrapers to know the difference and check functionality
        </p>
      </div>

      <div class="mt-6 border-t border-gray-100">
        <dl class="divide-y divide-gray-100">
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-2 sm:px-0">
            <dt
              class="text-md font-medium leading-6 text-gray-900 flex-col justify-center"
            >
              Features
            </dt>
            <DropDownButton
              :label="'Scraper ' + currentScraperId"
              :options="dropDownOptions"
              @change="setCurrentScraperId"
            />
            <DropDownButton
              :label="'Scraper ' + otherScraperId"
              :options="dropDownOptions"
              @change="setOtherScraperId"
            />
          </div>
          <div v-for="(feature, index) in scraperFeatures" :key="index">
            <ScraperCompareTableRow
              :featureName="String(feature)"
              :scraper1Detail="String(currentScraperDetails[feature])"
              :scraper2Detail="String(otherScraperDetails[feature])"
            />
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<script>
import ScraperCompareTableRow from "@/components/ScraperCompareTableRow.vue";
import DropDownButton from "@/components/DropDownButton.vue";
import { useScrapersStore } from "@/store/scrapersStore";
import axios from "axios";

export default {
  name: "ScraperCompareTable",
  components: {
    ScraperCompareTableRow,
    DropDownButton,
  },
  data() {
    return {
      scrapers: [],
      dropDownOptions: {},
      currentScraperId: null,
      otherScraperId: null,
      currentScraperDetails: {},
      otherScraperDetails: {},
      features: {},
    };
  },
  computed: {
    scraperFeatures() {
      return this.features;
    },
  },
  methods: {
    async fetchAllScrapers(projectId) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/scrapers/get_all_by_project",
          {
            project_id: projectId,
          }
        );
        this.scrapers = response.data;

        this.features = Object.keys(this.scrapers[0]);
        const store = useScrapersStore();
        this.currentScraperId = store.scraperId;

        this.currentScraperDetails = this.scrapers.find(
          (scraper) => scraper.id === this.currentScraperId
        );
        this.otherScraperId = this.scrapers.find(
          (scraper) => scraper.id !== this.currentScraperId
        ).id;
        this.otherScraperDetails = this.scrapers.find(
          (scraper) => scraper.id === this.otherScraperId
        );
        this.scrapers.forEach((scraper) => {
          this.dropDownOptions["Scraper " + scraper.id] = scraper.id;
        });
      } catch (error) {
        console.error("Error fetching all scrapers:", error);
      }
    },
    setCurrentScraperId(id) {
      this.currentScraperId = id;
      this.currentScraperDetails = this.scrapers.find(
        (scraper) => scraper.id === id
      );
    },
    setOtherScraperId(id) {
      this.otherScraperId = id;
      this.otherScraperDetails = this.scrapers.find(
        (scraper) => scraper.id === id
      );
    },
  },
  mounted() {
    const store = useScrapersStore();
    const projectId = store.projectId;
    this.fetchAllScrapers(projectId);
  },
};
</script>
