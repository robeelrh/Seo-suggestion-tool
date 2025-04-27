<template>
  <div class="bg-gray-50 p-8 w-full max-h-full">
    <ScraperHeader />
    <div class="py-6">
      <StatusCard :data="cardData" />
    </div>
    <div class="py-6">
      <UrlDetailTable />
    </div>
  </div>
</template>

<script>
import ScraperHeader from "@/components/ScraperHeader.vue";
import StatusCard from "@/components/StatusCard.vue";
import UrlDetailTable from "@/components/UrlDetailTable.vue";

export default {
  name: "UrlDetailsPage",
  components: {
    ScraperHeader,
    StatusCard,
    UrlDetailTable,
  },
  data() {
    return {
      cardData: {
        title: "Status",
        value: this.$route.params.status,
        percentage: "12.2%",
        indexable: this.$route.params.indexable,
        indexed: "indexed",
      },
    };
  },
};
</script>
