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
          <form
            @submit.prevent="postAddNewProject"
            class="space-y-4"
            action="#"
          >
            <div>
              <label
                for="url"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >URL</label
              >
              <input
                v-model="url"
                type="url"
                name="url"
                class="bg-gray-50 outline-none border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                placeholder="https://www.example.com"
                required
              />
            </div>
            <div>
              <label
                for="max-pages-to-crawl"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Max pages to crawl</label
              >
              <input
                v-model="maxPagesToCrawl"
                type="number"
                name="max-pages-to-crawl"
                placeholder="100"
                class="bg-gray-50 outline-none border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
                required
              />
            </div>
            <div>
              <label
                for="crawling-frequency"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Crawling frequency</label
              >
              <input
                v-model="crawlingFrequency"
                type="number"
                name="crawling-frequency"
                placeholder="0"
                class="bg-gray-50 outline-none border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
                required
              />
            </div>
            <div>
              <label
                for="crawling-speed"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Crawler Speed</label
              >
              <input
                v-model="crawlerSpeed"
                type="number"
                name="crawling-speed"
                placeholder="0"
                class="bg-gray-50 outline-none border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
                required
              />
            </div>

            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full text-white bg-red-500 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              {{ isSubmitting ? "Adding..." : "Add project" }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiService from "@/api/service";
export default {
  name: "ModalAddProject",
  data() {
    return {
      url: "",
      crawlingFrequency: 0,
      maxPagesToCrawl: 0,
      crawlerSpeed: 0,
      isSubmitting: false,
    };
  },
  methods: {
    closeModal() {
      this.$emit("close-modal");
    },
    async postAddNewProject() {
      console.log("creating new project");
      this.isSubmitting = true;
      apiService
        .post("/project/create", {
          url: this.url,
          crawling_frequency: this.crawlingFrequency,
          max_pages_to_crawl: this.maxPagesToCrawl,
          crawler_speed: this.crawlerSpeed,
        })
        .then((response) => {
          const data = response.data;
          this.isSubmitting = false;
          this.$emit("close-modal");
        })
        .catch((error) => {
          console.error("There was an error fetching the data", error);
          this.isSubmitting = false;
        });
    },
  },
};
</script>

<style scoped>
.fixed.inset-0 {
  display: flex;
}
</style>
