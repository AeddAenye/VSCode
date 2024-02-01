<template>
  <div class="task">
    <div class="text">
      <span>{{ text }}</span>
    </div>
    <div class="tag">
      <span>{{ tag }}</span>
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

    tag: {
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
  margin: 20px 0px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--block-bg);
  border-radius: 15px;
  padding: 20px;
}

.task .text {
  width: 80%;
  margin: 0px 20px;
  text-wrap: wrap;
}

.text span{
  width: fit-content;
}

.task .tag{
  color: rgb(103, 102, 102);
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