<template>
  <div class="task" :style="{ opacity: this.done ? 0.3 : 1}" >
    <div class="text" :style="{textDecoration: this.done ? 'line-through' : 'none' }" @click="donetask">
      <span>{{ text }}</span>
    </div>
    <div class="tag">
      <span># {{ tag }}</span>
    </div>
    <div class="buttons">
      <button class="delete" type="button" @click="deletetask">
        <img src="../assets/x.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },

    tag: {
      type: String,
      required: true,
    },

    done: {
      type: Boolean,
      default: false,
    },
  },

  methods: {
    deletetask() {
      this.$emit("deltask");
    },

    donetask(){
      this.$emit("donetask");
    }
  },
};
</script>

<style scoped>
.task {
  margin: 20px 0px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--block-bg);
  border-radius: 15px;
  padding: 20px;
  cursor: pointer;
}

.task.done {
  opacity: 0.5;
  text-decoration: line-through;
}

div{
  transition: all 0.2s ease;
}

.task .text {
  margin: 0px 20px;
  text-wrap: wrap;
  width: 80%;
}

.text span {
  width: fit-content;
}

.task .tag {
  color: rgba(0, 0, 0, 0.318);
  margin: 0px 20px;
  width: 10%;
  display: flex;
  justify-content: center;
}

.buttons {
  width: 10%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

button {
  margin: 0px 10px;
}

button.delete {
  background-color: rgb(255, 143, 143);
}

.task button.delete:hover {
  background-color: rgb(240, 55, 55);
}

.task button.delete:active {
  scale: 0.95;
}
</style>