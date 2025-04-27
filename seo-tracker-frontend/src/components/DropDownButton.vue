<template>
  <div class="flex justify-center">
    <button
      @click="toggleDropDownButton"
      class="py-3 px-6 flex flex-row gap-2 items-center border rounded-lg hover:bg-gray-50"
    >
      <span class="text-md text-gray-500">{{ selectedOption }}</span>
      <span>
        <img src="/icons/drop-down.svg" alt="icon" />
      </span>
    </button>

    <ul
      v-if="isOpen"
      class="absolute z-20 bg-white border rounded-lg shadow-lg"
    >
      <li
        v-for="(option, index) in options"
        :key="index"
        @click="selectOption(option, index)"
      >
        <span class="block py-3 px-7 hover:bg-gray-100">{{ index }}</span>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "DropDownButton",
  props: {
    label: {
      type: String,
      required: true,
    },
    options: {
      type: Object,
      required: false,
    },
  },
  data() {
    return {
      isOpen: false,
      selectedOption: "",
    };
  },
  watch: {
    label: {
      immediate: true, // Execute the handler immediately upon creation
      handler(newVal) {
        // Wait until the label prop is available
        if (newVal !== null && newVal !== undefined) {
          this.selectedOption = newVal;
        }
      },
    },
  },
  methods: {
    toggleDropDownButton() {
      this.isOpen = !this.isOpen;
    },
    selectOption(option, index) {
      this.selectedOption = index;
      this.$emit("change", option);
      this.isOpen = false;
    },
  },
};
</script>
