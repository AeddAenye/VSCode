<template>
  <div>
    <div>
      <CreateTask @addtask="addtask" />
    </div>
    <div class="wrapper">
        <Tag v-for="(tag, i) in tags" :key="i" :style="{ backgroundColor: tag.color }" :tag="tag.tag" />
    </div>

    <div v-for="(t, i) in tasks" :key="i">
      <Task :text="t.text" :tag="t.tag" @deltask="deletetask(i)" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import CreateTask from './components/CreateTask.vue';
import Task from './components/Task.vue';
import Tag from './components/Tag.vue';

let tasks = ref([]);
let tags = ref([]);

const addtask = (ntask) => {
  tasks.value.push({ text: ntask.text, tag: ntask.tag, done: false });

  if (!tags.value.find(tag => tag.tag === ntask.tag)) {
    tags.value.push({ tag: ntask.tag, color: changecolor() });
  }
};

const deletetask = (i) => {
  const deletedtask = tasks.value.splice(i, 1)[0];
  const tagindex = tags.value.findIndex(tag => tag.tag === deletedtask.tag);

  if (tagindex !== -1 && !tasks.value.some(task => task.tag === deletedtask.tag)) {
    tags.value.splice(tagindex, 1);
  }
};

const changecolor = () => {
  const randomColor = () => Math.floor(Math.random() * 256);
  return `rgba(${randomColor()}, ${randomColor()}, ${randomColor()}, ${0.5})`;
};
</script>

<style scoped>
.wrapper {
  width: fit-content;
  display: flex;
  flex-wrap: wrap;
  margin: 50px;
}

</style>
