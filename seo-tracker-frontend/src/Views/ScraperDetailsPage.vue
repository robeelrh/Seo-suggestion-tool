<template>
  <div class="bg-gray-50 p-8 w-full max-h-full">
    <ScraperHeader />
    <div class="flex flex-row gap-10">
      <div class="w-2/3">
        <IssuesSummary />
      </div>
      <div class="w-2/6">
        <SemiDonutChart />
      </div>
    </div>
    <div class="flex flex-row py-6 gap-10">
      <div class="w-3/5">
        <HorizontalBarChart />
      </div>
      <div class="w-2/5">
        <VerticalBarChart />
      </div>
    </div>
    <div class="py-6">
      <ScraperDetailsDataTable />
    </div>
  </div>
</template>

<script>
import IssuesSummary from "@/components/IssuesSummary.vue";
import SemiDonutChart from "@/components/SemiDonutChart.vue";
import HorizontalBarChart from "@/components/HorizontalBarChart.vue";
import VerticalBarChart from "@/components/VerticalBarChart.vue";
import ScraperHeader from "@/components/ScraperHeader.vue";
import ScraperDetailsDataTable from "@/components/ScraperDetailsDataTable.vue";

export default {
  components: {
    IssuesSummary,
    ScraperDetailsDataTable,
    SemiDonutChart,
    HorizontalBarChart,
    VerticalBarChart,
    ScraperHeader,
  },
};
</script>
