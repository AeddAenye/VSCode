<template>
  <div class="inputarea">
    <div class="userinput">
      <input type="text" placeholder="Нужно просто начать" v-model="tasktxt" />
    </div>
    <div>
      <button type="button" class="addtask" @click="taskcreate">
        <img src="../assets/plus.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasktxt: "",
    };
  },
  methods: {
    taskcreate() {
      if (this.tasktxt.trim() !== "") {
        this.$emit("add-task", { text: this.tasktxt });
        this.tasktxt = "";
      }
    },
  },
};
</script>

<style scoped>
.inputarea {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 20px 50px;
    padding: 20px;
    background-color: var(--block-bg);
    border-radius: 15px;
}

.inputarea .userinput {
    width: 90%;
    padding: 0px 20px;
}

.inputarea input {
    width: 100%;
    font-size: 1.5rem;
    padding: 10px;
    border-radius: 10px;
    border: none;
}

.inputarea button.addtask  {
    background-color: rgb(126, 187, 240);
}

.inputarea button:hover {
    background-color: rgb(88, 170, 242);
}

.inputarea button:active {
    scale: 0.95;
}
</style>