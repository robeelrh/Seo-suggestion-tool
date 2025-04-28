<template>
  <div class="bg-white px-6 rounded-lg">
    <div class="flex justify-between items-center mb-5">
      <h2 class="text-xl font-semibold pt-8 text-gray-800">
        Issues need to Fix
      </h2>
      <button
        @click="toggleModal"
        class="text-blue-600 underline hover:text-blue-700 transition duration-300"
      >
        View all
      </button>
    </div>
    <ul class="scrollable-issues">
      <li
        v-for="(issue, index) in processedIssues"
        :key="index"
        class="flex justify-between border-gray-100 border-b-2 py-4"
      >
        <span class="text-gray-500">{{ issue.description }}</span>
        <strong class="text-red-500">{{ issue.count }}</strong>
      </li>
    </ul>

    <div
      v-if="showModal"
      class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50"
      @click.self="toggleModal"
    >
      <div
        class="relative top-20 mx-auto p-5 border w-3/4 shadow-lg rounded-md bg-white"
      >
        <div class="mt-3 text-center">
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Issues Details
          </h3>
          <div class="mt-2 px-7 py-3">
            <ul>
              <li
                v-for="(issue, index) in processedIssues"
                :key="`modal-${index}`"
                class="flex justify-between border-gray-100 border-b-2 py-2"
              >
                <span class="text-gray-500">{{ issue.description }}</span>
                <strong class="text-red-500">{{ issue.count }}</strong>
              </li>
            </ul>
          </div>
          <div class="items-center px-4 py-3">
            <button
              @click="toggleModal"
              class="px-4 py-2 bg-red-500 text-white text-base font-medium rounded-md w-24 shadow-sm hover:bg-white hover:text-black focus:outline-none focus:ring-2 focus:ring-gray-300"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiService from "@/api/service";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "IssuesSummary",
  data() {
    return {
      issues: [],
      showModal: false,
    };
  },
  computed: {
    processedIssues() {
      return this.issues
        .filter((issue) => issue.count > 0)
        .map((issue) => {
          return {
            description: issue.description,
            count: issue.count,
          };
        });
    },
  },
  methods: {
    async fetchIssues() {
      const store = useScrapersStore();
      const scraperId = store.scraperId;
      try {
        const response = await apiService.post("/scraper/get_issue_info", {
          scraper_id: scraperId,
        });
        const data = response.data;
        this.issues = this.transformResponseToIssues(data);
      } catch (error) {
        console.error("There was an error fetching the issues data:", error);
      }
    },
    transformResponseToIssues(data) {
      return Object.keys(data).map((key) => {
        let description = key.replace(/_/g, " ");
        description = this.capitalizeFirstLetter(description);

        return {
          description,
          count: data[key],
        };
      });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleModal() {
      this.showModal = !this.showModal;
    },
  },
  mounted() {
    this.fetchIssues();
  },
};
</script>

<style>
.scrollable-issues {
  max-height: 353px;
  /* Fixed height */
  overflow-y: auto;
  /* Enables vertical scrolling */
  overflow-x: hidden;
  /* Hides horizontal scrollbar */
  scrollbar-width: none;
  /* Firefox */
  -ms-overflow-style: none;
  /* Internet Explorer 10+ */
}

.scrollable-issues::-webkit-scrollbar {
  display: none;
  /* Chrome, Safari, Opera*/
}
</style>
@/store/scrapersStore
