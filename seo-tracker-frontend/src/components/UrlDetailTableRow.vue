<template>
  <div>
    <div class="grid grid-cols-12 gap-2">
      <div class="col-span-1">
        <h3 class="text-lg text-gray-800">{{ index }}</h3>
      </div>
      <div class="col-span-3">
        <p class="text-lg text-gray-600">{{ error }}</p>
      </div>

      <div class="col-span-2 px-5">
        <span
          :class="getStatusClass(status)"
          class="py-1 px-3 inline-block rounded-lg"
        >
          {{ status }}
        </span>
      </div>
      <div class="col-span-2 pl-24">
        <span class="py-1 inline-block rounded-lg text-lg text-gray-600">
          {{ weight }}
        </span>
      </div>
      <div class="col-span-2 text-center">
        <span
          :class="getPriorityClass(priority)"
          class="py-1 px-3 inline-block rounded-lg"
        >
          {{ priority }}
        </span>
      </div>
      <div class="col-span-2 text-center">
        <button
          @click="toggleAccordian"
          class="text-blue-500 text-lg hover:text-blue-600"
        >
          {{ action }}
        </button>
      </div>
    </div>
    <div class="w-full mt-6" v-if="showSuggestion">
      <span class="text-lg text-gray-800">Suggestion: </span>
      <span class="text-lg text-gray-600">{{ suggestion }}</span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ScrapersDataTable",
  components: {},
  props: {
    originalError: {
      type: String,
      required: true,
    },
    index: {
      type: String,
      required: true,
    },
    error: {
      type: String,
      required: true,
    },
    status: {
      type: String,
      required: true,
    },
    weight: {
      type: String,
      required: true,
    },
    priority: {
      type: String,
      required: true,
    },
    action: {
      type: String,
      required: true,
    },
    suggestion:{
      type: String,
      required: false,
    }
  },
  data() {
    return {
      showSuggestion: false,
    };
  },
  methods: {
    toggleAccordian() {
      this.showSuggestion = !this.showSuggestion;
    },
    getStatusClass(status) {
      switch (status) {
        case "Fixed":
          return "bg-green-50 text-green-400 py-3 px-5 rounded-lg";
        case "Not Fixed":
          return "text-red-500 bg-red-100 py-3 px-5 rounded-lg";
        default:
          return "";
      }
    },
    getPriorityClass(priority) {
      switch (priority) {
        case "Low":
          return "text-green-400";
        case "High":
          return "text-red-500";
        case "Medium":
          return "text-yellow-400";
        default:
          return "";
      }
    },
  },
};
</script>
