<template>
  <div>
    <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-2 sm:px-0">
      <dt class="text-md font-medium leading-6 text-gray-900">
        {{ featureName }}
      </dt>
      <dd class="mt-1 text-md leading-6 text-gray-700 sm:col-span-1 sm:mt-0">
        {{ scraper1Detail }}
      </dd>
      <dd class="mt-1 text-md leading-6 text-gray-700 sm:col-span-1 sm:mt-0">
        {{ scraper2Detail }}
      </dd>
    </div>
  </div>
</template>

<script>
export default {
  name: "ScraperCompareTableRow",
  props: {
    featureName: {
      type: String,
      required: true,
    },
    scraper1Detail: {
      type: String,
      required: true,
    },
    scraper2Detail: {
      type: String,
      required: true,
    },
  },
};
</script>
