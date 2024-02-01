<template>
  <div class="task">
    <div class="text">
      <span>{{ text }}</span>
    </div>
    <div class="tag">
      <span># {{ tag }}</span>
    </div>
    <div class="buttons">
      <button class="check" type="button">
        <img src="../assets/check.svg" draggable="false">
      </button>
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
      default: 'Без тэга',
    },

    complete: {
      type: Boolean,
      required: true,
      default: true,
    }
  },

  methods: {
    deletetask() {
      this.$emit("deltask")
    },

    checktask(){
      this.$emit('checktask')
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
  margin: 0px 20px;
  text-wrap: wrap;
  width: 70%;
}

.text span{
  width: fit-content;
}

.task .tag{
  color: rgba(0, 0, 0, 0.318);
  margin: 0px 20px;
  width: 10%;
  display: flex;
  justify-content: center;
}

.buttons{
  width: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
}

button{
  margin: 0px 10px;
}

button.delete {
  background-color: rgb(245, 94, 94);
}

button.check {
  background-color: rgb(72, 234, 124);
}

.task button.delete:hover {
  background-color: rgb(240, 55, 55);
}

.task button.delete:active {
  scale: 0.95;
}
</style>