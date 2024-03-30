<template>
    <div class="pagination">
      <button @click="currentPage > 1 ? onPageChange(currentPage - 1) : null">Previous</button>
      <span>Page {{ currentPage }}</span>
      <button @click="currentPage < totalPages ? onPageChange(currentPage + 1) : null">Next</button>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  // Props
  const currentPageProp = ref(1);
  const totalPagesProp = ref(1);
  
  // Emit event to parent component
  const onPageChange = (pageNumber) => {
    if (pageNumber >= 1 && pageNumber <= totalPagesProp.value) {
      currentPageProp.value = pageNumber;
      emit('pageChange', pageNumber);
    }
  };
  
  // Computed properties
  const currentPage = computed(() => currentPageProp.value);
  const totalPages = computed(() => totalPagesProp.value);
  
  // Export props and methods
  const props = { currentPage, totalPages };
  const emit = defineEmits(['pageChange']);
  </script>
  
  <style scoped>
  .pagination {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .pagination button {
    margin: 0 5px;
    cursor: pointer;
  }
  </style>
  