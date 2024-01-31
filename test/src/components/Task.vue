<template>
  <div class="task">
    <div class="text">
      <span>{{ text }}</span>
    </div>
    <div>
      <button class="delete" type="button" @click="deletetask()">
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
  },
  methods: {
    deletetask() {
      this.$emit("deltask")
    }
  }
};
</script>

<style scoped>
.task {
  margin: 20px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--block-bg);
  border-radius: 15px;
  padding: 20px;
}

.task .text {
  width: calc(100% - 60px);
  margin: 0px 20px;
}

button.delete {
  background-color: rgb(245, 94, 94);
}

.task button.delete:hover {
  background-color: rgb(240, 55, 55);
}

.task button.delete:active {
  scale: 0.95;
}
</style>