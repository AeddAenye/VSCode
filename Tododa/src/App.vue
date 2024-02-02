<template>
  <div>
    <div class="counter">
      <span>{{ doned }} / {{ tasks.length }}</span>
    </div>
    <div>
      <CreateTask @addtask="AddTask" />
    </div>
    <div class="wrapper">
      <Tag v-for="(tag, i) in tags" :key="i" :style="{ backgroundColor: tag.color }" :tag="tag.tag" />
    </div>

    <div v-for="(task, i) in tasks" :key="i">
      <Task :text="task.text" :tag="task.tag" :done="task.done"
        @deltask="DelTask(i)" @donetask="DoneTask(i)" />

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import CreateTask from './components/CreateTask.vue';
import Task from './components/Task.vue';
import Tag from './components/Tag.vue';

let tasks = ref([]);
let tags = ref([]);
let doned = ref(0);

onMounted(() => {
  const localtasks = localStorage.getItem('tasks');
  const localtags = localStorage.getItem('tags');

  if (localtasks) {
    tasks.value = JSON.parse(localtasks);
  }

  if (localtags) {
    tags.value = JSON.parse(localtags);
  }

  doned.value = tasks.value.filter(task => task.done).length;
});

const SaveData = () => {
  localStorage.setItem('tasks', JSON.stringify(tasks.value));
  localStorage.setItem('tags', JSON.stringify(tags.value));
};

const AddTask = (newtask) => {
  tasks.value.push({ text: newtask.text, tag: newtask.tag, done: newtask.done });

  if (!tags.value.find(t => t.tag === newtask.tag)) {
    tags.value.push({ tag: newtask.tag, color: ChangeColor() });
  }
  doned.value += newtask.done ? 1 : 0;
  SaveData();
};

const DoneTask = (i) => {
  tasks.value[i].done = !tasks.value[i].done;
  doned.value += tasks.value[i].done ? 1 : -1;
  SaveData();
};

const DelTask = (i) => {
  const deletedtask = tasks.value.splice(i, 1)[0];
  const tagindex = tags.value.findIndex(tag => tag.tag === deletedtask.tag);

  if (tagindex !== -1 && !tasks.value.some(task => task.tag === deletedtask.tag)) {
    tags.value.splice(tagindex, 1);
  }
  doned.value -= deletedtask.done ? 1 : 0;
  SaveData();
};

const ChangeColor = () => {
  const randomColor = () => Math.floor(Math.random() * 256);
  return `rgba(${randomColor()}, ${randomColor()}, ${randomColor()}, ${0.5})`;
};

onUnmounted(() => {
  SaveData();
});
</script>

<style scoped>
.wrapper {
  width: fit-content;
  display: flex;
  flex-wrap: wrap;
  margin: 50px;
}

.done {
  text-decoration: line-through;
  opacity: 0.5;
}

.counter{
  position: fixed;
  top: 5px;
  left: 5px;
  color: rgba(0, 0, 0, 0.5);
}

@media screen and (min-width: 980px) {
  
}
</style>


