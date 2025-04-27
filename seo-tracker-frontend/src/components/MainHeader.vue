<template>
  <div class="flex flex-row justify-between bg-white py-6 px-6 border-b">
    <div class="flex flex-row gap-4">
      <div>
        <img src="/icons/wemasy-logo.svg" alt="Wemasy Logo" />
      </div>
      <div>
        <button
          class="py-1 px-3 flex flex-row gap-2 items-center border rounded-lg hover:bg-gray-50"
        >
          <span>
            <img src="/icons/workspace-icon.svg" alt="icon" />
          </span>
          <span class="text-gray-500">Workspace</span>
          <span> <img src="/icons/drop-down.svg" alt="icon" /> </span>
        </button>
      </div>
      <div>
        <button
          class="py-1.5 px-3 flex flex-row gap-2 items-center border rounded-lg hover:bg-gray-50"
        >
          <span class="text-gray-500">Untitled WEBSITE</span>
          <span>
            <img src="/icons/drop-down.svg" alt="icon" />
          </span>
        </button>
      </div>
      <div class="flex items-center">
        <button class="bg-gray-50 px-3 py-2.5 rounded-lg hover:bg-gray-200">
          <img src="/icons/setting-icon.svg" alt="icon" />
        </button>
      </div>
    </div>
    <div class="flex flex-row gap-4">
      <div class="flex items-center">
        <button class="bg-gray-50 px-3 py-2.5 rounded-lg hover:bg-gray-200">
          <img src="/icons/play.svg" alt="icon" />
        </button>
      </div>
      <div class="flex items-center">
        <button class="bg-gray-50 px-3 py-2.5 rounded-lg hover:bg-gray-200">
          <img src="/icons/bell.svg" alt="icon" />
        </button>
      </div>
      <div>
        <button
          class="flex items-center border rounded-lg hover:bg-white font-semibold hover:text-black px-4 py-1.5 text-white bg-red-500"
        >
          Deploye
        </button>
      </div>
      <div class="w-9 bg-gray-300 bg-opacity-100 rounded-lg">
        <img class="rounded-lg" src="/icons/user-img.png" alt="user-img" />
      </div>
    </div>
  </div>
</template>
