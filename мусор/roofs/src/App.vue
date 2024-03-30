<template>
  <div>
    <div class="choosers">
      <Container class="field" :checked="type_check" @update:checked="update_container_state('type', $event)" :component_to_show="chooser"
        :array_to_show="roofs_type" :item_size_persents="50" />
      <Container class="field" :checked="material_check" @update:checked="update_container_state('material', $event)"
        :component_to_show="chooser" :array_to_show="roofs_materials" :item_size_persents="33.333" />
        <Counter class="field" />
    </div>
    <div class="place"></div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import Container from './components/Container.vue'
import Chooser from './components/inContainer/Chooser.vue'
import Counter from './components/inContainer/Counter.vue'

let type_check = ref(false)
let material_check = ref(false)

let chooser = Chooser

let roofs_type = [
  { id: 1, text: 'Глянцевый' },
  { id: 2, text: 'Матовый' },
  { id: 3, text: 'Сатиновый' },
  { id: 4, text: 'Тканевый' }
]

let roofs_materials = [
  { id: 1, text: 'MSD Classic' },
  { id: 2, text: 'MSD Premium' },
  { id: 3, text: 'MSD Evolution' },
  { id: 4, text: 'MSD Cold Stretch' },
  { id: 5, text: 'Teqtum KM2' },
  { id: 6, text: 'Teqtum EURO' },
  { id: 7, text: 'Lumfer' },
  { id: 8, text: 'Bauf 205' },
  { id: 9, text: 'Bauf 230' },
  { id: 10, text: 'Bauf 270' }
]

const update_container_state = (name, value) => {
  if (name === 'type') { type_check.value = value }
  else if (name === 'material') { material_check.value = value }
};
</script>

<style scoped>
.choosers {
  display: flex;
}

.choosers div {
  text-wrap: nowrap;
}

.field{
  margin: 10px;
}
</style>
