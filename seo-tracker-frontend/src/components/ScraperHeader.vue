<template>
  <div class="flex items-center justify-between py-6">
    <div class="flex items-center border rounded">
      <span class="pl-2">
        <img src="/icons/globe.svg" alt="Globe Icon" />
      </span>
      <input type="text" class="p-4" placeholder="Enter country" />
    </div>

    <div class="flex items-center space-x-4">
      <button
        @click="goToCompareRoute"
        class="flex items-center border rounded-lg px-4 py-4 text-gray-500"
      >
        <img src="/icons/switch-horizontal.svg" alt="Switch horizontal icon" />
        <span class="ml-2">Compare</span>
      </button>

      <button
        class="flex items-center border rounded-lg px-4 py-4 text-gray-500"
      >
        <img src="/icons/calendar.svg" alt="calendar Icon" />
        <span class="ml-2">Select Date</span>
      </button>

      <button
        class="flex items-center border rounded-lg px-4 py-4 text-gray-500"
      >
        <img src="/icons/reschedule.svg" alt="reschedule Icon" />
        <span class="ml-2">Reschedule</span>
      </button>

      <button
        class="flex items-center border rounded-lg hover:bg-white hover:text-black px-6 py-4 text-white bg-red-500"
      >
        <img src="/icons/export.svg" alt="export Icon" />
        <span class="ml-2">Export</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToCompareRoute() {
      this.$router.push({ path: "/scraperCompare" });
    },
  },
};
</script>
