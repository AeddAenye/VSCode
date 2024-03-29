<template>
  <div class="inputarea">
    <div class="fields">
      <div class="text">
        <input type="text" placeholder="Нужно просто начать" v-model="txt" />
      </div>

      <div class="tag">
        <input type="text" placeholder="Добавьте тэг" v-model="tag" />
      </div>
    </div>
    <div class="buttons">
      <button type="button" @click="taskcreate">
        <img src="../assets/plus.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      txt: '',
      tag: '',
    }
  },

  methods: {
    taskcreate() {
      let trimedtxt = this.txt.trim()
      let trimedtag = this.tag.trim()
      if (trimedtxt !== '') {
        if (trimedtag === '') {
          trimedtag = 'Без тэга'
        }
        this.$emit('addtask', { text: trimedtxt, tag: trimedtag, done: false })

        this.txt = ''
        this.tag = ''
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
  padding: 20px;
  background-color: rgb(203, 203, 203);
  border-radius: 15px;

  position: fixed;
  top: 20px;
  left: 40px;

  width: calc(100svw - 120px);
  z-index: 5;

  box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.35);
}

.text {
  width: 70%;
}

.tag {
  width: 30%;
}

.fields {
  width: 95%;
}

.buttons {
  width: 5%;
  display: flex;
  justify-content: center;
}

.inputarea input {
  width: 95%;
  font-size: 1.5rem;
  padding: 10px 10px;
  border-radius: 10px;
  border: none;
}

.fields {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 0px 20px;
}

.fields div {
  margin: 0px 20px;
  display: flex;
  justify-content: center;
}

.inputarea button {
  background-color: rgb(126, 240, 170);
  transition: background-color 0.2s ease;
}

.inputarea button:hover {
  background-color: rgb(80, 189, 122);
}

.inputarea button:active {
  scale: 0.95;
}
</style>