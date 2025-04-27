<template>
  <div class="flex items-center justify-between p-4 border-b">
    <h2 class="text-xl font-semibold">{{ title }}</h2>
    <div class="flex items-center space-x-2">
      <div class="relative">
        <span
          class="absolute inset-y-0 left-0 flex items-center pl-4 text-3xl text-gray-400"
        >
          <img src="/icons/search-icon.svg" alt="search-icon" />
        </span>
        <input
          :value="value"
          @input="$emit('input', $event.target.value)"
          type="text"
          class="border rounded pl-12 pr-10 py-2 w-full"
          placeholder="Search"
        />
        <span class="absolute inset-y-0 right-0 flex items-center pr-3">
          <button
            class="focus:outline-none focus:shadow-outline text-2xl text-gray-400"
          >
            <img src="/icons/drop-down.svg" alt="drop-down Icon" />
          </button>
        </span>
      </div>
      <div>
        <DropDownButton
          :label="'Filters'"
          :options="filterOptions"
          @change="setDate"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DropDownButton from "@/components/DropDownButton.vue";
import { useScrapersStore } from "@/store/scrapersStore";

export default {
  name: "SearchBar",
  data() {
    return {
      filterOptions: {},
      isCreating: false,
    };
  },
  components: {
    DropDownButton,
  },
  props: {
    title: String,
    value: String,
  },
  computed: {
    getProjectId() {
      const store = useScrapersStore();
      return store.projectId;
    },
  },
  mounted() {
    this.generateDates();
  },
  methods: {
    async createScraper() {
      this.isCreating = true;

      const payload = {
        script_path: "micro_service/test_runner/playwright/main.py",
        args: ["--project-id", toString(this.getProjectId)], // Ensure to call function and convert to string
      };

      axios
        .post("http://127.0.0.1:8000/api/script_runner/run", payload)
        .then((response) => {
          console.log("Response:", response.data);
        })
        .catch((error) => {
          console.error(
            "Error:",
            error.response ? error.response.data : error.message
          );
        })
        .finally(() => {
          this.isCreating = false;
        });
    },
    triggerSearch() {
      this.$emit("input", this.value);
    },
    generateDates() {
      // Your existing method implementation here
    },
    setDate(date) {
      this.$emit("getStartingDate", date);
    },
  },
};
</script>
