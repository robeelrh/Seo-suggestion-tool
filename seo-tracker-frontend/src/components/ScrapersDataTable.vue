<template>
  <div class="overflow-x-auto w-full">
    <div class="bg-white rounded-lg">
      <SearchBar
        @applyFilter="fetchScraperByDate"
        title="Scrapers"
        v-model="searchQuery"
        @getStartingDate="fetchScraperByDate"
      />
    </div>
    <div>
      <table class="min-w-full bg-white">
        <thead class="sticky top-0 z-10 bg-white border-r-2 border-l-2">
          <tr>
            <th
              class="py-2 px-6 bg-gray-50 text-left font-bold uppercase text-sm text-gray-500"
            >
              Scraper ID
            </th>
            <th
              class="py-2 px-6 bg-gray-50 text-left font-bold max-w-sm uppercase text-sm text-gray-500"
            >
              Domain URL
            </th>
            <th
              class="py-2 px-6 bg-gray-50 font-bold uppercase text-sm text-gray-500"
            >
              Follow Links
            </th>
            <th
              class="py-2 px-6 bg-gray-50 font-bold uppercase text-sm text-gray-500"
            >
              Status
            </th>
            <th
              class="py-2 px-6 bg-gray-50 font-bold uppercase text-sm text-gray-500"
            >
              Created at
            </th>
          </tr>
        </thead>
        <tbody class="border">
          <tr
            v-for="(row, index) in filteredRows"
            :key="index"
            class="hover:bg-grey-lighter cursor-pointer"
            @click="selectScraper(row.scraper_id)"
          >
            <td class="py-6 px-6 text-gray-600">{{ row.scraper_id }}</td>
            <td
              class="py-6 px-6 text-gray-600 max-w-sm whitespace-normal break-words"
            >
              {{ row.domain_url }}
            </td>
            <td
              class="py-6 px-6 text-center"
              :class="getFollowLinksClass(row.follow_links)"
            >
              {{ row.follow_links == 1 ? "True" : "False" }}
            </td>
            <td class="py-6 px-6 text-center uppercase">
              <span :class="getStatusClass(row.status)">
                {{ row.status }}
              </span>
            </td>
            <td class="py-6 px-6 text-gray-600 text-center">
              {{ formatDate(row.created_at) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";
import axios from "axios";
import moment from "moment";
import { useScrapersStore } from "@/store/scrapersStore";
import { defineComponent, watch } from "@vue/composition-api";

export default defineComponent({
  components: {
    SearchBar,
  },
  data() {
    return {
      searchQuery: "",
      rows: [],
    };
  },

  mounted() {
    this.fetchData();
  },
  computed: {
    filteredRows() {
      if (!this.searchQuery) return this.rows;
      return this.rows.filter((row) =>
        row.domain_url.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    projectId() {
      const store = useScrapersStore();
      return store.projectId;
    },
  },

  watch: {
    projectId(newProjectId, oldProjectId) {
      if (newProjectId !== oldProjectId) {
        this.fetchData();
      }
    },
  },

  methods: {
    async fetchData() {
      const projectId = this.projectId;
      if (!projectId) {
        console.error("projectId is not available in sessionStorage");
        return;
      }

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/scrapers/get_all_by_project",
          {
            project_id: projectId,
          }
        );

        const data = response.data;
        this.rows = this.transformData(data);
      } catch (error) {
        console.error("There was an error fetching the data", error);
      }
    },

    async fetchScraperByDate(startingDate) {
      const projectId = this.projectId;
      if (!projectId) {
        console.error("projectId is not available in sessionStorage");
        return;
      }

      const currentDate = new Date();
      const formattedCurrentDate = currentDate.toISOString().split("T")[0];

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/dashboard/get_scraper_by_time",
          {
            project_id: projectId,
            start_date: startingDate,
            end_date: formattedCurrentDate,
          }
        );

        const data = response.data;
        this.rows = this.transformData(data);
      } catch (error) {
        console.error("There was an error fetching the data", error);
      }
    },
    transformData(data) {
      return data.map((item) => ({
        scraper_id: item.id,
        domain_url: item.domain_url,
        follow_links: item.follow_links,
        status: item.status,
        created_at: item.created_at,
        projectId: item.project_id,
      }));
    },
    getStatusClass(status) {
      switch (status) {
        case "pending":
          return "bg-yellow-50 text-yellow-400 py-3 px-3 rounded-lg";
        case "failed":
          return "bg-red-100 text-red-600 py-3 px-3 rounded-lg";
        case "completed":
          return " bg-green-50 text-green-400 py-3 px-3 rounded-lg";
        case "progress":
          return "text-red-500 bg-red-100 py-3 px-3 rounded-lg";
        default:
          return "";
      }
    },
    formatDate(date) {
      return moment(date).format("MMMM DD, YYYY hh:mm A");
    },
    getFollowLinksClass(followLinks) {
      const isFollowLinksTrue = Boolean(followLinks);
      if (isFollowLinksTrue) {
        return "text-red-600";
      } else {
        return "text-green-400";
      }
    },
    selectScraper(scraperId) {
      const store = useScrapersStore();
      store.setScraperId(scraperId);
      this.$router.push({ name: "scraperDetails", params: { id: scraperId } });
    },
  },
});
</script>
