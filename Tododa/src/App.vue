<template>
  <div>
    <div>
      <CreateTask @addtask="addtask" />
    </div>

    <div>
      <div v-for="(task, i) in tasks" :key="i">
        <Task :text="task.text" :tag="task.tag" @deltask="deletetask(i)" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CreateTask from './components/CreateTask.vue'
import Task from './components/Task.vue'

let tasks = ref([])
let tags = []



const addtask = (ntask) => {
  tasks.value.push({ text: ntask.text, tag: ntask.tag });

  console.log(`Заметка ${ntask.text} добавлена`);
  console.log(tasks.value);

  if (!tags.includes(ntask.tag)) {
    tags.push(ntask.tag);
    console.log('Новый тэг');
  }
};

const deletetask = (i) => {
  tasks.value.splice(i, 1)
  console.log(`Заметка ${i} удалена`)
  console.log(tasks);
}
</script>
