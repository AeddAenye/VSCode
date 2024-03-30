<template>
  <div class="form">
    <div v-for="item in props.work_array" :key="item.id"
         class="item"
         @click="selectItem(item.id)"
         :class="{ 'active': item.id === selectedItem }"
         :style="{ width: `calc(${props.item_size_persents}% - 20px)` }">
      {{ item.text }}
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';

const emits = defineEmits(['selected']);
const props = defineProps({
  work_array: {},
  item_size_persents: {}
})

const selectedItem = ref(null)

const selectItem = (itemId) => {
  selectedItem.value = itemId === selectedItem.value ? null : itemId;
  if(selectedItem.value !== null){
    emits('selected', true)
  }
  else{
    emits('selected', false)
  }
}

</script>

<style scoped>
.form {
  width: fit-content;
  height: fit-content;
  display: flex;
  flex-wrap: wrap;
}

.item {
  box-sizing: border-box;
  font-size: 1.2rem;
  padding: 10px;
  margin: 10px;
  border: 1px solid rgba(0, 0, 0, 0.216);
  border-radius: 10px;
  transition: all 0.4s ease;
  text-align: center;
}

.item.active {
  background: rgb(138, 227, 138);
  border: 1px solid rgb(138, 227, 138);
}

.item:hover {
  background: rgb(201, 245, 201);
}

.item.active:hover {
  background: rgb(138, 227, 138);
  border: 1px solid rgb(138, 227, 138);
}
</style>
