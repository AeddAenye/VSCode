<template>
  <div>
    <CreateTask @addtask="AddTask" />
  </div>
  <div class="wrapper">
    <Tag v-for="(tag, i) in tags" :key="i"
      :style="{ backgroundColor: rgba(tag.r, tag.g, tag.b, i === selectedTagIndex ? 0.7 : 0.3), cursor: 'pointer' }"
      :tag="tag.tag" @click="filterTasksByTag(i)" />
  </div>

  <div class="tasks">
    <div v-for="(task, i) in filteredTasks" :key="i" class="task-container" :style="{ backgroundColor: rgba(task.tag) }">
      <Task :text="task.text" :tag="task.tag" :done="task.done" @deltask="DelTask(i)" @donetask="DoneTask(i)" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import CreateTask from './components/CreateTask.vue';
import Task from './components/Task.vue';
import Tag from './components/Tag.vue';

let tasks = ref([]);
let tags = ref([]);
let doned = ref(0);
let selectedTagIndex = ref(null);

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
    let colors = ChangeColor();

    tags.value.push({ tag: newtask.tag, r: colors.r, g: colors.g, b: colors.b, a: colors.a });
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

const rgba = (r, g, b, a) => {
  return `rgba(${r}, ${g}, ${b}, ${a})`;
};

const ChangeColor = () => {
  const randomColor = () => Math.floor(Math.random() * 256);

  return {
    r: randomColor(),
    g: randomColor(),
    b: randomColor(),
    a: 0.3
  };
};

const filterTasksByTag = (index) => {
  if (selectedTagIndex.value === index) {
    selectedTagIndex.value = null;
  } else {
    selectedTagIndex.value = index;
  }
};

const filteredTasks = computed(() => {
  if (selectedTagIndex.value === null) {
    return tasks.value;
  } else {
    const tag = tags.value[selectedTagIndex.value];
    return tasks.value.filter(task => task.tag === tag.tag);
  }
});

onUnmounted(() => {
  SaveData();
});
</script>

<style scoped>
.wrapper {
  width: fit-content;
  display: flex;
  flex-wrap: wrap;
  margin: 100px 50px 50px 50px;
}

.done {
  text-decoration: line-through;
  opacity: 0.5;
}

.tasks {
  display: flex;
  flex-wrap: wrap;
}

.task-container {
  width: calc(33.33333% - 80px);
  height: 320px;
  margin: 20px 40px;
}
</style>
