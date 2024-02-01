<template>
  <div>
    <div>
      <CreateTask @addtask="addtask" />
    </div>
    <div class="wrapper">
      <div class="tag" v-for="(t, i) in tags" :key="i">
        <Tag :tag="t" />
      </div>
    </div>

    <div v-for="(t, i) in tasks" :key="i">
      <Task :text="t.text" :tag="t.tag" @deltask="deletetask(i)" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CreateTask from './components/CreateTask.vue'
import Task from './components/Task.vue'
import Tag from './components/Tag.vue';

let tasks = ref([])
let tags = ref([])

const addtask = (ntask) => {
  tasks.value.push({ text: ntask.text, tag: ntask.tag })

  console.log(`Заметка ${ntask.text} добавлена`)
  console.log(tasks.value)

  if (!tags.value.includes(ntask.tag)) {
    tags.value.push(ntask.tag)
    console.log('Новый тэг')
    console.log(tags.value)
  }
}

const deletetask = (i) => {
  tasks.value.splice(i, 1)
  console.log(`Заметка ${i} удалена`)
  console.log(tasks.value)
}


const getRandomRgba() {
      const randomColor = () => Math.floor(Math.random() * 256);
      const r = randomColor();
      const g = randomColor();
      const b = randomColor();
      const a = Math.random().toFixed(2); // Ограничим до двух знаков после запятой

      return `rgba(${r}, ${g}, ${b}, ${a})`
};
</script>

<style scoped>
.wrapper {
  width: fit-content;
  display: flex;
  flex-wrap: wrap;

  margin: 50px;
}

.wrapper .tag{
  margin: 5px 20px;
}
</style>