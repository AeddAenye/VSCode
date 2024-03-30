<template>
    <div class="form">
        <button type="button" class="minus" @click="minus">-</button>
        <input type="text" name="" id="" v-model="count">
        <button type="button" class="plus" @click="plus">+</button>
    </div>
</template>
  
<script setup>
import { ref, defineProps, defineEmits, watch } from 'vue';

const emits = defineEmits(['selected']);
const props = defineProps({
    min_count: { type: Number },
    max_count: { type: Number }
})
let count = ref(0)

const plus = () => { if (count.value < props.max_count) { count.value += 1 } }
const minus = () => { if (count.value > props.min_count) { count.value -= 1 } }


watch(count, (nval) => {
    if (nval !== null || (nval >= props.min_count && nval <= props.max_count)) { emits('selected', true) }
    else { emits('selected', false) }
})
</script>
  
<style scoped>
.form {
    display: flex;
    align-items: center;
    height: fit-content;
    widows: fit-content;
}

input {
    width: 3ch;
    height: 40px;
    border: none;
    font-size: 1.5rem;
    text-align: center;
}

button {
    width: 40px;
    height: 40px;
    border: none;
    margin: 5px;
    border-radius: 10px;
    font-size: 1.5rem;
}
</style>
  