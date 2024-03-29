<template>
  <div class="task" :style="{ opacity: this.done ? 0.3 : 1 }">

    <div class="top-content">
      <div class="text" :style="{ textDecoration: this.done ? 'line-through' : 'none' }" @click="donetask">
        <span>{{ text }}</span>
      </div>
    </div>

    <div class="bottom-content">
      <div class="tag">
        <span># {{ tag }}</span>
      </div>
      <div class="buttons">
        <button class="delete" type="button" @click="deletetask">
          <img src="../assets/x.svg" draggable="false" />
        </button>
      </div>
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

    tagcolor: {
      type: String,
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

    donetask() {
      this.$emit("donetask");
    }
  },
};
</script>

<style scoped>
.task {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;

  border: 2px solid rgb(203, 203, 203);
  border-radius: 15px;
  padding: 40px 20px 20px 20px;
  height: calc(100% - 40px);
  position: relative;
}

.task.done {
  opacity: 0.5;
  text-decoration: line-through;
}

div {
  transition: all 0.2s ease;
}

.top-content {
  width: 100%;
}

.bottom-content {
  width: 100%;
}

.task .text {
  text-wrap: wrap;
  width: 100%;
}

.bottom-content .tag span{
  display: flex;
  text-wrap: nowrap;
  width: 100%;
  color: rgba(0, 0, 0, 0.5);
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
}

button>img {
  width: 30px;
  height: 30px;
}

button {
  width: 30px;
  height: 30px;
}

button.delete {
  background-color: rgb(255, 143, 143);
  border-radius: 10px;
  padding: 0;
  position: absolute;
  top: 10px;
  right: 10px;

  transition: background-color 0.2s ease;
}

button.delete:hover {
  background-color: rgb(240, 55, 55);
}

button.delete:active {
  scale: 0.95;
}
</style>