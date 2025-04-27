<template>
  <div class="bg-white p-6 rounded-lg w-full flex items-center justify-between">
    <div class="flex flex-col justify-center">
      <div class="text-4xl font-bold text-gray-800 pt-6">{{ data.value }}</div>
      <div class="text-lg text-gray-500 py-6">{{ data.title }}</div>
    </div>
    <div class="flex flex-col items-start justify-center">
      <div>
        <AreaChart />
      </div>
      <div class="text-sm text-green-400">
        <span class="font-bold">{{ data.percentage }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import AreaChart from "@/components/AreaChart.vue";

export default {
  components: {
    AreaChart,
  },
  props: ["data"],
};
</script>
