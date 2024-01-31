<template>
  <div>
    <div>
      <CreateTask @add-task="addTask" />
    </div>

    <div>
      <div v-for="(task, index) in tasks" :key="index">
        <Task :text="task.text" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import CreateTask from './components/CreateTask.vue';
import Task from './components/Task.vue';

const tasks = ref([]);
const addTask = (newTask) => {
  tasks.value.push(newTask);
};
</script>
