<template>
  <div
    class="fixed inset-0 z-50 flex items-center justify-center bg-gray-800 bg-opacity-75"
  >
    <div class="relative p-4 w-full max-w-md max-h-full">
      <div class="relative bg-white rounded-lg shadow">
        <div
          class="flex items-center justify-end p-2 md:p-3 border-b rounded-t dark:border-gray-600"
        >
          <button
            @click="closeModal"
            type="button"
            class="end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center"
          >
            <svg
              class="w-3 h-3"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 14"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
              />
            </svg>
          </button>
        </div>
        <div class="p-4 md:p-5">
          <h3 class="font-bold mb-2">All Projects</h3>
          <ul class="max-h-80 overflow-auto">
            <li v-if="showNoProjectsError">No projects available.</li>
            <li
              v-else
              v-for="project in projectList"
              :key="project.id"
              @click="selectedProjectId = project.id"
              class="mb-2 px-2 py-1 rounded-md"
              :class="
                selectedProjectId === project.id
                  ? 'text-white bg-red-500'
                  : ' bg-gray-100 text-black'
              "
            >
              <p class="text-sm font-semibold">
                URL: <span class="font-normal">{{ project.url }}</span>
              </p>
              <p class="text-xs font-semibold">
                Max Pages to Crawl:
                <span class="font-normal">
                  {{ project.max_pages_to_crawl }}
                </span>
              </p>
              <p class="text-xs font-semibold">
                Crawling Frequency:
                <span class="font-normal">{{
                  project.crawling_frequency
                }}</span>
              </p>

              <p class="text-xs font-semibold">
                Crawler Speed:
                <span class="font-normal">
                  {{ project.crawler_speed }}
                </span>
              </p>
            </li>
          </ul>
          <button
            @click="selectProject"
            v-if="selectedProjectId"
            class="w-full text-white bg-red-500 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Select
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "ModalSelectProject",
  data() {
    return {
      projectList: [],
      selectedProjectId: null,
      showNoProjectsError: false,
    };
  },
  computed: {
    getProjectId() {
      const store = useScrapersStore();
      return store.projectId;
    },
  },
  methods: {
    selectProject() {
      this.$emit("select-project", this.selectedProjectId);
      this.closeModal();
    },
    closeModal() {
      this.$emit("close-modal");
    },
    async getProjects() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/project/get_all"
        );
        if (response.data.success) {
          this.projectList = response.data.projects;
        } else {
          this.showNoProjectsError = true;
        }
      } catch (error) {
        console.error("Error fetching projects: ", error);
        this.showNoProjectsError = true;
      }
    },
  },
  async created() {
    await this.getProjects();
    this.selectedProjectId = this.getProjectId;
  },
};
</script>

<style scoped>
.fixed.inset-0 {
  display: flex;
}
</style>
