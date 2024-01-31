<template>
  <div>
    <div>
      <CreateTask @add-task="addtask" />
    </div>

    <div>
      <div v-for="(task, i) in tasks" :key="i" >
        <Task :text="task.text" @deltask="deletetask(i)"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CreateTask from './components/CreateTask.vue'
import Task from './components/Task.vue'

let tasks = ref([])

const addtask = (ntask) => {
  tasks.value.push(ntask);
  console.log(`Заметка ${ntask} добавлена`)
  console.log(tasks.value);
}

const deletetask = (i) => {
  tasks.value.splice(i, 1)
  console.log(`Заметка ${i} удалена`)
  console.log(tasks);
}
</script>
