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
