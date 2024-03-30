<template>
  <component :is="component_to_show" :work_array="array_to_show" :item_size_persents="item_size_persents" @selected="check_value"/>
</template>
  
<script setup>
import { defineProps, defineEmits } from 'vue';

const emits = defineEmits(['update:checked']);
const props = defineProps({
  checked: {
    type: Boolean,
  },
  component_to_show: {
    type: Object,
    required: true
  },
  array_to_show: {},
  item_size_persents:{},
  min_count:{},
  max_count:{}
})


const check_value = (value) => {
  emits('update:checked', value);
}

</script>
  
<style scoped></style>
